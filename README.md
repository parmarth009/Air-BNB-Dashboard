# 🌍 Global Airbnb Performance & Sentiment Analysis Dashboard | Power BI

## 📌 Project Overview

The **Global Airbnb Performance Dashboard** is a Power BI analytics project designed to uncover business insights from Airbnb listings, hosts, reviews, and customer behavior across multiple cities worldwide.

This dashboard helps stakeholders understand:

- How Airbnb listings evolved over time
- Which property types dominate the platform
- Customer engagement and review behavior
- Host trust & verification patterns
- Seasonal demand trends and market performance
- **Customer sentiment patterns across 2,79,712 reviews** *(new in dev branch)*
- **Booking win probability estimation via Monte Carlo Simulation** *(new in dev branch)*

---

## 🎯 Problem Statement

Airbnb operates across multiple cities with thousands of listings, hosts, and reviews, making it difficult to:

- Track platform growth over time
- Understand customer engagement and **sentiment** patterns
- Analyze trust and verification of hosts
- Identify seasonal demand fluctuations
- Compare performance across property types and cities
- **Detect declining sentiment trends before they impact revenue**
- **Estimate the probability of a listing being booked compared to competing listings based on price, review score, and instant booking availability**

Without centralized analytics, business teams may struggle to make data-driven decisions regarding expansion, pricing strategy, customer trust, and host performance.

---

## ✅ Solution

This Power BI dashboard provides a centralized analytical view of Airbnb platform performance by:

- Visualizing listing growth trends
- Tracking review frequency, customer engagement, and **sentiment scores**
- Evaluating host verification and trust signals
- Identifying seasonal demand patterns
- Comparing room types and city-level performance
- **Surfacing sentiment breakdowns (positive / neutral / negative) by room type and time period**
- **Simulating 1,00,000 booking scenarios to estimate how price, review score, and instant booking affect a listing's competitive win probability**

The dashboard enables faster strategic decisions using interactive visuals and KPI-driven insights.

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Power BI** | Dashboard development & data visualization |
| **Python (pandas)** | Sentiment classification & data preprocessing |
| **Python (numpy, scipy)** | Monte Carlo Simulation for booking win probability |
| **DAX** | KPI calculations, measures, and business logic |
| **Data Modeling** | Relationship building, schema optimization |
| **Excel / CSV** | Source data handling |

---

## 📂 Data Source

**Dataset:** Airbnb Listings & Reviews – Maven Analytics

