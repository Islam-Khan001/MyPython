# to print hello world
print("hello world")
print()

# add two numebr
x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))
print("Sum of Num1 and Num2 : ", (x+y))
print()


# calculate the area of triangle
base = int(input("Enter base : "))
height = int(input("Enter height : "))
print("Area of Triangle : ", (.5*base*height))
print()


# swap two numebr b,a = a,b
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print("Before Swapping : ")
print("Num1 : ", num1)
print("Num2 : ", num2)
num1, num2 = num2, num1
print("After Swapping : ")
print("Num1 : ", num1)
print("Num2 : ", num2)
print()


# convert kilometers to meters
kilometer = int(input("Enter Kilometers : "))
print("In Meters : ", kilometer*1000)


# --------------------lAB EX 2 -------------------------
print("LAB EX2-------------")


# convert to farhenhiet

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = 25
print("Celsius:", celsius)
print("Fahrenheit:", celsius_to_fahrenheit(celsius))


# check num is positive negative or Zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


num = -5
print(num, "is", check_number(num))


# check odd or even
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 7
print(num, "is", check_odd_even(num))


# check leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = 2024
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")




# find the largest among three numbers
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = 10
num2 = 20
num3 = 15
print("Largest number is:", find_largest(num1, num2, num3))


