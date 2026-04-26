import pandas as pd
import wbgapi as wb
from constants import countries

# only extract gini coefficients for countries and print for testing
df = wb.data.DataFrame(
    "SI.POV.GINI",
    economy=countries,
    time=range(1995, 2026),
    labels=True
)

print(df)