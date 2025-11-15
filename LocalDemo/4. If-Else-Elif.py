from loguru import logger
import math


# If-else-elif

length_of_land = float(input("Enter your land length in ft: "))
breadth_of_land = float(input("Enter your land breadth in ft: "))

logger.info (f"Confirm your details once, ")
logger.info (f"Entered Length is {length_of_land} ft.")
logger.info (f"Entered Breadth is {breadth_of_land} ft.")

area_of_land = length_of_land * breadth_of_land
logger.info(f"Your area of the land comes to {area_of_land} sq.ft.")

if area_of_land <=500:
    logger.info(f"So, You can only build 1 BHK with area - {area_of_land} sq.ft.")
elif area_of_land >500 and area_of_land <=1000:
    logger.info(f"So, You are eligible for 2BHK with area - {area_of_land} sq.ft.")
else:
    logger.info(f"So, You can have a choice to build more than 1/2BHK with area {area_of_land} sq.ft.")


                       