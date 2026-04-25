from constants import indicators, countries
import pandas as pd
import wbgapi as wb

# function to extract data for a particular country
def extractCountryData(country):
    df = wb.data.DataFrame(
        indicators,
        economy=country,
        time=range(1995, 2026),
        labels=True
    ).reset_index()

    return df

# function to save the dataframe to an excel and csv file, country too if provided
def saveToCSVandExcel(df, country=None):
    df.to_csv(f"DATA_CSV/{country}_raw_data.csv", index=False)
    df.to_excel(f"DATA_XLSX/{country}_raw_data.xlsx", index=False)

