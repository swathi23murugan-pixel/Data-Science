import pandas as pd
data=[{"txn_id":"T1","category":"Electronics","price":1000.0,"quantity":2},{"txn_id":"T2","category":"Furniture","price":300.0,"quantity":1},{"txn_id":"T3","category":"Electronics","price":None,"quantity":1},{"txn_id":"T1","category":"Electronics","price":1000.0,"quantity":2}]
df=pd.DataFrame(data).drop_duplicates()
df["price"]=df["price"].fillna(df["price"].mean())
df["revenue"]=df["price"]*df["quantity"]
result=df.groupby("category")["revenue"].agg(["sum","mean"]).reset_index()
result.columns=["category","total_revenue","avg_revenue"]
print(result.to_dict("records"))