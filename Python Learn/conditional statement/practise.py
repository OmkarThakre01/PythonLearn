# num1 = int(input("enter num1 :- "))
# num2 = int(input("enter num2 :- "))

# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num2 is greater than num1")
# else:
#     print("num1 and num2 are equal")


# 2)==>
# gender = input("gender is M or F:-")
# if gender == "M":
#     print("gender is male")
# elif gender == "F":
#     print("gender is female ")
# else:
#     print("gender is unknown ")


# 3)==>
# num = int(input("enter number:-"))
# if num%2 == 0 :
#     print(f"the number are even {num}")
# else:
#     print(f"the number are Odd {num}")



# 4)==>
# laepYear = int(input("enter year only:- "))
# if laepYear%4 ==0 and laepYear%100 ==0:
#     print(f"year is leap year {laepYear}")
# else:
#     print(f"year is not leap year {laepYear}")


# 5) ==> if- elif ladder

degree = int(input('enter degree celcius:- '))

if degree < 0:
    print("frezzing cold")
elif degree >=0 and degree < 10:
    print("very cold")
elif degree >= 10 and degree < 20:
    print(" cold")
elif degree >= 20 and degree < 30:
    print("pleasant")
elif degree >= 30 and degree < 40:
    print("hot")
else:
    print("very hot")
