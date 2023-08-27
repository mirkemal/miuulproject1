import pandas as pd
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
df = pd.read_csv("C:\\Users\\mirke\\OneDrive\\Masaüstü\\persona.csv")
df.head()
df.shape
df.info

print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())

print(df["PRICE"].nunique())
print(df["PRICE"].value_counts())

print(df["COUNTRY"].value_counts())

df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.groupby("SOURCE").agg({"PRICE": "sum"})
df.groupby(by = ["COUNTRY"]).agg({"PRICE": "mean"})
df.groupby(by = ["SOURCE"]).agg({"PRICE": "mean"})
df.groupby(by = ["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

df.groupby(by = ["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

agg_df.reset_index(inplace=True)
agg_df.head()
df.dtypes

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
mylabels = ["0_18" , "19_23" , "24_30" , "31_40" , "41_" + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

agg_df["customers_level_based"] = agg_df[["COUNTRY", "SOURCE", "SEX", "age_cat"]].agg(lambda x: "_".join(x).upper(), axis=1)
agg_df.head(50)
agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels= ["D", "C", "B", "A"])
agg_df.head(50)
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})


new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]== new_user]

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]== new_user]




































