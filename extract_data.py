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
    saveToCSVandExcel(df_panel, country)

    # set the global data frame
    df_curr = df_panel
