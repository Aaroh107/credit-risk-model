# Credit Default Risk Model

Predicting whether a credit card customer will **default** (stop paying) next month, then turning that
prediction into a lending decision: a probability of default (PD), a 300–900 credit score, an
expected-loss estimate, and the reasons behind each decision.

> 🚧 Work in progress. Built step by step; see the roadmap below.

## Dataset

[UCI Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients):
30,000 credit card customers from Taiwan (2005), with credit limit, demographics, six months of
repayment history, bill amounts and payments. About 22% defaulted.

## Roadmap

- [x] 0. Project setup
- [ ] 1. Download and first look at the data
- [ ] 2. Exploratory data analysis
- [ ] 3. Cleaning and feature engineering
- [ ] 4. Baseline model (logistic regression)
- [ ] 5. XGBoost model and tuning
- [ ] 6. Explainability (SHAP) and calibration
- [ ] 7. Business layer: cut-off, expected loss, credit score
- [ ] 8. Streamlit app
- [ ] 9. Tests, CI and final write-up

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
pip install -e .
```

## Tech stack

Python · pandas · scikit-learn · XGBoost · Optuna · SHAP · Streamlit · pytest
