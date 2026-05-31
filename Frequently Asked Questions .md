# ❓ FAQs — Global Airbnb Performance & Sentiment Analysis Dashboard

---

## Q1: What data cleaning and transformation steps did you perform?

The source dataset from Maven Analytics was largely pre-cleaned, so no major transformations like currency conversion or deduplication were required. The primary data preparation work involved:

- **Sentiment enrichment** — the `listings_with_sentiment.csv` file was generated externally using a Python (pandas) script (`sentiment.py`) that classified each listing's `review_scores_rating` into Positive / Neutral / Negative categories and exported the result as a new CSV, which was then loaded into Power BI
- **DAX-based business logic** — rather than transforming raw data, 23 DAX measures were authored to derive all KPIs and analytical logic directly inside the model. Key examples include `City Rank` (RANKX), `Cumulative Listings`, `Cumulative %`, `Superhost Listings`, and `Net Sentiment Score`

---

## Q2: Why was a score-based sentiment approach used instead of NLP?

The dataset sourced from Maven Analytics **does not contain textual review comments** — only aggregated numerical ratings (`review_scores_rating` out of 100). Rather than treating this as a limitation, a **score-based sentiment classification** was designed using industry-standard customer satisfaction benchmarks:

| Score Range | Sentiment | Interpretation |
|-------------|-----------|----------------|
| ≥ 90 | ✅ Positive | High satisfaction |
| 70 – 89 | ⚠️ Neutral | Average experience |
| < 70 | ❌ Negative | Poor experience |

This approach is well-suited for business analytics because:

- It is **objective and reproducible** — same input always gives same output
- It maps directly to **real-world customer satisfaction benchmarks** used in hospitality and service industries
- It enabled **quantifiable business metrics** like the Net Sentiment Score (57,461), which would be harder to derive cleanly from raw NLP outputs
- It kept the pipeline **lightweight and scalable** — no heavy NLP dependencies, just a clean pandas script

---

## Q3: How was the data model structured and why?

The dataset originally provided **2 tables** — `Listings.csv` and `Reviews.csv`. A third table, `listings_with_sentiment`, was intentionally introduced to keep the model clean and maintainable:

- **Reviews → Listings (Many-to-One):** Multiple reviews naturally belong to a single listing. Placing Reviews on the many side (`*`) and Listings on the one side (`1`) allows review counts and engagement metrics to be correctly sliced by listing attributes like city and room type
- **Listings → listings_with_sentiment (One-to-One):** Rather than adding sentiment columns directly into the Listings table, a separate enriched table was created via the Python script. This keeps the original Listings table clean and unmodified, makes the sentiment layer independently maintainable, and leaves the door open for future sentiment models without disrupting existing relationships
- **Single filter direction** was used on both relationships to avoid ambiguous cross-filtering, keep DAX measure behaviour predictable, and maintain better query performance — a best practice in Power BI data modelling

This star-like schema keeps the model **simple, performant, and scalable** for future additions like new data sources or predictive analytics layers.

---

## Q4: What do the 23 DAX measures cover and why DAX over Power Query?

The 23 DAX measures power every KPI and analytical layer of the dashboard. They fall into **5 functional groups:**

| Group | Measures | Purpose |
|-------|----------|---------|
| **Platform Overview** | `Total Listing`, `Avg Nightly Price`, `Avg Rating` | Quick health snapshot of the platform |
| **Review Quality Breakdown** | `Accuracy`, `Cleanliness`, `Communication`, `Location`, `Value` | Surface which aspects of guest experience are performing well or poorly |
| **City & Cumulative Analysis** | `City Rank`, `Cumulative Listings`, `Cumulative %` | Pareto-style analysis to identify cities driving majority of platform volume |
| **Host & Room Type Segmentation** | `Superhost Listings`, `No Superhost Listings`, `Entire Place`, `Private Room`, `Shared Room`, `Hotel Room` | Direct comparison across host credibility and property categories |
| **Reviewer Behavior & Sentiment** | `Reviewers`, `Reviews per Reviewer`, `Cumulative Reviewers`, `Cumulative % Review Frequency`, `Net Sentiment Score` | Map customer engagement patterns and overall satisfaction health |

**Why DAX over Power Query?** Power Query is the right tool for static data shaping — cleaning, merging, and loading. DAX responds dynamically to slicer selections and filter context, making it the correct choice for any metric that needs to change based on what the user is exploring in the dashboard.

---

## Q5: What future improvements are you planning for this dashboard?

The most significant planned improvement is the integration of a **Monte Carlo Simulation layer** — work on which has already begun. A Python script (`airbnb_monte_carlo.py`) has been developed that simulates **100,000 booking competition scenarios** to model how a listing's review score affects its probability of winning a booking over a competitor.

The simulation builds an **attractiveness score** for each listing based on three factors — review score, instant bookability, and price — and runs probabilistic comparisons against randomly sampled competitor listings drawn from the real dataset's distribution. It answers a direct business question:

> *"If my listing has a review score of 4.5, what is my probability of being booked over a competitor?"*

A **dedicated Monte Carlo Analysis page** will be added to the Power BI dashboard, surfacing these insights interactively for hosts and stakeholders.

