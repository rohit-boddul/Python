from loguru import logger

lord_names = ["Krishna temple", "Radha temple", "Govinda temple", "Madanmohan temple", "Giridhar temple", "Ramanlal temple"]

# for rohit in range(len(lord_names)):
    # logger.info(f"{rohit+1} temple is '{lord_names[rohit]}'")
# ------------------------------------------------------------------------------------------------------------

# for x in range(5):
#     logger.info((x+1) * " *")

# *
# **
# ***
# ****
# *****

# ------------------------------------------------------------------------------------------------------------
# for i in range(5, 0, -1):
#        print('*' * i)


# rows = 4
# for i in range(rows):
#     print('  ' * i + '* ' * (rows - i))


# for i in range(0, 101, 2):
#       print(i)

numbers = [i for i in range(0, 101, 2)]
print(numbers)

numbers = [i for i in range(0, 102, 3)]
logger.info(numbers)

# ------------------------------------- Paragraph test --------------------------------------------#

# sample paragraph - 

paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

# para_in_list = paragraph.lower().split(" ")
# logger.info(f"Converted paragraph into list = {para_in_list}")

# count = 0
# for search in para_in_list:
#     if search == "the":
#         count = count + 1
# logger.info(f"Total count for 'the' found is {count}")



# ------------------------------------- Problem Statement 1 --------------------------------------------#

# Que1: insert the number in the list and should not change the ordering of the list but WITHOUT using any built-in function

list = [5, 18, 77, 108, 930]
number_to_insert = 100 

# by using built-in functions
updated_list = list.append(number_to_insert)
updated_list = list.sort()
logger.info(list)


# without using in built-in function --> 
list = [5, 18, 77, 108, 930]
number_to_insert = 100 

index = 0
for search in list:
    if search > number_to_insert:
        index = index 
        break
    else:
        index = index + 1
logger.info(f"Index comes to = {index}")

list.append(None)
logger.info(list)
length = len(list)
logger.info(f"Length of list = {length}")
logger.info(index)

for i in range (len(list)-1, index, -1):
    list[i] = list[i-1]
    list[index] = number_to_insert
logger.info(f"sorted list = {list}")




# ------------------------------------- Problem Statement 2 --------------------------------------------#

lst = [202, 165, 89,76, 12]
no_to_insert = 15 

# Que2 - Insert the number 15 in such a way that list is sorted in descending order

index = 0
for r in lst:
    if r <= no_to_insert:
        index = index
        break
    else:
        index = index + 1
logger.info(f"Index = {index}") 

lst.append(None)
logger.info(f"Updated list = {lst}")

for a in range(len(lst)-1, index, -1):
    lst[a] = lst[a-1]
    lst[index] = no_to_insert
logger.info(f"Ordered new elements are = {lst}")


# Table using for loop
# for var1 in range(2, 11):
#     for var2 in range(1, 11):
#         print(var1 * var2, end = "\t")
#     print()

for r1 in range(10, 110, 10):
    for r2 in range(1, 11):
        print(r1 * r2, end = "\t")
    print()