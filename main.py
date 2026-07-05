from cleaner import *
import pandas as pd
df = pd.read_csv('input.csv')
def run_pipeline(df):
    df = clean_col_names(df)
    df = remove_duplicates(df)
    df = clean_age(df)
    df = clean_salary(df)
    df = clean_gender(df)
    df = clean_phone_number(df)
    df = clean_bd(df)
    return df

if __name__ == "__main__":
    df = pd.read_csv("input.csv")
    clean_df = run_pipeline(df)
    clean_df.to_csv("output.csv", index=False)
