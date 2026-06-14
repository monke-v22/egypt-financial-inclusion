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

def fetch_world_bank():
    frames = []
    for code, name in indicators.items():
        df = wb.data.DataFrame(code, COUNTRY, time = YEARS).T
        df.columns = [name]
        frames.append(df)

compined = pd.concat(frames, axis = 1)
compined.index.name = "year"
compined.to_csv("data/raw/world_bank.csv")
print("SUCCESFULLY!, World bank data is saved :)")

if __name__ == "__main__":
    fetch_world_bank()

