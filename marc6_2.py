import pandas as pd

print("\n\nTitanic Data")


df2 = pd.read_csv("titan.csv")
print("\nSome Data : ")
print(df2)

print("\nWhole Data in String  : ")
print(df2.to_string())

print("\nTop 5 Rows : ")
print(df2.head())

print("\nLast 5 Rows : ")
print(df2.tail())

print("\nTop 10 Rows : ")
print(df2.head(10))

print("\nRandomly Gives any Row : ")
print(df2.sample()) # give random data

print("\nInfo : ")
print(df2.info())

print("\nDescribe : ")
print(df2.describe()) #

print("\nDropping : ")
print(df2.dropna().info()) # inplace=True to in all

print("\nFilling : ")
print(df2.fillna(0).info())

print("\nDuplicates : ")
print(df2.drop_duplicates().info())

print("\nShape : ")
print(df2.shape)

# print("\nUnique Varities : ")
# print(df2.parch.unique)

# print("\nCounts : ")
# print(df2.parch.value_counts()[:5])

# print("\nGives some : ")
# print(df2.parch.value_counts()[15:])

# print("\nGive one : ") # check
# print(df2.parch == 2)

# print("\nGive this : ")
# print(((df2.parch == 3) & (df2.parch == 3)))


