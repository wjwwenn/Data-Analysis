# FOR LOOP
bag = [10, 1231, 124323, 1243]

i = 0
for item in bag:
    i = i + 1 
    print(i)
    
for item in bag:
    if item == 10:
        print("yes")  # printed 1 yes as in bag, there is only 1 value 10
        
# WHILE LOOP
i = 10
while i < 11:
    print("yup")
    i = i + 1 # printed 1 time as there is only 1 i=10

# CONDITIONALS 
# Boolean - true/false

# CONDITIONAL EXPRESSIONS
# ----------------------- Exercise 1
list_a = [1, 2, 3]
for i in list_a: 
    if i == 2:
        print("yup its two")
    elif i == 1:
        print("something different")
    else:
        print(i)

# ----------------------- Exercise 2 
list_d = ["Justin", "Apple", "Food", 321, "Another", 102]
list_e = []
for i in list_d:
    print(i)

isinstance(3, int)
isinstance("Justin", str)

for i in list_d: 
    if isinstance(i, int):
        list_e.append(i)
        
print(list_e)

# ----------------------- Exercise 3

x = 0 # position from 0
list_d[x]
list_d[x+1]
for item in list_d:
    print(list_d[x])
    x += 1 # set x equal to new variable (x + 1)
    # x = x + 1

# ----------------------- Exercise 4
# Removing the integers from list_d, shifting to list_e
# Keeping list_d with strings
x = 0
list_d = ["Justin", "Apple", "Food", 321, "Another", 102]
list_e = []
for item in list_d:
    if isinstance(item, int):
        list_e.append(item)
        list_d.pop(x)
    x += 1