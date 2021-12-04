

import pandas

df = pandas.read_csv("./cars.csv")

print(df.to_numpy())
print(df.as_matrix())