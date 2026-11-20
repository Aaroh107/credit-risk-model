"""Milestone 1 - First look at the data.

Run this file in PyCharm (green Run button). It prints a summary in the Run panel
and shows two charts. Each chart opens in its own window: CLOSE THE WINDOW to continue.
The charts are also saved to reports/figures/.

Same content as notebooks/01_first_look.ipynb (the notebook is for viewing on GitHub).
"""

import matplotlib.pyplot as plt
import pandas as pd

from credit_risk.data import PROJECT_ROOT, load_raw

FIGURES = PROJECT_ROOT / "reports" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 200)

# ---------------------------------------------------------------- 1. Load the data
df = load_raw()
print(f"{df.shape[0]:,} customers, {df.shape[1]} columns\n")
print("First 5 customers:")
print(df.head())

# ---------------------------------------------------------------- 2. Missing values
print(f"\nMissing values in the whole table: {df.isna().sum().sum()}")

# ---------------------------------------------------------------- 3. How many defaulted?
# The single most important number: what share of customers defaulted.
counts = df["default"].value_counts().sort_index().rename({0: "Paid", 1: "Defaulted"})
print("\nPaid vs defaulted:")
print(counts)
print(f"Default rate: {df['default'].mean():.1%}")
print("-> A model that always says 'paid' would be ~78% accurate but catch zero defaulters.")

ax = counts.plot.bar(color=["#4C72B0", "#C44E52"], rot=0)
ax.set_title("Customers who paid vs defaulted (October 2005)")
ax.set_ylabel("Number of customers")
plt.tight_layout()
plt.savefig(FIGURES / "01_default_counts.png", dpi=120)
print("\n[Chart 1 open - close the window to continue]")
plt.show()

# ---------------------------------------------------------------- 4. Money columns
print("\nBasic statistics for the money columns (NT$):")
print(df[["credit_limit", "age", "bill_amt_sep", "paid_amt_sep"]].describe().round(0))
print("-> Negative bills = the customer overpaid, so the bank owes them money.")

# ---------------------------------------------------------------- 5. Odd category codes
print("\nCategory codes (documented: education 1-4, marriage 1-3):")
for col in ["education", "marriage", "pay_status_sep"]:
    print(f"  {col}: {df[col].value_counts().sort_index().to_dict()}")
print("-> education 0/5/6 and marriage 0 are undocumented. We clean them in Milestone 3.")

# ---------------------------------------------------------------- 6. First hint of what predicts default
rate = df.groupby("pay_status_sep")["default"].mean()
print("\nDefault rate by September repayment status:")
print((rate * 100).round(1).astype(str) + "%")

ax = rate.plot.bar(color="#C44E52", rot=0)
ax.set_title("Default rate by September repayment status")
ax.set_xlabel("-2 no use, -1 on time, 0 minimum paid, 1+ = months late")
ax.set_ylabel("Share who defaulted in October")
ax.yaxis.set_major_formatter(lambda y, _: f"{y:.0%}")
plt.tight_layout()
plt.savefig(FIGURES / "01_default_rate_by_pay_status.png", dpi=120)
print("\n[Chart 2 open - close the window to finish]")
plt.show()

print("\nSummary: paying on time -> ~13-17% default; 2 months late -> ~69% default.")
print(f"Charts saved in {FIGURES}")
