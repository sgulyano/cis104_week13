import pandas as pd
# s = pd.Series([1,3,'ABC', [4,5,6]])
# print(s, type(s), s.dtype)
# df = pd.DataFrame([[1,2,3,4],[6,7,8,9],[10,11,12,13]], columns=["ก","ข","ค","ง"])
# # print(df)
# df2 = pd.DataFrame({'a':[[1,2],[3,4]], 'b':[1.2, 3.4]})
# print(df2)
# print(df2.dtypes)



df3 = pd.DataFrame([{'a':1, 'b':2}, {'a':4, 'c':5}, {'a':4, 'b':3, 'c':5}])
print(df3)
# df3 = df3.fillna(value=0)
# df3.bfill(inplace=True)
# print(df3)
df3.dropna(axis='index', how="all", inplace=True)
print(df3)



# print(df3.loc[1:,['a','c']])
# print(df3.iloc[1:,[0,2]])

# print(df3.to_json(orient="table"))

# print(df3.dtypes)
# df3.to_csv('out.csv')
# d = pd.read_csv('week8\\table.csv')
# print(d)

# x = pd.read_json('test.json')
# print(x)

# x = pd.read_json('test2.json')
# print(x)