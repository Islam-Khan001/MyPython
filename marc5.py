import pandas as pd

df = pd.read_csv("mydata1.csv")
print("\nSome Data : ")
print(df)

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
print(((df.Pulse == 110) & (df.Maxpurt5lse == 130)))