import numpy as np
import pandas as pd

def clean_col_names(df):
    df.columns = (df.columns.str.strip().str.lower() #str.strip() remove whiteness end/beginning
                  .str.replace(" ", "_"))
    return df

def remove_duplicates(df):
    df = df.drop_duplicates(subset=['phone_number'])
    return df

#Age
def clean_age(df): 
    # converr all types to int
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['age'] = np.floor(df['age'])
    # remove all unrealistic ages (0-120)
    df = df[(df['age'] >= 0) & (df['age'] <= 120)] #add df[] for boolean indexing --> so it will return other than T/F
    df['age'] = df['age'].astype('Int64')
    return df

# Phone Number --> convert to standard format (xxx) xxx-xxxx
def clean_phone_number(df):
    df['phone_number'] = df['phone_number'].str.replace(r"\D", "", regex=True) #\D: any non digit char 
    df['phone_number'] = df['phone_number'].apply(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}" if len(x) == 10 else x)
    return df

#Gender -> convert to F/M (unless already)
def clean_gender(df):
    df["gender"] = df['gender'].replace({"Male":"M", "Female":"F"})
    df["gender"] = df["gender"].fillna("N/A")
    return df

#Salary
def clean_salary(df): #remove $ & ','
    df['salary'] =df['salary'].str.replace(r"[\$,]", "", regex=True)
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    return df

#BD --> convert to standard format (YYYY-MM-DD) and remove invalid dates
def clean_bd(df):
    df['birthday'] = pd.to_datetime(df['birthday'],format='mixed', errors='coerce')
    return df

#city
def clean_city(df):
    df["city"] = df["city"].str.title()
    return df
