
## Medicare Drug Spending Analysis

## Project Overview

This project aims to analyze trends in Medicare Part D drug spending, identify clusters of drugs based on spending behavior, and forecast future spending. The analysis uses data from 2019 to 2023 and applies data preprocessing, exploratory data analysis (EDA), clustering, time series forecasting, and principal component analysis (PCA) to gain actionable insights.

## Project Structure

medicare-drug-spending-analysis/
|├── data/
|   |── raw/               # Raw dataset
|   └── processed/          # Cleaned dataset
|├── notebooks/
|   |── 1_data_ingestion.ipynb
|   |── 2_clean_spending_data.ipynb
|   |── 3_eda.ipynb
|   |── 4_clustering.ipynb
|   |── 5_forecasting.ipynb
|   └── 6_trend_analysis.ipynb
|├── reports/
|   └── images/             # Visualizations for README
|├── scripts/
|├── logs/
└── README.md


##  Technologies & Tools Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **scikit-learn** for clustering
- **ARIMA (Statsmodels)** for forecasting
- **Prophet (optional)** for alternate forecasting
- **Jupyter Notebook** for analysis
- **Git/GitHub** for version control

 ## Data Ingestion
-Loaded and reviewed dataset: 14,000+ rows.
-Checked for nulls, duplicates, and incorrect data types.
-Removed unnecessary entries (e.g., manufacturer = "Overall")

## Data Cleaning
-Aggregated spending by drug brand.
-Replaced outliers using Winsorization to preserve trend patterns.
-Ensured consistent formatting across all columns.

## Exploratory Data Analysis (EDA)

### Key insights:

- **Total Medicare drug spending has increased** consistently from 2019 to 2023.
- **Top drugs** like *Ozempic*, *Eliquis*, *Jardiance*, and *Trulicity* show explosive YoY growth.
- Manufacturer-wise analysis showed a **few pharma companies dominating spending**, with notable growth from diabetes and cardiovascular drug makers.

###  EDA Graph Example:

![Total Medicare Drug Spending](reports/images/Medicare%20Drug%20Spending.png)

---

##  Clustering of Drugs

###  Objective:
Group drugs based on their annual spending profiles using **K-Means Clustering**.

###  Clustering Insights:

- **Cluster 0**: Low/moderate spending drugs grouped tightly.
- **Cluster 1**: High-growth outliers like *Ozempic*, *Jardiance*, *Trulicity*.
- **Cluster 2**: Mid-spending consistent drugs.
- **Cluster 3**: Extreme outlier (*Eliquis*) dominating total spend.

###  Clustering PCA Plot:

![Clustering PCA Plot](reports/images/clustering.png)

---

## Trend Analysis

###  Drug-Level Trends:
- **Top 5 Fastest-Growing Drugs (by CAGR)**: Ozempic, Farxiga, Jardiance, Mounjaro, Skyrizi.
- **Declining Drugs**: Revlimid and similar brands are seeing drops due to generics/expiry.

###  Manufacturer Trend Plot:

![Manufacturer Spending Trend](reports/images/manufactures%20spending%20trend.png)

---

##  Forecasting (2024–2026)

### objective:
Predict Medicare drug spending for 2024–2026 using ARIMA.

###  Forecast Result:

- **2024 Projected Spend**: ~$600 billion
- **2025 Projected Spend**: ~$650 billion
- **2026 Projected Spend**: ~$700 billion
- **Trend**: Continued exponential growth in healthcare expenditure

###  Forecasting Graph:

![Forecasting](reports/images/forecasting.png)

---

##  Key Takeaways

-  **Spending is becoming more concentrated** in fewer high-demand drugs.
- **Diabetes, heart, and kidney medications are leading the growth**.
- **Some older drugs are declining**, hinting at patent expirations or better alternatives.
- **Forecasts show an urgent need** for cost control or reimbursement reforms.

## Future Improvements

-Add LSTM-based deep learning forecasting.
-Integrate API for real-time Medicare data.
-Use advanced feature engineering: cost per prescription.

## 🚀 How to Run the Project

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/medicare-drug-spending-analysis.git
   cd medicare-drug-spending-analysis
