
# 1
l = [-45, 1, 56, -46, 12, -15, 18, 12]

print("print positive number are")
for i in l:
    if i >= 0:
        print(i)
print("\n print negative number are")
for i in l:
    if i < 0:
        print(i)


# 2
li = [10, 20, 30, 40, 50, 60, 70]

sum = 0
for i in li:
    sum += i
print(f"\n  {sum/ len(li)}")


# 3
g = [-45, 1, 56, -46, 12, -15, 18, 16]

# g.sort()
# print (g)

large = g[0]
index= 0
for i in range(len(g)):
    if g[i] > large:
        large = g[i]
        index = i
print(large, index)


# 4

s= [-45, 1, 56, -46, 12, -15, 18, 16]

largest = s[0]
secondlargest = s[0]
indexOne = 0
indexTwo = 0
for i in s:
    if i > largest:
        secondlargest = largest
        # indexTwo = indexOne
        largest = i
        # indexOne = i 
    elif i > secondlargest:
        secondlargest = i
        # indexTwo = indexOne

print(secondlargest, largest )


# 5
var = [-45, 1, 56, -46, 12, -15, 18, 16]


for i in range (len(var)-1):
    if var[i] < var[i+1]:
        # print("array is sorted")
        continue
    else:
        print("array not sorted")
        break
else:
    print("array is sorted")