# Demand Forecasting

A machine-learning project that forecasts product demand and turns those forecasts into inventory reorder recommendations.

## Goal

Given historical product sales, price, promotion, and inventory data, predict future unit demand per product and recommend how many units to reorder.

## Phase 1: foundation

- Generate a realistic daily-sales dataset.
- Build a transparent baseline forecast using recent sales averages.
- Evaluate with MAE and MAPE.
- Add inventory policy: demand during supplier lead time plus safety stock.

## Setup

Requires Python 3.11 or newer.

```bash
cd /Users/I767461/OSS/demand-forecasting
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

## Layout

```text
src/demand_forecasting/  Application and ML code
tests/                   Automated tests
data/raw/                Source data (not committed)
data/processed/          Prepared datasets (not committed)
notebooks/               Exploratory notebooks
```

## First domain rule

```
recommended_order = max(0, forecast_demand_over_lead_time + safety_stock - current_inventory)
```

The next step is to create a synthetic e-commerce sales dataset, then use it to establish a baseline model.
