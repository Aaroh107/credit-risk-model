"""Download and load the UCI 'Default of Credit Card Clients' dataset.

The data covers 30,000 credit card customers in Taiwan, April-September 2005.
Each row is one customer. The target column `default` is 1 if the customer
failed to pay their bill in October 2005 (the month after the data ends).
"""

from pathlib import Path

import pandas as pd

UCI_DATASET_ID = 350

# Project root = two folders above this file (src/credit_risk/data.py -> project root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_CSV = PROJECT_ROOT / "data" / "raw" / "credit_default.csv"

# The UCI download names columns X1..X23 and Y. We give them readable names.
# Months: the data runs April-September 2005, so "sep" is the most recent month.
COLUMN_NAMES = {
    "X1": "credit_limit",  # total credit given to the customer (NT dollars)
    "X2": "sex",  # 1 = male, 2 = female
    "X3": "education",  # 1 = graduate school, 2 = university, 3 = high school, 4 = other
    "X4": "marriage",  # 1 = married, 2 = single, 3 = other
    "X5": "age",
    # Repayment status each month: -1 = paid on time, 1 = 1 month late, 2 = 2 months late, ...
    # (-2 = no spending that month, 0 = paid the minimum amount)
    "X6": "pay_status_sep",
    "X7": "pay_status_aug",
    "X8": "pay_status_jul",
    "X9": "pay_status_jun",
    "X10": "pay_status_may",
    "X11": "pay_status_apr",
    # Bill amount on the statement each month (how much the customer owed)
    "X12": "bill_amt_sep",
    "X13": "bill_amt_aug",
    "X14": "bill_amt_jul",
    "X15": "bill_amt_jun",
    "X16": "bill_amt_may",
    "X17": "bill_amt_apr",
    # Amount actually paid each month
    "X18": "paid_amt_sep",
    "X19": "paid_amt_aug",
    "X20": "paid_amt_jul",
    "X21": "paid_amt_jun",
    "X22": "paid_amt_may",
    "X23": "paid_amt_apr",
    "Y": "default",  # 1 = defaulted next month, 0 = paid
}


def download_raw(path: Path = RAW_CSV) -> Path:
    """Download the dataset from UCI, rename the columns and save it as a CSV file."""
    from ucimlrepo import fetch_ucirepo  # imported here so loading never needs the internet

    dataset = fetch_ucirepo(id=UCI_DATASET_ID)
    df = pd.concat([dataset.data.features, dataset.data.targets], axis=1)
    df = df.rename(columns=COLUMN_NAMES)

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def load_raw(path: Path = RAW_CSV) -> pd.DataFrame:
    """Load the saved CSV, downloading it first if it is not there yet."""
    if not path.exists():
        download_raw(path)
    return pd.read_csv(path)


if __name__ == "__main__":
    saved = download_raw()
    df = load_raw(saved)
    print(f"Saved {len(df):,} rows x {df.shape[1]} columns to {saved}")
