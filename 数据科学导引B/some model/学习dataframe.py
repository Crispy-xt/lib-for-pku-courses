import pandas as pd
import numpy as np

data = [["Tom", 12], ["Jerry", "34"]]
df = pd.DataFrame(data=data, columns=["name", "score"])
print(df)
df = df.drop(columns=["score"])
print(df)
df["python score"] = [56, 78]
print(df)
df.rename(columns={"python score": "python 成绩"}, inplace=True)
df.rename(index={0: 1, 1: 2}, inplace=True)
print(df)
print(df.head(1))
print(df[["name", "python 成绩"]])
print(df.loc[[2, 1]])
print(df.loc[1, "name"])
