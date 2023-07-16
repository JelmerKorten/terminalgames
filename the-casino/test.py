import pandas as pd

df = pd.DataFrame.from_dict({"lat":[-10.1,-11.1,10.1], "lon":[-38.1,-38.1,-38.1]})
df = df.loc[(df["lat"]== -10.1) & (df["lon"] == -38.1)]
print(df.dtypes)