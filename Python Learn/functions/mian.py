# def hello():
#     print("hello world")
# hello()



# funcion parameter and argument

# positional parameter
def sum (a, b ):
    print(f"sum of function is: {a + b}")
sum(2, 4)
sum(2, 56)

# keyword argument

def hello(name, age):
    print(f"your name is {name} and age is {age} ")
hello(age=22, name="Omkar")

# default argumnet

def sumIs (a, b=45):
    print(a+b)
sumIs(12)


# ex1 -- check it pallindrome or not 

def pallindrome(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]
    if rev == st:
        print("its pallindrome")
    else:
        print("its not pallindrome")

pallindrome("NAMAN")
pallindrome("OMKAR")
