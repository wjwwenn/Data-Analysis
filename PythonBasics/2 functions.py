str_items = ['Abc', 'JM', 'def', 'ED', 'AD']
new_items = sorted(str_items)
new_items

new_items = sorted(str_items, key=str.lower, reverse=True)

# ------------------------------------ FUNCTIONS
# Separate into String and Num lists
items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int): 
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass
    
print(str_items)
print(num_items)

def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

list_item = [123, 3234, "adfasd"]
items2 = ["Mic", "Phone", list_item]
print(parse_lists(items2))

# ------------------------------------ Exercise 2
# Sum integers/floats in the list
items3 = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

my_sum(items3)

# Count integers/floats in the list
def count_nums(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
    return total

count_nums(items3)

    
# Average integers/floats in the list
def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    #num_of_items = len(my_num_list)
    num_of_items = count_nums(my_num_list)
    return the_sum / (num_of_items * 1.0)

my_avg(items3)
        
# ------------------------------------ Exercise 3
# Combining sum and count
def my_sum_and_count(my_num_list):
    total = 0
    count = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
            count += 1
        return total, count