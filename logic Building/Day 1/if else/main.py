# 1
# num = int(input("enter number check even or odd :- "))

# if num%2 == 0:
#     print("num is even")
# else:
#     print("num is odd")


# 2

# num1 = int(input("Enter a Number check postive, negative or zero :- "))

# if num1 > 0:
#     print("number will be Postive")
# elif num1 < 0:
#     print("number will be Negative")
# else:
#     print("number will be zero")


# 3

# age = int(input("Enter your age:- "))

# if(age>= 18):
#     print("your are eligible for voting")
# else:
#     print("your are not eligible for voting")


# 4

# num1= int(input("enter first num"))
# num2= int(input("enter second num"))

# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num2 is greater than num1")
# else:
#     print("print both number are equal")


# 5

# num1= int(input("enter first num"))
# num2= int(input("enter second num"))
# num3= int(input("enter third num"))

# if num1 >= num2 and num1 >= num3:
#     print("num1 is greater than num2 & num3")
# elif num1 <= num2 and num2 >= num3:
#     print("num2 is greater than num1, num3")
# else:
#     print("num3 is greater than num1 and num2")


# 6

# grade = int(input("enter her percentage:- "))

# if grade >= 90:
#     print("A")
# elif grade >= 75 and grade <= 89:
#     print("B")
# elif grade >= 50 and grade <= 74:
#     print("C")
# else:
#     print("fail")

# 7

# leap = int(input("year:- "))

# if (leap%4 ==0 and leap%100 != 0) or (leap%400 == 0):
#     print("leap year")
# else:
#     print("Not leap year")


# 8
# amt = int(input("enter num:-"))

# if amt < 1000:
#     discount = 5/100
# elif amt >= 1000 and amt < 5000:
#     discount = 10/100
# else:
#     discount = 15/100

# discountAmount = amt * discount
# finalPrice = amt - discountAmount

# print(discountAmount)
# print(finalPrice)


# 9

# a = float(input("enter number :- "))
# b = float(input("enter number :- "))
# op = input("enter operators :- ")

# if op == "+":
#     print(a+b)
# elif op == "-":
#     print(a-b)
# elif op == "/":
#     if b != 0:
#         print( a / b)
#     else:
#         print("Cannot divide by zero")
# elif op == "*":
#     print(a*b)
# else:
#     print("Invalid operator")


# 10

# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))

# # Triangle validity check
# if a + b > c and a + c > b and b + c > a:

#     if a == b and b == c:
#         print("Equilateral Triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")

# else:
#     print("Not a valid triangle")


# 11 atm


balance = float(input("Enter your balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient balance")
elif withdraw <= 0:
    print("Invalid amount")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)