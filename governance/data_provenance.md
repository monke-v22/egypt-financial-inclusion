# Data Provenance — Egypt Financial Inclusion Analysis

## Overview
This document records the origin, collection method, and transformation
history of all data used in this project.

---

## Source 1 — World Bank Open Data

| Field | Detail |
|-------|--------|
| Provider | World Bank Group |
| Access Method | Python wbgapi library |
| Collection Script | src/data_collection.py — fetch_world_bank() |
| Raw Output | data/raw/world_bank.csv |
| Clean Output | data/processed/world_bank_clean.csv |
| PostgreSQL Table | world_bank → world_bank_clean |
| Country | Egypt (EGY) |
| Period | 2011–2023 |
| Date Collected | June 2026 |
| License | CC BY 4.0 |
| URL | https://data.worldbank.org |

### Indicators Collected
| Indicator Code | Name |
|---------------|------|
| FX.OWN.TOTL.ZS | account_ownership_pct |
| FP.CPI.TOTL.ZG | inflation_rate |
| NY.GDP.PCAP.CD | gdp_per_capita_usd |
| FB.CBK.BRCH.P5 | bank_branches_per_100k |

### Transformations Applied
1. Index converted from "YR2011" string format to integer (2011)
2. Fully empty columns dropped (bank_capital, domestic_credit)
3. Values cast to float to ensure NaN compatibility
4. Missing values filled via linear interpolation
5. All values rounded to 2 decimal places

---

## Source 2 — FRED (Federal Reserve Bank of St. Louis)

| Field | Detail |
|-------|--------|
| Provider | Federal Reserve Bank of St. Louis |
| Access Method | FRED REST API (JSON) |
| Collection Script | src/data_collection.py — fetch_fred() |
| Raw Output | data/raw/fred_data.csv |
| Clean Output | data/processed/fred_clean.csv |
| PostgreSQL Table | fred_data → fred_clean |
| Country | Egypt |
| Period | 2011–2023 |
| Date Collected | June 2026 |
| License | Public Domain |
| URL | https://fred.stlouisfed.org |

### Indicators Collected

|    Series ID     |         Name          |
|------------------|-----------------------|
| XRNCUSEGA618NRUG | egy_usd_exchange_rate |
| FPCPITOTLZGEGY   | egy_inflation_fred    |

### Transformations Applied

1. Monthly observations aggregated to annual averages
2. Index cast to integer
3. Missing values filled via linear interpolation
4. All values rounded to 2 decimal places

---

## Database

|  Field   |                      Detail                         |
|----------|-----------------------------------------------------|
| Engine   | PostgreSQL 16                                       |
| Database | egypt_finance                                       | 
| Host     | localhost:5432                                      | 
| Tables   | world_bank, world_bank_clean, fred_data, fred_clean |
