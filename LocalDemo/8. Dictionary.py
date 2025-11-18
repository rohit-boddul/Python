from loguru import logger

# USE CASES OF DICTIONARY 
#1. NoSQL DB - key:value pair data 
#2. after hitting the API, you will get the response in key:value pair 

labour_with_cost = {"Mahesh":500, "Mithilesh":400}
logger.info(labour_with_cost)

# adding one of dictinary item to the existing dict
labour_with_cost["Jagmohan"] = 1000
logger.info(f"Updated Dict: {labour_with_cost}")

# Getting only keys using function
logger.info(f"Only keys: {labour_with_cost.keys()}")

# getting only values
logger.info(f"only values: {labour_with_cost.values()}")

# getting only items
logger.info(f"only items: {labour_with_cost.items()}")

# using For loop for dict iteration
for name in labour_with_cost:
    logger.info(f"{name, labour_with_cost[name]}")

for key, value in labour_with_cost.items():
    logger.info(f"{key} {value}")

# deleting the key
iphones = {"iphone16": 100000, "iphone17":110000}
logger.info(f"Mobile Phones: {iphones}")

del iphones["iphone16"]
logger.info(f"Updated mobile list: {iphones}")

# ---------------------------------------- FUNCTIONS in Dict ----------------------------------------# 
dict = {
    'id':101, 
    'name':'rohit',
    'course': 'IT'
}

# 1. Key function
logger.info(f"Finding Keys = {dict.keys()}")

# 2. Value function
logger.info(f"Finding Values = {dict.values()}")

# 3. Items
logger.info(f"Items = {dict.items()}")

# 4. get(key)
logger.info(f"Getting the values = {dict.get('id')}")

# 5.update 
Updated_values = dict.update({'id':111})
logger.info(dict)

# 6. pop()
logger.info(f"Popped items: {dict.pop("id")}")
logger.info(dict)

# 7. clear()
logger.info(f"Cleared items: {dict.clear()}")
logger.info(dict)

# 8. len
dict1 = {
    'id':101, 
    'name':'rohit',
    'course': 'IT'
}
logger.info(f"Length of dict = {(len(dict1))}")

# 9. existence of keys in Dict
logger.info(f"Exist = {'id' in dict1}") 

# 10. copy 
new_dict = dict1.copy()
logger.info(f"New copy: {new_dict}")

