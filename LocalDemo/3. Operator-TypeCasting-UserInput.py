from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour1 = "Jagmohan"
is_home = True 

#1. Calculate total area of the land? 
total_area_of_land = length_of_land * breadth_of_land
logger.info(f"Total area of the land is {total_area_of_land} sq.ft.")