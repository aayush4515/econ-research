import wbgapi as wb
import pandas as pd
import numpy as np
from constants import indicators, countries
from utils import extractCountryData, saveToCSVandExcel, convertToPanelFormat

df_curr = None

# extract data for each of the five countires individualy
for country in countries:
    df = extractCountryData(country)

    # convert the data into panel format
    df_panel = convertToPanelFormat(df, country)

    # log-transform GDP per captia
    df_panel.insert(6, "log_gdp_pc", np.log(df_panel["gdp_pc"]))

    # save data
    saveToCSVandExcel(df_panel, "RAW_DATA", country)

    # convert into 5-year averaged values because of missing gini coefficients

    df = df_panel
    df["period_5yr"] = (df["year"] // 5) * 5
    df_5yr = df.groupby(["country", "period_5yr"]).mean(numeric_only=True).reset_index()

    # save the 5-year average data
    saveToCSVandExcel(df_5yr, "5_YEAR_AVG", country)

    # set the global data frame
    df_curr = df
