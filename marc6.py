# iris or titanic

# Today topic -- 
import pandas as pd


df = pd.read_csv("iris.csv")
print("\nSome Data : ")
print(df)

print("\nWhole Data in String  : ")
print(df.to_string())

print("\nTop 5 Rows : ")
print(df.head())

print("\nLast 5 Rows : ")
print(df.tail())

print("\nTop 10 Rows : ")
print(df.head(10))

print("\nRandomly Gives any Row : ")
print(df.sample()) # give random data

print("\nInfo : ")
print(df.info())

print("\nDescribe : ")
print(df.describe()) #

print("\nDropping : ")
print(df.dropna().info()) # inplace=True to in all

print("\nFilling : ")
print(df.fillna(0).info())

print("\nDuplicates : ")
print(df.drop_duplicates().info())

print("\nShape : ")
print(df.shape)

print("\nUnique Varities : ")
print(df.variety.unique)

print("\nCounts : ")
print(df.variety.value_counts()[:5])

print("\nGives some : ")
print(df.variety.value_counts()[15:])

print("\nGive one : ") # check
print(df.variety == "Virginica")

print("\nGive this : ")
print(((df.variety == "setosa") & (df.variety == "setosa")))



