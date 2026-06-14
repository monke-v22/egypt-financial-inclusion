import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

DB_URL = "postgresql://monke:754899@localhost:5432/egypt_finance"
engine = create_engine(DB_URL)

def load_world_bank():
    df = pd.read_csv("data/raw/world_bank.csv", index_col="year")
    df.to_sql("world_bank", engine, if_exists="replace", index=True)
    print("SUCCESS! world_bank table loaded :)")

def load_fred():
    df = pd.read_csv("data/raw/fred_data.csv", index_col="year")
    df.to_sql("fred_data", engine, if_exists="replace", index=True)
    print("SUCCESS! fred_data table loaded :)")

if __name__ == "__main__":
    load_world_bank()
    load_fred()

    


