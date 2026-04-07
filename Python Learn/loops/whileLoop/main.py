# a=1
# while a <= 30:
#     print(a)
#     a= a + 1

# 1
# a = 678
# while a > 0:
#     print(a % 10)
#     a= a // 10

# 2
# a = 678
# rev =0 
# while a > 0:
#     rev= rev * 10 + a % 10
#     a= a // 10

# print(rev)

# 3
# a = 126
# copy = a
# rev =0 
# while a > 0:
#     rev= rev * 10 + a % 10
#     a= a // 10    
# if copy == rev:
#     print("its plandromic number")
# else:
#     print("its not plandromic number")

# 4
import random 
#  EX-1
# num = random.randint(1, 11)
# guess = int(input("guess your number:"))

# while guess != num:
#     print("the number not equal to guess")
#     guess = int(input("guess your number again:"))
# print("number is equal to your guess")

#  EX-2

num = random.randint(1, 11)
tries = 0

while True:
    guess= int(input("Enter the  guess number"))

    if num == guess:
        print(f"guess number is correct {tries}")
        tries = tries + 1
        break
    elif num > guess:
        print(f"number is greater than guess number ")
        tries = tries + 1
    elif num < guess:
        print(f"number is num less than guess number ")
        tries = tries + 1
    else:
        print(f"num not equal to guess guess again ")
        tries = tries + 1

