import pandas as pd

df = pd.read_csv("PS_2023.10.31_06.00.18.csv", skiprows=96)

df

df.describe()

df['disc_year']

df.columns

# +
df2 = df.dropna()

# on garde dans df2 seulement les exoplanètes pour lesquelles on a toutes les informati
# -

df2




















