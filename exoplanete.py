import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PS_2023.10.31_06.00.18.csv", skiprows=96)

df

df.describe()

df['disc_year']

df.columns

# +
df2 = df.dropna()

# on garde dans df2 seulement les exoplanètes pour lesquelles on a toutes les informations disponibles
# -

df2

df.set_index('pl_name')

df.columns

# +
#pd.cut(df['pl_eqt'], bins = 
# -

df3 = df.dropna(subset = ['pl_eqt'])
df3

df3['pl_eqt'].describe()

df4 = pd.cut(df3['pl_eqt'], bins = [0,500,1000,1500,2000,2500,3000,3500,4000,4500], labels= ['0-500 K', '500-1000 K', '1000-1500 K', '1500-2000 K', '2000-2500 K', '2500-3000 K', '3000-3500 K', '3500-4000 K', '4000-4500 K'])

df4

df['pl_eqt']

df


