import wbgapi as wb
import pandas as pd
import numpy as np
from constants import indicators, countries
from utils import extractCountryData, saveToCSVandExcel, convertToPanelFormat, extractData

df_curr = None

# extract data for each of the five countires individualy
for country in countries:
    df = extractCountryData(country)

    # convert the data into panel format
    df_panel = convertToPanelFormat(df, country)

    # log-transform GDP per captia
    df_panel.insert(7, "log_gdp_pc", np.log(df_panel["gdp_pc"]))

    # save data
    saveToCSVandExcel(df_panel, "RAW_DATA", "raw_data", country)

    # set the global data frame
    df_curr = df_panel

    # convert into 5-year averaged values because of missing gini coefficients
    df = df_panel
    df["period_5yr"] = (df["year"] // 5) * 5
    df_5yr = df.groupby(["country", "period_5yr"]).mean(numeric_only=True).reset_index()

    # save the 5-year average data
    saveToCSVandExcel(df_5yr, "5_YEAR_AVG", "5_year", country)

# interpolate gini-coefficients for each country over the 30 year period
for country in countries:
    df_curr["gini_interp"] = df_curr.groupby("country")["gini"].transform(
        lambda x: x.interpolate()
    )
    # save the data
    saveToCSVandExcel(df_curr, "Interpolated", "interpolated", country)

# extract all country data in a single dataframe
# =============================================================================================

df_all = extractData()
df_all_panel = df_all

# log-transform GDP per captia
df_all_panel.insert(7, "log_gdp_pc", np.log(df_all["gdp_pc"]))

# save the all-country data
saveToCSVandExcel(df_all_panel, "All_Countries", "raw_data", "all_countries")

# convert into 5-year averaged values because of missing gini coefficients
df_all_panel["period_5yr"] = (df_all_panel["year"] // 5) * 5
df_5yr = df_all_panel.groupby(["country", "period_5yr"]).mean(numeric_only=True).reset_index()

# save the 5-year average data
saveToCSVandExcel(df_5yr, "All_Countries", "5_year", "all_countries")

# interpolate gini-coefficients for each country over the 30 year period
df_all["gini_interp"] = df_all.groupby("country")["gini"].transform(
    lambda x: x.interpolate()
)

# save the data
saveToCSVandExcel(df_all, "All_Countries", "interpolated", "all_countries")

# =============================================================================================