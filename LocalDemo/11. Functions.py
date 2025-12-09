from loguru import logger

# circumference of land 

length_of_land = 100 
breadth_of_land = 50
per_ft_fence_cost = 17

circumference = 2 * (length_of_land + breadth_of_land)
print(circumference)



# calculate fencing cost of that circumference, and take fencing cost per ft is 17 rupees
def calculate_fencing_cost (length, width, cost_per_ft):
    circumference = 2 * (length + width)
    cost_for_fencing = circumference * cost_per_ft
    return cost_for_fencing

cost = calculate_fencing_cost(length_of_land, breadth_of_land, per_ft_fence_cost)
logger.info(f"Total fencing cost will come to {cost}/-")


# calculate the how much grass will be needed sorrounding for the home, grass is 10/- per sq. ft.

# total_land_dim = 100 ft. * 100 ft. 
# total_home_dim = 80 ft. * 60 ft.

total_sides = 4

def total_grass (length, cost_per_grass):
    total_grass_for_one_side = length * cost_per_grass
    total_cost_for_all_sides = total_grass_for_one_side * total_sides
    return total_cost_for_all_sides

cost = total_grass(10, 0.5)
logger.info(f"Cost needed for grass is {cost} per ft.")
# -------------------------------------------------------------------------------------------------------------

# FUNCTION

# 1. self contained block, contains line of code and whenever we use same line of code, 
# we simply use the name of function

# ROLE of Function in DATA?
# 1. data cleaning
# 2. transforming and aggregating data


def show():
    logger.info("Hello!")
show()

# ------------------------------------------ Calculator Using Function ----------------------------------- #

def calculator (var1, var2):
    logger.info(f"Addition - {var1 + var2}")
    logger.info(f"Subtraction - {var1 - var2}")

calculator(10, 5)

# WOP in python for function contains the calculator code having all operations, values need to be taken during 
# run time

def calc (value1, value2):
    logger.info(f"Addition = {value1 + value2}")
    logger.info(f"Subtraction = {value1 - value2}")
    logger.info(f"Multiplication = {value1 * value2}")
    logger.info(f"Division = {value1 / value2}")

# a = float(input("Enter value1 = "))
# b = float(input("Enter value2 = "))

# result = calc(a, b)
# ------------------------------------------------------------------------------------------------------- #

# RETURN statement - 

# WHY do we need to return the values from function?
# -->
# 1. it is exit status 
# 2. kind of signal of function to OS that function is working fine
# 3. with NO RETURN - return keyword 0, with RETURN - 1 


def multiplication(v1, v2):
    return v1 * v2

result = multiplication (10, 5)
logger.info(result)


# Calculate two functions, 1 for volume of cuboid and 2nd for vol of cyl 

def vol_cub (l, b, h):
    return l * b * h

vol_of_cuboid = vol_cub (10, 5, 8)

def vol_cyl (pi, r, h):
    return pi * r * r * h

vol_of_cyl = vol_cyl(3.14, 5, 7)
logger.info(f"Volume of Cuboid = {vol_of_cuboid} and Volume of Cyl = {vol_of_cyl}")
# ------------------------------------------------------------------------------------------------------- #
# DEFAULT argument into function - 
# when you want to fix the argument

def show1(name = 'RAJ'):
    print(name)
show()
# show('ROHIT')  -- this is default arugument
# ------------------------------------------------------------------------------------------------------- #


# RECURSIVE Function
# when a function call itself that process is known as recursion and this type of function are known as recursive functionl






































