from loguru import logger

labour_w_cost = {
    "Mahesh":500,
    "Ramesh":400,
    "Mithilesh":400,
    "Sumesh":300,
    "Jagmohan":1000,
    "Rampyare":800
}

# get method 
logger.info(f"{labour_w_cost.get("Mahesh")}")

# keys and values
logger.info(f"{labour_w_cost.items()}")

# Update method
labour_w_cost.update({"Mahesh":2000})
logger.info(f"{labour_w_cost}")

# POP
labour_w_cost.pop("Rampyare")
logger.info(f"{labour_w_cost}")

# adding again new dict and merging them to old
new_labour = {'Rampyare':800}
updated_labour_list = labour_w_cost | new_labour
logger.info(updated_labour_list)