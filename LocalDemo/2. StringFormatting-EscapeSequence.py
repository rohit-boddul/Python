length_of_land = 100
bricks_cost_per_piece = 10.5
labour1 = "Jagmohan"
is_home = True 

# print (length_of_land, bricks_cost_per_piece, labour1, is_home)
# print (type(length_of_land), type(bricks_cost_per_piece), type(labour1), type(is_home))

print ("Length of the land is", length_of_land)
print ("Labour name is",labour1)

# \n -- this is for escaping lines (Escape Sequence)
print ("My home is of 4BHK, \nLength of the total land is", length_of_land)
print ("My home is of \"4BHK\"")
print ("My home is of \t \"4BHK\"")
# ----------------------------------------------------------------------------------------------------------

#String Formatting
# 1. F-string 
print(f"Length of the land is {length_of_land} sq.ft.")
print(f"First labour name is '{labour1}'")

# 2. .format method
print("Length of the land is {}".format(length_of_land))



# ----------------------------------------------------------------------------------------------------------

# Logging
from loguru import logger
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - Line:%(lineno)d - %(message)s",)

logging.info(f"Hello")
logger.info(f"Hello")





