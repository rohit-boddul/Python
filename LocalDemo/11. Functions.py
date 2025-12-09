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




def cost_landing (land_length,land_breadth,home_length,home_breadth,garden_length,garden_breadth,psqftcost):
    land_area = land_length * land_breadth
    home_area = home_length * home_breadth
    garden_area = garden_length * garden_breadth
    cost_of_shaded_area = (land_area - home_area - garden_area) * psqftcost
    return cost_of_shaded_area

result = cost_landing(100,100,80,60,100,20,10)
print(result)






