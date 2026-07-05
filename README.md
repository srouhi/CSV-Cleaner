
# CSV-Cleaner

A simple Python data cleaning pipeline built with **Pandas** and **NumPy**. This project demonstrates common data cleaning tasks performed on messy customer data before analysis.

## Features

The pipeline performs the following cleaning operations:

- Standardizes column names (lowercase with underscores)
- Removes duplicate records based on phone number
- Cleans and validates age values
- Standardizes phone numbers to `(XXX) XXX-XXXX`
- Converts gender values (`Male` → `M`, `Female` → `F`)
- Removes currency symbols and commas from salary values
- Parses mixed birthday formats into a standard datetime format

## Project Structure

CSV-Cleaner/
│
├── cleaner.py         # Data cleaning functions
├── main.py            # Runs the cleaning pipeline
├── input.csv          # Sample raw dataset
├── output.csv         # Cleaned dataset
├── requirements.txt
└── README.md


## Skills Demonstrated

- Data cleaning with Pandas
- Data transformation
- Regular expressions
- Datetime parsing
- Data validation
- Modular Python programming
- ETL pipeline design

