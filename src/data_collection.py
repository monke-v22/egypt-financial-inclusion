import wbgapi as wb
import pandas as pd
import requests

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
        df = wb.data.DataFrame(code, country, time = years).T
        df.columns = [name]
        frames.append(df)

    combined = pd.concat(frames, axis=1)
    combined.index.name = "year"
    combined.to_csv("data/raw/world_bank.csv")
    print("SUCCESFULLY!, World bank data is saved :)")

def fetch_fred():
    FRED_API_KEY = "fb11bef5215ff9d8c629a93df88d7742" 

    series = {
        "XRNCUSEGA618NRUG": "egy_usd_exchange_rate",
        "FPCPITOTLZGEGY":   "egy_inflation_fred",
    }

    frames = []
    for code, name in series.items():
        url = (
            f"https://api.stlouisfed.org/fred/series/observations"
            f"?series_id={code}&api_key={FRED_API_KEY}&file_type=json"
            f"&observation_start=2011-01-01&observation_end=2023-12-31"
        )
        response = requests.get(url)
        data = response.json()
        

        df = pd.DataFrame(data["observations"])[["date", "value"]]
        df["date"] = pd.to_datetime(df["date"])
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df["year"] = df["date"].dt.year
        df = df.groupby("year")["value"].mean().reset_index()
        df = df.rename(columns={"value": name}).set_index("year")
        frames.append(df)

    combined = pd.concat(frames, axis=1)
    combined.index.name = "year"
    combined.to_csv("data/raw/fred_data.csv")
    print("SUCCESFULLY!, FRED data saved :)")

if __name__ == "__main__":
    fetch_world_bank()
    fetch_fred()

