name = input("Enter you name  : ")
print("hello " + name)

a = int(input("enter a : "))
b = int(input("enter b : "))
print(a+b)


# this is a list, and is ordered, mutable, store heterogeneous data, allow duplicates
# my_list = [element1, element2, element3, ...]
mylist = ["hello0", "is", "my", "list"]
print(mylist)
mylist.sort()
print(mylist)
list2 = sorted(mylist, reverse=True)
print(list2)


# this is a tuple and is ordered, immutable, store heterogeneous data, allow duplicates
animal = ("dog", "cat", "lion", "penguin", "sea lion", "cat")
trees = ("this", "is", "tree")
print(animal)
print(len(animal))
print(animal[2])
print(animal[1:3])

f1 = list(animal)
f1.pop()
f1.insert(4, "dog")
f1[2] = "kiwi"
print(f1)


# extend - joins two list  animal.extend(trees)
# is - memebership operator
print("this is for loop")
for i in animal:
    print(i)

print("checkng memborship operator")
print(animal is trees)


# this is a set and is unordered, mutable,  cannot store heterogenious data, doesnot allow duplicates

set1 = {"a", "b", "c", "d", "e"}
print(set1)
print(len(set1))

# add update discard
# union - common only one time and other also only one time
# intersection - only common ones

print("conditional statements")


# sir - feb10
# frozenset can take duplicates values
# str, int, tuple, are immutable


# what is anaconda and jupyter and how use it
