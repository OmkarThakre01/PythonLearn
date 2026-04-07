# syntax error
# print("hello world" # missing closing paranthesis

# no indentation
# def func():
# print("hello")

 
# try except 

# a = int(input("hey give me num:- "))
# try:
#     print(100/a)
# except ZeroDivisionError:
#     print("sorry you can not divide by zero")
# print("ok i have done division")



# a = int(input("hey give me num:- "))
# try:
#     print(100/a)
# except Exception as err:
#     print(f"sorry you can not {err}")
# print("ok i have done division")



# a = int(input("hey give me num:- "))
# try:
#     print(100/a)
# except Exception as err:
#     print(f"sorry you can not {err}")
# else:
#     print("there is no exception")
# finally:
#     print("i will run no matter what")
# print("ok i have done division")


# raise --> manually throw an exception
age = int(input("hey tell you age:- "))
try:
    if age < 10 or age> 18:
      raise ValueError("sorry , your age must be 10 & 18")
    else:
        print("welcome to the club")
except Exception as err:
    print(f"sorry you can not {err}")

print("the club start soon")