import pandas as pd

df = pd.DataFrame.from_dict({"lat":[-10,-11,10], "lon":[-38,-38,-38]})
df = df.loc[(df["lat"]== -10) & (df["lon"] == -38)]
print(df)
