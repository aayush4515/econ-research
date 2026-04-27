# clean the wgi dataset for the five South Asian countries
# Required columns: Year | va_score | cc_score | ge_score

import pandas as pd
from constants import economies, countries

datasets = ["va.csv", "cc.csv", "ge.csv"]

for economy, country in zip(economies, countries):
    # base df with all years
    df_global = pd.DataFrame({
        "Year": range(1996, 2025)
    })

    for dataset in datasets:
        df_curr = pd.read_csv(f"WGI_DATA/{dataset}")
        df_cleaned = df_curr.loc[
            df_curr["Economy (code)"] == economy,
            ["Year", "Governance score (0-100)"]
        ].rename(
            columns={
                "Governance score (0-100)": f"{dataset[0:2]}_score"
            }
        )

        # merge by Year, keeping all years from df_global
        df_global = df_global.merge(
            df_cleaned,
            on="Year",
            how="left"
        )

    # save one file per country
    df_global.to_csv(f"WGI_DATA_CLEANED/{country}_governance.csv", index=False)



