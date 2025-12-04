from loguru import logger

# Features of SET - 
# -->
# 1. unordered elements present in the sets
# 2. immuatable data type/structure
# 3. cannot contain any DUPLICATES in SET
# ----------------------------------------------------------------

# USES
# 1. when you don't want any DUPLICATES (duplicate values get discarded)

# ----------------------------------------------------------------
# SET in maths
# -->

# 1. UNION
# 2. INTERSECTION
# 3. DIFFERENCE
# ----------------------------------------------------------------

set_var = {1,2,1,3,4,6}
logger.info(f"{type(set_var)}")
logger.info(f"{set_var}")

# empty set
empty_set = set()
logger.info(f"{type(empty_set)}")

# -------------------------------------------- METHODS in SET -------------------------------------------- #

set_1 = {1, 2, 7, 8, 4, 12}
set_2 = {2, 4, 6, 5, 15}

# 1. UNION (gives all elements from two or more sets but avoids duplicates)
union_result = set_1.union(set_2)
logger.info(union_result)

# 2. INTERSECTION (only matched records)
intersection_result = set_1.intersection(set_2)
logger.info(intersection_result)

# 3. SYMMETRIC DIFFERENCE 
sym = set_1.isdisjoint(set_2)
logger.info(sym)

# 4. ADD 
new_value = set_1.add(455)
logger.info(set_1)

# ----------------------------------------------- QUESTIONS ------------------------------------------ #
# Q1. given two lists. find the missing and additional values in both lists. 

# INPUT = 
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

# OUTPUT =
# missing values in list1 = [8,7]
# additional values in list1 = [1, 2, 3]
# missing values in list2 = [1, 2, 3]
# additional values in list2 = [7, 8]

missing_val = set2 - set1
logger.info(f"Missing values in list1 = {list(missing_val)}")

additional_list1 = set1 - set2
logger.info(f"Missing values in list1 = {list(additional_list1)}")

missing_val_list2 = set1 - set2
logger.info(f"Missing values in list1 = {list(missing_val_list2)}")

additional_list2 = set2 - set1
logger.info(f"Missing values in list1 = {list(additional_list2)}")




# Q2. given 3 arrays, we have to find common elements in 3 sorted lists using set

# INPUT = 
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# OUTPUT = 
# result = [80, 20]

# ------->>
newset1 = set(ar1)
newset2 = set(ar2)
newset3 = set(ar3)

result = newset1.intersection(newset2, newset3)
print(list(result))

















