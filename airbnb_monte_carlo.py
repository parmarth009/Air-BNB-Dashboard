import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ── 1. Load data ──────────────────────────────────────────────────────────────
# Automatically finds the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Listings.csv")

df = pd.read_csv(csv_path, encoding='latin1')

# Clean price (remove $ and commas if needed)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# Keep only rows with review scores and price
df = df.dropna(subset=['review_scores_rating', 'price', 'instant_bookable'])

# Convert instant_bookable to 1/0
df['instant_bookable'] = df['instant_bookable'].map({'t': 1, 'f': 0, True: 1, False: 0})

print(f"Working with {len(df):,} listings")

# ── 2. Attractiveness model ───────────────────────────────────────────────────
def attractiveness(review, instant, price, w_review=2.0, w_instant=0.5, w_price=0.01):
    return (w_review * review) + (w_instant * instant) - (w_price * price)

# ── 3. Monte Carlo simulation ─────────────────────────────────────────────────
N = 100_000

mu_review = df['review_scores_rating'].mean()
std_review = df['review_scores_rating'].std()
mu_price   = df['price'].mean()
std_price  = df['price'].std()
p_instant  = df['instant_bookable'].mean()

print(f"\nReview score — mean: {mu_review:.2f}, std: {std_review:.2f}")
print(f"Price        — mean: ${mu_price:.2f}, std: ${std_price:.2f}")
print(f"Instant book — {p_instant:.1%} of listings")

review_thresholds = [3.5, 4.0, 4.5, 4.7, 4.9, 5.0]
results = []

print("\n── Simulation Results ──────────────────────────────────────────")
print(f"{'Review Score':<15} {'Win Probability':<18} {'95% CI'}")
print("-" * 55)

for your_review in review_thresholds:
    wins = 0
    for _ in range(N):
        comp_review  = np.clip(np.random.normal(mu_review, std_review), 1, 5)
        comp_price   = max(np.random.normal(mu_price, std_price), 10)
        comp_instant = np.random.binomial(1, p_instant)

        your_score = attractiveness(your_review, 1, mu_price)
        comp_score = attractiveness(comp_review, comp_instant, comp_price)

        if your_score > comp_score:
            wins += 1

    win_rate = wins / N
    ci = 1.96 * np.sqrt(win_rate * (1 - win_rate) / N)
    results.append((your_review, win_rate, ci))
    print(f"{your_review:<15.1f} {win_rate:<18.1%} ±{ci:.2%}")

# ── 4. Plot ───────────────────────────────────────────────────────────────────
reviews, win_rates, cis = zip(*results)

# ── Color palette & style ─────────────────────────────────────────────────────
BG        = "#0F1117"
PANEL     = "#1A1D27"
ACCENT1   = "#FF385C"   # Airbnb red
ACCENT2   = "#00C9A7"   # teal highlight
GOLD      = "#FFD166"
TEXT_PRI  = "#FFFFFF"
TEXT_SEC  = "#9CA3AF"
GRID_COL  = "#2A2D3A"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    PANEL,
    "axes.edgecolor":    GRID_COL,
    "axes.labelcolor":   TEXT_SEC,
    "axes.titlecolor":   TEXT_PRI,
    "xtick.color":       TEXT_SEC,
    "ytick.color":       TEXT_SEC,
    "grid.color":        GRID_COL,
    "grid.linestyle":    "--",
    "grid.linewidth":    0.6,
    "text.color":        TEXT_PRI,
    "font.family":       "DejaVu Sans",
    "font.size":         11,
})

fig = plt.figure(figsize=(15, 7), facecolor=BG)
fig.subplots_adjust(left=0.07, right=0.97, top=0.82, bottom=0.13, wspace=0.35)

# ── Super title ───────────────────────────────────────────────────────────────
fig.text(0.5, 0.93, "Airbnb Booking Intelligence", ha='center',
         fontsize=22, fontweight='bold', color=TEXT_PRI)
fig.text(0.5, 0.87, "Monte Carlo Simulation  ·  100,000 market scenarios  ·  Win Probability Analysis",
         ha='center', fontsize=11, color=TEXT_SEC)



