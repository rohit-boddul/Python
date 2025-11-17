from loguru import logger

# List Comprehension in Python

# 1. Syntax when there is only IF condition
new_list_var_name = ["output"      'for loop'     'if condition']

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(num_list) * 0,len(num_list)+2, 2):
    logger.info(i)

# using list comprehension 
new_even_list = [i for i in range(len(num_list) * 0,len(num_list)+2, 2)]
logger.info(new_even_list)

# -------------------------------- EVEN & ODD both in list ------------------------------------------#
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for r in num_list:
    if r % 2 == 0:
        logger.info(f"Even numbers = {r}")
    elif r % 2 != 0:
        logger.info(f"Odd numbers = {r}")
        



messages = [f"Even numbers = {r}" if r % 2 == 0 else f"Odd numbers = {r}" for r in num_list]

for msg in messages:
    logger.info(msg)

