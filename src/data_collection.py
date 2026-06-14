import wbgapi as wb
import pandas as pd

country = "EGY"
years = range(2011, 2024)
indicators = {
    "FX.OWN.TOTL.ZS": "account_ownership_pct",
    "FB.BNK.CAPA.ZS": "bank_capital_to_assets",
    "FS.AST.DOMS.GD.ZS": "domestic_credit_pct_gdp",
    "FP.CPI.TOTL.ZG": "inflation_rate",
    "NY.GDP.PCAP.CD": "gdp_per_capita_usd",
    "FB.CBK.BRCH.P5": "bank_branches_per_100k",
}


