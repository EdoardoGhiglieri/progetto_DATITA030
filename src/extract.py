import pandas as pd
from src import ROOT_DIR, raw_path


def extract_custumers():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_customers.csv')
    return df

def extract_items():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_items.csv')
    return df

def extract_categories():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_categories.csv')
    return df

def extract_orders():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_orders.csv')
    return df

def extract_products():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_products.csv')
    return df

def extract_sellers():
    df = pd.read_csv(ROOT_DIR / raw_path / 'olistPW_2016_sellers.csv')
    return df



if __name__ == "__main__":
    print(extract_orders())