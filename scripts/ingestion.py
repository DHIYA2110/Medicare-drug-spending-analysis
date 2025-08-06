import pandas as pd
import numpy as np
import os
from utils import setup_logger

logger = setup_logger("data_ingestion")

def load_and_clean(filepath):
    logger.info(f"Loading dataset: {filepath}")
    df = pd.read_csv(filepath)
    logger.info(f"Initial shape: {df.shape}")

    # Replace blanks with NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    logger.info("Replaced blanks with NaN.")

    # Drop rows missing brand or generic names
    df.dropna(subset=["Brnd_Name", "Gnrc_Name"], inplace=True)
    logger.info("Dropped rows with missing Brand or Generic names.")

    # Fill numeric blanks with 0
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(0)
    logger.info(f"Filled missing numeric columns: {list(num_cols)}")

    # Convert CAGR & change columns to numeric
    for col in df.columns:
        if "CAGR" in col or "Chg" in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Save cleaned data
    os.makedirs("data/processed", exist_ok=True)
    cleaned_path = os.path.join("data/processed", "cleaned_medicare_drug_spending.csv")
    df.to_csv(cleaned_path, index=False)
    logger.info(f"Saved cleaned dataset to {cleaned_path}")

    return df
