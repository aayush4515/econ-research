import wbgapi as wb
import pandas as pd
import numpy as np
from constants import indicators, countries, economies
from utils import extractCountryData, saveToCSVandExcel, convertToPanelFormat, extractData

df_curr = None

# extract data for each of the five countires individualy
for economy, country in zip(economies, countries):
    df = extractCountryData(economy)

    # convert the data into panel format
    df_panel = convertToPanelFormat(df, economy)

    # log-transform GDP per captia
    df_panel.insert(6, "log_gdp_pc", np.log(df_panel["gdp_pc"]))

    # add the palma ratio columns for each country
    df_palma = pd.read_csv(f"PALMA_RATIOS/{country}_palma_ratio.csv")
    df_panel["palma_ratio"] = df_palma["palma_ratio"]

    # add the WGI indicators: va, cc and ge
    wgi_cols = ["va_score", "cc_score", "ge_score"]
    df_wgi = pd.read_csv(f"WGI_DATA_CLEANED/{country}_governance.csv")
    df_wgi = df_wgi.rename(columns={"Year": "year"})
    df_panel = df_panel.merge(
        df_wgi[["year"] + wgi_cols],
        on="year",
        how="left"
    )

    # save data
    saveToCSVandExcel(df_panel, "RAW_DATA", "raw_data", economy)

    # set the global data frame
    df_curr = df_panel

# extract all country data in a single dataframe
# =============================================================================================

# df_all = extractData()
# df_all_panel = df_all

# # log-transform GDP per captia
# df_all_panel.insert(7, "log_gdp_pc", np.log(df_all["gdp_pc"]))

# # save the all-country data
# saveToCSVandExcel(df_all_panel, "All_Countries", "raw_data", "all_countries")

# =============================================================================================