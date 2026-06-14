import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://monke:754899@localhost:5432/egypt_finance"
engine = create_engine(DB_URL)

def clean_world_bank():
    df = pd.read_sql("SELECT * FROM world_bank", engine, index_col="year")

    df.index = df.index.str.replace("YR", "").astype(int)
    df.dropna(axis=1, how="all", inplace=True)
    df.dropna(axis=0, how="all", inplace=True)

    # Explicitly convert to float so NULLs become NaN
    df = df.astype(float)

    df.interpolate(method="linear", limit_direction="both", inplace=True)
    df = df.round(2)

    df.to_sql("world_bank_clean", engine, if_exists="replace", index=True)
    df.to_csv("data/processed/world_bank_clean.csv")
    print("yuppy! world bank cleaned and saved :)")

def clean_fred():
    df = pd.read_sql("SELECT * FROM fred_data", engine, index_col="year")

    df.index = df.index.astype(int)

    df.dropna(axis=1, how="all", inplace=True)
    df.dropna(axis=0, how="all", inplace=True)
    df.interpolate(method="linear", inplace=True)
    df = df.round(2)
    df.to_sql("fred_clean", engine, if_exists="replace", index=True)

    df.to_csv("data/processed/fred_clean.csv")

    print("yuppy yuppy! fred data cleaned and saved :)")

if __name__ == "__main__":
    clean_world_bank()
    clean_fred()