Sourced from [Maven Analytics Data Playground](https://www.mavenanalytics.io/data-playground). The dataset includes:

- Listings information
- Host details
- Review data (2,79,712 reviews analyzed for sentiment)
- Property types
- Geographic and seasonal trends

---

## ✨ Feature Highlights

### 📊 Business Problems Addressed

- Platform growth tracking
- Customer engagement and sentiment analysis
- Host credibility assessment
- Demand seasonality understanding
- Property performance comparison
- **Revenue risk quantification from negative sentiment**
- **Booking win probability estimation to guide host pricing and quality decisions**

### 📈 Key Visuals Included

**KPI Cards**
- Total Listings · Total Hosts · Property Types · Total Reviews · Cities Covered
- **Net Sentiment Score · Positive / Neutral / Negative Sentiment Counts**
- **Avg Nightly Price · Avg Rating · Avg Review Accuracy · Instant Bookable %**

**Trend Analysis**
- Listing growth over time
- Room-type performance trends
- **Positive sentiment trend (2013–2022)**

**Customer Behavior & Sentiment Analysis**
- Review frequency distribution
- Repeat reviewer patterns
- **Sentiment breakdown by room type (Entire Place, Private Room, Shared Room)**
- **Neutral reviewer identification for conversion targeting**

**Trust & Verification Analysis**
- Host verification insights
- Trust signal evaluation

**Seasonality Analysis**
- Monthly demand trends
- Geographic demand comparison

**Monte Carlo Simulation**
- **Booking win probability by review score (3.5 to 5.0)**
- **Impact of instant booking and price on competitive positioning**

---

## 🧠 Sentiment Analysis Report

> **Scope:** 2,79,712 reviews analyzed across all cities and room types.

### ⚙️ How Sentiment Was Calculated

Since the dataset does not contain textual review comments, a **score-based classification** was used on `review_scores_rating` from `Listings.csv`:

| Sentiment | Condition | Interpretation |
|-----------|-----------|----------------|
| ✅ Positive | rating ≥ 90 | Great experience |
| ⚠️ Neutral | rating 70–89 | Average experience |
| ❌ Negative | rating < 70 | Poor experience |

Classification was done via **Python (pandas)** using `sentiment.py`. Output saved as `listings_with_sentiment.csv` and imported into Power BI.

**Net Sentiment Score = Count(Positive) − Count(Negative) = 1,53,907 − 96,446 = 57,461**

---

### Overall Sentiment Distribution

| Sentiment | Count | Share |
|-----------|-------|-------|
| ✅ Positive | 1,53,907 | 55.02% |
| ⚠️ Neutral | 29,359 | 10.50% |
| ❌ Negative | 96,446 | 34.48% |
| **Net Sentiment Score** | **57,461** | — |

---

### 🔑 Key Findings & Recommendations

**🔴 34.48% Negative Sentiment — Revenue Risk:** Nearly 1 in 3 customers had a poor experience. At 20% churn, that's ~19,000+ lost users. → Implement automated host alert systems, verified quality badges, and recovery discount programs.

**🟡 10.5% Neutral — Untapped Growth Pool:** ~29,359 fence-sitters can be converted into promoters with post-stay micro-surveys, personalized follow-ups, and loyalty incentives.

**📉 Post-2015 Positive Sentiment Decline:** Positive reviews peaked ~22,000–23,000 around 2015, then declined as rapid scaling diluted host quality. → Revisit onboarding standards, add visible sentiment scores on host profiles, and build sentiment forecasting.

**🏠 Entire Place — Biggest Asset, Biggest Risk:** Drives the highest positive sentiment (~1,00,000+) but also the highest negatives — a quality control problem at scale. → Enforce mandatory listing checklists, tiered pricing guidelines, and AI-powered listing audits.

**🚪 Private Room — Significant but Inconsistent:** Second largest sentiment driver in both directions. → Improve host-guest boundary guidelines, add privacy-specific search filters, and a Private Room Trust Program.

**🛏 Shared Room — Near-Zero Engagement:** Negligible sentiment volume signals critical low demand. → Audit viability and consider repositioning as budget/hostel-style stays.

📄 **Full detailed Sentiment Analysis Report:** [Click here](https://github.com/parmarth009/Global-Airbnb-Performance-Dashboard-Power-BI/blob/Dev/sentimental%20analysis%20report.pdf)

---

### 📝 Sentiment Analysis Conclusion

With **55.02% positive sentiments**, Airbnb enjoys majority satisfaction — but the **34.48% negative rate** and post-2015 decline are clear warning signs. The biggest opportunities: converting 29,359 neutral customers into promoters, fixing quality inconsistency in Entire Place listings, and rebuilding Private Room trust. The **Net Sentiment Score of 57,461** is a strong baseline, but targeted programs can push it significantly higher.

> Every percentage point shift from negative to positive represents thousands of retained customers and millions in recovered revenue.

---

## 🎲 Monte Carlo Simulation Report

> **Scope:** 1,00,000 booking scenarios simulated using listing attributes to estimate competitive win probability.

### ⚙️ Problem Statement

Estimate the probability of an Airbnb listing being booked compared to competing listings by simulating customer choices based on factors such as nightly price, review scores, and instant booking availability. Using Monte Carlo Simulation, thousands of booking scenarios are generated to evaluate how changes in these factors affect a listing's chances of securing a booking and outperforming competitors.

### ⚙️ How It Was Calculated

The simulation models customer decision-making across 1,00,000 randomized scenarios. For each scenario, a listing competes against randomly sampled competitors from the dataset. Win probability is calculated as the share of scenarios in which the listing is chosen, based on weighted factors: review score, price competitiveness, and instant booking status.

The simulation was implemented in **Python (numpy, scipy)** via `airbnb_monte_carlo.py` and results were imported into Power BI.

**Key stats used:** Avg Nightly Price: **$867.26** · Avg Rating: **93.4** · Avg Review Accuracy: **9.82** · Instant Bookable: **45.99%**

---

### 🔑 Key Findings & Recommendations

**📊 Win Probability by Review Score:**

| Review Score | Win Probability |
|---|---|
| 3.5 | ~44.6% |
| 4.0 | ~46.6% |
| 4.5 | ~48.0% |
| 4.7 | ~48.6% |
| 4.9 | ~50.1% |
| 5.0 | ~50.8% |

**🏆 The 4.9 Threshold is the Tipping Point:** A listing only starts consistently beating the majority of competitors at a review score of **4.9 and above**. Scores below 4.9 keep hosts in a sub-50% win rate, meaning they lose more bookings than they win in head-to-head scenarios.

**📉 The Competitive Gap is Narrow but Decisive:** The win probability difference between a 3.5 and a 5.0 rated host is just **5.6 percentage points** — but in a high-volume market, this compounding disadvantage translates into significant lost revenue over time.

**⚡ Instant Booking Amplifies the Effect:** With only **45.99% of listings being instantly bookable**, enabling instant booking provides a measurable edge — particularly for mid-range review scores where the margin between winning and losing bookings is smallest.

**💰 Price Sensitivity:** At the market average of **$867.26/night**, price deviations in either direction affect win probability. Overpriced listings at lower review scores suffer the steepest drop in competitiveness.

**Recommended Actions:**
- **Target the 4.9 Score:** Coach hosts below 4.9 with specific improvement checklists to cross the majority-win threshold
- **Enable Instant Booking:** Prioritize getting hosts below 50% win probability to enable instant booking for a quick competitive boost
- **Price-Score Alignment:** Build a pricing recommendation tool that suggests optimal price ranges based on a host's current review score to maximize win probability

---

## 💡 Business Impact & Insights Summary

| Insight | Business Value |
|---------|---------------|
| Peak listing growth ~2015, slowdown during COVID-19 | Informs expansion and recovery strategy |
| Entire Place listings dominate the platform | Focus quality programs on highest-volume category |
| 34.48% negative sentiment rate | Quantifies churn risk; drives host accountability programs |
| Post-2015 sentiment decline | Signals onboarding standard erosion during rapid scaling |
| 29,359 neutral reviews | Actionable conversion opportunity for loyalty programs |
| Shared Room near-zero engagement | Category viability re-evaluation needed |
| Win probability crosses 50% only at 4.9+ review score | Sets a clear quality benchmark for competitive hosts |
| 5.6pp gap between 3.5 and 5.0 rated hosts | Small margin with large compounding revenue impact |

---

## 📸 Dashboard Preview

**Page 1 — Dashboard Overview**

![Page 1 Overview](1st%20page.gif)

**Page 2 — Sentiment Analysis**

![Page 2 Sentiments](2nd%20page.gif)

**Page 3 — Monte Carlo Simulation**

![Page 3 Monte Carlo](3rd%20page.gif)

**Page 4 — Ratings & Review Analysis**

![Page 4 Ratings](4th%20page.gif)

---

## 🗂️ Data Model

**Model View**

![Model View](model_view.png)

The data model consists of **3 tables** connected through two relationships:

| Relationship | From | To | Cardinality | Join Key | Filter Direction |
|---|---|---|---|---|---|
| Reviews → Listings | `Reviews` | `Listings` | Many-to-One (`*` → `1`) | `listing_id` | Single (Listings filters Reviews) |
| Listings → listings_with_sentiment | `Listings` | `listings_with_sentiment` | One-to-One (`1` → `1`) | `listing_id` | Single |

**Why this structure?**

- **Reviews ↔ Listings (Many-to-One):** Multiple reviews can belong to a single listing, so `Reviews` sits on the many side (`*`) and `Listings` on the one side (`1`). This allows measures like review counts and reviewer frequency to be sliced and filtered by listing attributes (city, room type, host info) defined in `Listings`.

- **Listings ↔ listings_with_sentiment (One-to-One):** `listings_with_sentiment` is the enriched version of `Listings` generated by the Python sentiment script — it contains all the same listing records with an additional `sentiment` column. The one-to-one relationship ensures every listing maps to exactly one sentiment record, keeping the model clean and avoiding row duplication in visuals.

This star-like schema keeps the model simple and performant, with `Listings` acting as the central reference table bridging raw review data and the derived sentiment data.

---

## 📐 DAX Measures

This project uses **23 DAX measures** in total. Below are the **5 most important** ones:

---

### 1. City Rank (RANKX)

```DAX
City Rank =
RANKX(
    ALL(Listings[city]),
    [Total Listing],
    ,
    DESC
)
```

---

### 2. Cumulative Listings (CALCULATE + FILTER + ALL)

```DAX
Cumulative Listings =
VAR CurrentRank =
    MAXX(
        VALUES(Listings[city]),
        [City Rank]
    )
RETURN
    CALCULATE(
        [Total Listing],
        FILTER(
            ALL(Listings[city]),
            [City Rank] <= CurrentRank
        )
    )
```

---

### 3. Cumulative % (DIVIDE + CALCULATE + ALL)

```DAX
Cumulative % =
DIVIDE(
    [Cumulative Listings],
    CALCULATE(
        [Total Listing],
        ALL(Listings[city])
    )
)
```

---

### 4. Superhost Listings (CALCULATE)

```DAX
Superhost Listings =
CALCULATE(
    COUNT(Listings[listing_id]),
    Listings[host_is_superhost] = "t"
)
```

---

### 5. Net Sentiment Score (CALCULATE)

```DAX
Net Sentiment Score =
CALCULATE(
    COUNTROWS(listings_with_sentiment),
    listings_with_sentiment[sentiment] = "Positive"
)
-
CALCULATE(
    COUNTROWS(listings_with_sentiment),
    listings_with_sentiment[sentiment] = "Negative"
)
```

---

### 🔑 Key DAX Functions Used

| Function | Purpose |
|----------|---------|
| `CALCULATE()` | Changes filter context |
| `FILTER()` | Creates custom filters |
| `ALL()` | Removes filters |
| `DIVIDE()` | Safe division |
| `RANKX()` | Creates rankings |

---

📄 **The remaining 18 DAX measures are documented here:** [List of all DAX Measures created.md](https://github.com/parmarth009/Global-Airbnb-Performance-Dashboard-Power-BI/blob/Dev/List%20of%20all%20DAX%20Measures%20created.md)

---

## ⚙️ Setup & Reproduction Instructions

### Step 1 — Prerequisites

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (latest version)
- [Python 3.x](https://www.python.org/downloads/) (for running the sentiment and Monte Carlo scripts)

### Step 2 — Download This Repository

Click the green **Code** button → **Download ZIP** → Extract on your computer.

### Step 3 — Download the Dataset

> ⚠️ The raw dataset is **not included** in this repository due to file size limits. Download it separately.

📥 [Download Datasets.zip from Google Drive](https://drive.google.com/file/d/1Eraw8D2gnL5OYuK6ENYAqdsOhEfT9Gx2/view?usp=drive_link)

Once downloaded:
1. Extract the zip file
2. You will get a folder called `Airbnb Data` containing 4 files:
   - `Listings.csv` ← used for sentiment analysis and Monte Carlo simulation
   - `Listings_data_dictionary.csv`
   - `Reviews.csv`
   - `Reviews_data_dictionary.csv`
3. Place these files inside `data/raw/`:

```
Air-BNB-Dashboard/
├── data/
│   └── raw/
│       ├── Listings.csv
│       ├── Listings_data_dictionary.csv
│       ├── Reviews.csv
│       └── Reviews_data_dictionary.csv
├── sentiment.py
├── airbnb_monte_carlo.py
└── Air Bnb Dashboard.pbit
```

---

### Step 3.5 — Generate the Sentiment File (Python)

> ⚠️ This step is **required** before opening the Power BI dashboard. The sentiment analysis page depends on `listings_with_sentiment.csv` which is generated by this script.

**Install the required Python library:**
```bash
pip install pandas
```

**Run the sentiment script:**

1. Copy `Listings.csv` from `data/raw/` into the same folder as `sentiment.py`
2. Open a terminal or command prompt in that folder
3. Run:
```bash
python sentiment.py
```

4. A new file called `listings_with_sentiment.csv` will be generated in the same folder
5. Move this file into `data/raw/`:

```
Air-BNB-Dashboard/
├── data/
│   └── raw/
│       ├── Listings.csv
│       ├── listings_with_sentiment.csv  ← generated by sentiment.py
│       ├── Listings_data_dictionary.csv
│       ├── Reviews.csv
│       └── Reviews_data_dictionary.csv
├── sentiment.py
├── airbnb_monte_carlo.py
└── Air Bnb Dashboard.pbit
```

---

### Step 3.6 — Run the Monte Carlo Simulation (Python)

> ⚠️ This step is **required** for the Monte Carlo simulation page in the dashboard.

The Monte Carlo simulation script `airbnb_monte_carlo.py` is **already included in this repository**. You do not need to write or download it separately.

**Install the required Python libraries:**
```bash
pip install pandas numpy scipy
```

**Run the Monte Carlo script:**

1. Copy `Listings.csv` from `data/raw/` into the same folder as `airbnb_monte_carlo.py`
2. Open a terminal or command prompt in that folder
3. Run:
```bash
python airbnb_monte_carlo.py
```

4. The output file will be generated in the same folder
5. Move it into `data/raw/` alongside the other CSV files

---

### Step 4 — Open the Dashboard in Power BI

1. Open `Air Bnb Dashboard.pbit` in Power BI Desktop
2. When prompted to connect a data source, navigate to your `data/raw/` folder
3. Select the CSV files as the data source
4. Click **Load** and let Power BI refresh
5. All visuals will populate automatically ✔

---

## ❓ Frequently Asked Questions

Have questions about the data cleaning process, sentiment methodology, data model design, DAX measures, or future roadmap?

📄 **[Read the full FAQs here](https://github.com/parmarth009/Global-Airbnb-Performance-Dashboard-Power-BI/blob/Dev/Frequently%20Asked%20Questions%20.md)**

---

## 🚀 Future Improvements

- Add predictive analytics for booking trends
- Integrate real-time Airbnb API data
- Add drill-through city-level insights
- Build forecasting models for demand analysis
- **Automate sentiment scoring pipeline using NLP models**
- **Add sentiment trend alerts for hosts and cities**
- **Build a neutral-reviewer conversion tracking dashboard**
- **Extend Monte Carlo simulation with more competitive factors (amenities, location score, response rate)**
- **Build an interactive what-if simulator for hosts to test pricing and quality scenarios**

---

## 👨‍💻 Author

**Parmarth Sharma** — Data Analyst

---

> 📌 *This README reflects the `dev` branch, which includes the latest Sentiment Analysis and Monte Carlo Simulation layers built on top of the core performance dashboard.*
