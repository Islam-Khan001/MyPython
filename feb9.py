# dictionary

mydict = {'name' : "islam",
          'class' : "mca",
          'year' : 1,
          'items' : ["hello","this", "is", "collection"]}

print(mydict['name']) #prints islam
print(len(mydict))   # prints the length of dictionary
print(mydict.keys())    # prints all the keys 
print(mydict.values())  # prints all the values
print(mydict['items'])  # prints all the items
print(type(mydict))  # prints type of dictionary

# updating a dictionary

mydict['name'] = "hemant"
mydict['age'] = 21
print(mydict)
mydict.update({'age' : 18})
print(mydict)

print(mydict.pop('age'))  # works with any key
print(mydict.popitem())   # pops the last element

copymydict = mydict.copy()

print(mydict)

print()


# ------------------------------------------------------------------------

# loops
# 2 loops - while and for loops

i = 0
print("\nwhile loop : ")
while(i<=10):
    print(i)
    i+=1   # i++ will not work in python

print("\nfor loop : ")

for j in range(15,25,2): # start stop and step
    print(j)


fruitslist = ["mango","kiwi","apple", "banana", "orange"]

print("\niterating list through for loop : ")

for fruit in fruitslist:  # fruit = element in the list
    print(fruit)
    if(fruit == "banana"):
        break


# ------------------------------------------------------------------------
# functions
    
def myfunc(a,b):
    c = a+b
    return c

print("\nReturn from function : ",myfunc(10,20))



# sir - feb10
#  str[0].isalpha and isnumber to check the type
# python pandas and numphy , lib = sklearn, you should learn this
# sypervised machine learning
# deep learning
# actual language processing

