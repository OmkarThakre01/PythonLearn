from pathlib import Path
import os


def readFileAndFolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")


def createFile():  
    try:
        readFileAndFolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p, "w") as fs:
                data = input("what you wnat to write in this file :- ")
                fs.write(data)
                print("file created successfully")
        else:
            print("file already exists")
            
    except Exception as err:
        print(f"{err}")

def readFile():
    try:
        readFileAndFolder()
        name = input("please tell your file read :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                print(fs.read())
            print("Read successfully")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("please tell your file name want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for creating a file ")
            print("press 2 for reading a file ")
            print("press 3 for updating a file ")

            res = int(input("enter num"))

            if res == 1:
                name2 = input("please tell your file name want to update :- ")
                p2 = Path(name2)
                p.rename(p2)
            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("write you owerright data - ")
                    fs.write(data)
            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("write you append data - ")
                    fs.write(data)
    except Exception as err:
        print(f"Error: {err}")


def deletfile():
    try:
        readFileAndFolder()
        name = input("please tell your file  want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("no such file exists")
    except Exception as err:
        print(f"Error: {err}")

print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deletion a file ")

check = int(input("please tell your number - "))


if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
elif check == 4:
    deletfile()
else:
    print("no of number be exists")