from loguru import logger

# Features of Tuple 

# 1. ordered - 
# 2. immutable - only we can read the tuple data, can't change any values whilst runing the code
#-------------------------------------------------------------------------------------------------------------#
#SYNTAX

# tuple = (    )

var_name = (1, 2, 3, "Rohit", True, 2.5)
logger.info(f"var names are {var_name}")
logger.info(f"var names are {type(var_name)}")

# slicing in Tuple
logger.info(f"Sliced values are {var_name[1:4]}")

# IN method
if "Rohit" in var_name:
    logger.info("Name is available")

# Method count in Tuple (gives how many values are there in Tuple)
logger.info(f"Count = {var_name.count(2)}")

# len()
logger.info(f"Total len = {len(var_name)}")



# ----------------------------------------- INTERVIEW QUESTIONS ---------------------------------------#
# 1. Write a program to return entire element as a Tuple which can have list in the tuple inputs

# Example: 
# input = test_tuple = ([5,6], [6,7,8,9], [3])
# output = test_tuple = (5,6,6,7,8,8,9,3)

# also talk about the TIME and SPACE complexity 

test_tuple = ([5,6], [6,7,8,9], [3])

complete_list = list(test_tuple)
logger.info(complete_list)

result = []
for r in test_tuple:
    result = result + r
logger.info(tuple(result))

# 2. Write a program to return a tuple which is expontial of given 2 Tuples as an input
tuple1 = [10,2,3,5]
tuple2 = [3,6,4,3]

final_tuple = []
result = []
for i in range(len(tuple1)):
    result = tuple1[i] ** tuple2[i]
    final_tuple.append(result)
print(tuple(final_tuple))














