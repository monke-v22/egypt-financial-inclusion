# Data Dictionary — Egypt Financial Inclusion Analysis

## Table: world_bank_clean

| Column | Description | Unit | Source |
|--------|-------------|------|--------|
| year | Reference year | Integer (2011–2023) | World Bank |
| account_ownership_pct | Percentage of adults aged 15+ who report having an account at a bank or mobile money provider | % of adults | World Bank (FX.OWN.TOTL.ZS) |
| inflation_rate | Annual percentage change in consumer price index | % | World Bank (FP.CPI.TOTL.ZG) |
| gdp_per_capita_usd | Total economic output divided by population, in current USD | USD | World Bank (NY.GDP.PCAP.CD) |
| bank_branches_per_100k | Number of commercial bank branches per 100,000 adults | Branches per 100k | World Bank (FB.CBK.BRCH.P5) |

## Table: fred_clean

| Column | Description | Unit | Source |
|--------|-------------|------|--------|
| year | Reference year | Integer (2011–2023) | FRED |
| egy_usd_exchange_rate | Annual average official exchange rate of EGP against USD | EGP per 1 USD | FRED (XRNCUSEGA618NRUG) |
| egy_inflation_fred | Annual inflation rate cross-check from FRED | % | FRED (FPCPITOTLZGEGY) |

## Notes
- Missing values in account_ownership_pct were filled using linear
  interpolation (World Bank surveys this every 3 years via Findex)
- Two indicators were dropped due to no available Egypt data:
  bank_capital_to_assets (FB.BNK.CAPA.ZS) and
  domestic_credit_pct_gdp (FS.AST.DOMS.GD.ZS)
- All values rounded to 2 decimal places during cleaning