ax  = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# ── Chart 1 — Win Probability Bars ───────────────────────────────────────────
bar_colors = [ACCENT2 if w >= 0.5 else ACCENT1 for w in win_rates]
bars = ax.bar(reviews, win_rates, width=0.07, color=bar_colors,
              alpha=0.85, zorder=3, linewidth=0)

# Glow effect — duplicate bars slightly wider and very transparent
ax.bar(reviews, win_rates, width=0.10, color=bar_colors, alpha=0.15, zorder=2, linewidth=0)

# Error bars
ax.errorbar(reviews, win_rates, yerr=cis, fmt='none',
            color=TEXT_PRI, capsize=5, capthick=1.5, elinewidth=1.5, alpha=0.6, zorder=4)

# 50% reference line
ax.axhline(0.5, color=GOLD, linestyle='--', linewidth=1.4,
           label='50% baseline (coin flip)', zorder=3, alpha=0.85)

# Value labels on top of bars
for bar, wr in zip(bars, win_rates):
    ax.text(bar.get_x() + bar.get_width() / 2, wr + 0.025,
            f"{wr:.0%}", ha='center', va='bottom',
            fontsize=10, fontweight='bold', color=TEXT_PRI)

ax.set_xlabel("Your Review Score", labelpad=10, fontsize=11)
ax.set_ylabel("Booking Win Probability", labelpad=10, fontsize=11)
ax.set_title("Win Probability by Review Score", pad=14, fontsize=13, fontweight='bold')
ax.set_ylim(0, 1.05)
ax.set_xticks(reviews)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
ax.grid(axis='y', zorder=0)
ax.set_axisbelow(True)
legend = ax.legend(fontsize=9, facecolor=PANEL, edgecolor=GRID_COL,
                   labelcolor=TEXT_PRI, framealpha=0.9)

# Subtle panel border
for spine in ax.spines.values():
    spine.set_edgecolor(GRID_COL)
    spine.set_linewidth(0.8)

# ── Chart 2 — Review Score Distribution ──────────────────────────────────────
n, bins, patches = ax2.hist(df['review_scores_rating'], bins=45,
                             edgecolor='none', zorder=3, alpha=0.0)

# Gradient-style coloring: low scores red → high scores teal
norm = plt.Normalize(bins.min(), bins.max())
for patch, left_edge in zip(patches, bins[:-1]):
    t = norm(left_edge)
    r = 1 - t
    g = t
    b = 0.6
    patch.set_facecolor((r * 1.0, g * 0.78, b * 0.67))
    patch.set_alpha(0.85)

# Mean line
ax2.axvline(mu_review, color=GOLD, linestyle='--', linewidth=1.8,
            label=f'Market mean: {mu_review:.2f}', zorder=4)

# 4.5 target line
ax2.axvline(4.5, color=ACCENT2, linestyle='-', linewidth=1.8,
            label='Target score: 4.5', zorder=4, alpha=0.9)

# Shaded "safe zone" above 4.5
ax2.axvspan(4.5, 5.0, alpha=0.07, color=ACCENT2, zorder=2)

ax2.set_xlabel("Review Score Rating", labelpad=10, fontsize=11)
ax2.set_ylabel("Number of Listings", labelpad=10, fontsize=11)
ax2.set_title("Competitor Review Score Distribution", pad=14, fontsize=13, fontweight='bold')
ax2.grid(axis='y', zorder=0)
ax2.set_axisbelow(True)
legend2 = ax2.legend(fontsize=9, facecolor=PANEL, edgecolor=GRID_COL,
                     labelcolor=TEXT_PRI, framealpha=0.9)

for spine in ax2.spines.values():
    spine.set_edgecolor(GRID_COL)
    spine.set_linewidth(0.8)

# ── Footer ────────────────────────────────────────────────────────────────────
fig.text(0.5, 0.02,
         f"Based on {len(df):,} listings  ·  Assumptions: instant_bookable=True, price=market mean  ·  N=100,000 iterations",
         ha='center', fontsize=8.5, color=TEXT_SEC, alpha=0.7)

# Save chart to the same folder as the script
output_path = os.path.join(script_dir, "airbnb_monte_carlo.png")
plt.savefig(output_path, dpi=180, bbox_inches='tight', facecolor=BG)
plt.show()
print(f"\nChart saved to: {output_path}")