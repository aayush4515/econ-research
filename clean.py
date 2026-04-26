# NOTE: USED ALREADY. DO NOT RUN AGAIN

# clean the data if needed
import pandas as pd
from constants import countries

# drop the percentile columns from top 10% dataset

for country in countries:
    # load the csv data into the dataframe
    df = pd.read_csv(f"WID_DATA_10%/{country}_top_10%.csv", sep=";")

    # drop the percentile column
    df = df.drop(columns=['Percentile '])

    # save the new dataframe to a csv
    df.to_csv(f"WID_DATA_10%_CLEANED/{country}_top_10%.csv", index=False)
