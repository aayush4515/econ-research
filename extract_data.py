import wbgapi as wb
import pandas as pd
from constants import indicators, countries
from utils import extractCountryData, saveToCSVandExcel

# extract data for each of the five countires individualy
for country in countries:
    df = extractCountryData(country)
    # save data
    saveToCSVandExcel(df, country)