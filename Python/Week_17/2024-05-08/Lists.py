# Jason Escalera
# 2024-05-08

# creating a empty list
Lst = []

# using  a for loop to add the number 1-100 to the list
for a in range (1,101):
    Lst.append(a)

#printing the list Lst
print(Lst)

# creating a empty list named  odd
odd = []

# using  a for loop to add the odd number 1-100 to the list odd
for b in range (1,101,2):
    odd.append(b)

# printing the list odd
print(odd)


even = []


for c in range(2,101,2):
    even.append(c)

#printing the list even
print(even)

#create a variable named B that point to the first list that you created
b = Lst

#create a variable named joined that joins even a odd list using a operator
 Joined = even+ odd