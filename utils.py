from constants import indicators, countries
import pandas as pd
import wbgapi as wb
import os

# function to extract data for a particular country
def extractCountryData(country):
    df = wb.data.DataFrame(
        indicators,
        economy=country,
        time=range(1995, 2026),
        labels=True
    ).reset_index()

    # replace the column names with indicator names instead of indicator codes
    df["series"] = df["series"].replace(indicators)

    return df

# function to save the dataframe to an excel and csv file, country too if provided
def saveToCSVandExcel(df, folder, type=None, country=None):
    # create the directories if they do not exist
    csv_folder = f"CSV_DATA/{folder}"
    xlsx_folder = f"XLSX_DATA/{folder}"

    os.makedirs(csv_folder, exist_ok=True)
    os.makedirs(xlsx_folder, exist_ok=True)

    df.to_csv(f"{csv_folder}/{country}_{type}.csv", index=False)
    df.to_excel(f"{xlsx_folder}/{country}_{type}.xlsx", index=False)

# function to convert data into panel format
def convertToPanelFormat(df, country=None):
    df_long = df.melt(
        id_vars=["series", "Series"],
        var_name="year",
        value_name="value"
    )

    df_long["year"] = df_long["year"].str.replace("YR", "").astype(int)

    df_final = df_long.pivot_table(
        index=["year"],
        columns="series",
        values="value"
    ).reset_index()

    df_final.insert(0, "country", country)

    return df_final

# function to extract data from all countries at once, also includes panel conversion
def extractData():
    df = wb.data.DataFrame(
        indicators,
        economy=countries,
        time=range(1995, 2026),
        labels=True
    ).reset_index()

    # replace indicator codes with short names
    df["series"] = df["series"].replace(indicators)

    # convert wide to long
    df_long = df.melt(
        id_vars=["economy", "Country", "series", "Series"],
        var_name="year",
        value_name="value"
    )

    # clean year column
    df_long["year"] = df_long["year"].str.replace("YR", "").astype(int)

    # convert long to panel format
    df_panel = df_long.pivot_table(
        index=["economy", "Country", "year"],
        columns="series",
        values="value"
    ).reset_index()

    # clean column names
    df_panel = df_panel.rename(columns={
        "economy": "country_code",
        "Country": "country"
    })

    return df_panel