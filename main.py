# for loops questions

# 1
# num = int(input("enter the number :-"))
# for i in range(num):
#     print("hello world")

# 2
# num = int(input("enter the number :-"))
# for i in range(1, num+1):
#     print(i)

# 3
# num = int(input("enter the number :-"))
# for i in range(num, 0, -1):
#     print(i)

# 4
# num = int(input("enter the number :-"))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

# 5
# n = int(input("enter the number :-"))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(f"your sum is {sum}")

# 6
# n = int(input("enter the number :-"))
# fac = 1
# for i in range(1, n+1):
#     fac = fac * i
# print(f"your fac is {fac}")

# 7
# num = int(input("tell your number:-  "))
# even = 0
# odd = 0
# for i in range(1, num+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"{even}, {odd}")

# 8
# num = int(input("tell your number:-  "))
# for i in range (1, num+1):
#     if num%i == 0:
#         print(i)

# 9
# num = int(input("tell your number:-  "))
# sum = 0
# for i in range (1, num):
#     if num%i == 0:
#         sum = sum + i

# if sum == num:
#     print(f"your number is perfect")
# else:
#     print(f"your number is not perfect")

# 10
# n = int(input("check your number is prime or not:-  "))
# count = 0
# for i in range (1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("number is prime")
# else:
#     print("number is not prime")
    
# 11
# a = "OMKAR"
# b=""
# for i in range(len(a)-1, -1, -1):
#     b= b + a[i]
# print(b)

# 12
# a = "NAMAN"
# b=""
# for i in range(len(a)-1, -1, -1):
#     b= b + a[i]

# if b==a:
#     print("this is pallindrome")
# else:
#     print("this is not pallindrome")

# 13
a= "asf@#$%2345^skjsd23$%323tmkms"

char = 0 
dig = 0
symb = 0

for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char += 1
    else:
        symb +=1
print(f"your digit {dig} \n your char {char} \n your symbole {symb}")