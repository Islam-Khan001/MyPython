# Today topic -- 
import pandas as pd

df = pd.read_csv("mydata1.csv")
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

print("\nUnique of Pulses : ")
print(df.Pulse.unique)

print("\nCounts : ")
print(df.Pulse.value_counts()[:5])

print("\nGives some : ")
print(df.Pulse.value_counts()[15:])

print("\nGive one : ") # check
print(df.Pulse == 104)

print("\nGive this : ")
print(((df.Pulse == 110) & (df.Maxpulse == 130)))





# task to do 

# drop_duplicated() - to remove duplicates
# df.dropna() - drops null rows but data doesnot change
# df1 = df.dropna() - store in other
# df.dropna(inplace = True) -- to also change data

# df.fillna(0) -- fills but data doesnot change
# df.fillna(0, inplace = True)

# why drop when we have fillna?
# -- because we have to different datatypes




