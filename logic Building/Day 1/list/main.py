# 1
l = [1, 2, 3, 4]

sum =0
for i in l:
    sum = sum + i
print(sum)


# 2

# nums = [10, 5, 20, 8]

# largenum = nums[0]

# for i in range(len(nums)):
#     if nums[i] > largenum:
#         largenum = nums[i]
# print(largenum)


# 3

num = [1, 2, 3, 4, 6]

count = 0 
for i in num:
    if i%2 == 0:
        count = count+ 1
print(count)


# 4

n = [1, 2, 3]
reversed=[]
for i in range (len(n)-1, -1, -1):
    reversed.append(n[i])
print(reversed)


# 5

d=[1, 2, 2, 3, 4, 4]

unique = []

for i in d:
    if i not in unique:
        unique.append(i)
print(unique)


# 6

num =[10, 20, 4, 45, 99]

largest = num[0]
secondlargest = num[0]

for i in num:
    if i > largest:
        secondlargest = largest
        largest = i
    elif secondlargest > largest:
        secondlargest = i

print(largest, secondlargest)



# 7

# method 1=====>
list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2
print(result)

# method 2=====>

result=[]

for i in list1:
    result.append(i)
    
for i in list2:
    result.append(i)

print(result)


# method 3=====>

list1.extend(list2)
print(list1)


# 8

r = [1, 2, 3, 4]