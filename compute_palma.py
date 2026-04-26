# compute the palma ratio using the top 10 and bottom 40% share
import pandas as pd
from constants import countries

for country in countries:
    # load the csv datasets into dataframes
    df_top_10 = pd.read_csv(f"WID_DATA_10%/{country}_top_10%.csv")
    df_bottom_40 = pd.read_csv(f"WID_DATA_40%/{country}_bottom_40%.csv", sep=";")

    # merge by year
    df = pd.merge(df_top_10, df_bottom_40, on="Year", how="inner")

    # compute palma ratio
    df["palma_ratio"] = df["top_10_share"] / df["bottom_40_share"]

    # save the palma ratio for the corresponding country

    # drop the top_10_share and bottom_40_share columns
    df = df.drop(columns=['top_10_share', 'bottom_40_share'])
    df.to_csv(f"PALMA_RATIOS/{country}_palma_ratio.csv", index=False)