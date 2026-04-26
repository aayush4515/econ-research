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

# extract all country data in a single dataframe
# =============================================================================================

df_all = extractData()
df_all_panel = df_all

# log-transform GDP per captia
df_all_panel.insert(7, "log_gdp_pc", np.log(df_all["gdp_pc"]))

# save the all-country data
saveToCSVandExcel(df_all_panel, "All_Countries", "raw_data", "all_countries")

# =============================================================================================