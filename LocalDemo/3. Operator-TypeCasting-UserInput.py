from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour1 = "Jagmohan"
is_home = True 

#1. Calculate total area of the land? 
total_area_of_land = length_of_land * breadth_of_land
logger.info(f"Total area of the land is {total_area_of_land} sq.ft.")

#2. Perimeter of land?
perimeter_of_land = 2 * (length_of_land + breadth_of_land)
logger.info(f"Perimeter of the land is {perimeter_of_land}m")

#3. Modulo Operator (gives remainder - ARMSTRONG Number Code)
logger.info (15%6)

#4. Division (gives division values in FLOAT - even if it a whole number)
logger.info(15/6)

#5. Floor Division (gives Quotient)
logger.info(15//6)

#6. Ceiling values 
logger.info(math.ceil(15/6)) 
# -----------------------------------------------------------------------------------------------------------


# TYPE CONVERSION

a = "25"
b = 25
logger.info(float(a)+b)

# Types of TYPE CASTING
# i. explicit - developer gives it explicitly 
# ii. implict - python itself does it by its own

# ----------------------------------------------------------------------------------------------------------

# USER INPUT --> 



#1. area of the circle
# logger.info("To calculate the Area of circle, please provide below values -")
# radius_of_circle = float(input("Radius of the circle - "))
# logger.info(type(radius_of_circle))
# area_of_circle = 3.14159 * float (radius_of_circle) * float (radius_of_circle)
# logger.info(f"Area of cirle = {area_of_circle} units sq.")

# 2. Volume of cuboid
# length = int(input("Enter length:"))
# width = float(input("Enter Width:"))
# height = int(input("Enter Height:"))

# vol_of_cuboid = length * width * height
# logger.info(f"Volume of cuboid = {vol_of_cuboid} m.")


# 3. Addition of two numbers using split() function
val1, val2 = input("Enter two values to add: ").split()
val1 = int(val1)
val2 = int(val2)

logger.info(int(val1))
logger.info(int(val2))

addition_of_two_num = val1 + val2 
logger.info(f"Addition of two number = {addition_of_two_num}")







