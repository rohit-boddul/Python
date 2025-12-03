from loguru import logger

# PROBLEM STATEMENT - 
# Total labour cost if total days was 50, out of which Mahesh was absent for 3 days and Jagmohan was absent for 7 days, 
# find out the total labour cost

labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300, "Jagmohan":1000, "Rampyare":800}

total_working = 50
Mahesh_absent_days = 3 * labour_with_cost["Mahesh"]
Jagmohan_absent_days = 7 * labour_with_cost["Jagmohan"]
total_labour_cost = 0

for name in labour_with_cost:
    if name == "Mahesh":
        # logger.info(f"'Mahesh' earned in 47 days = {(labour_with_cost[name] * total_working) - Mahesh_absent_days}/-")
        total_labour_cost = (labour_with_cost[name] * total_working) - Mahesh_absent_days
    elif name == "Ramesh":
        # logger.info(f"'Ramesh' earned in 50 days = {labour_with_cost[name] *  total_working}/-")
        total_labour_cost = total_labour_cost + (labour_with_cost[name] *  total_working)
    elif name == "Mithilesh":
        # logger.info(f"'Mithilesh' earned in 50 days = {labour_with_cost[name] *  total_working}/-")
        total_labour_cost = total_labour_cost + (labour_with_cost[name] *  total_working)
    elif name == "Sumesh":
        # logger.info(f"'Sumesh' earned in 50 days = {labour_with_cost[name] *  total_working}/-")
        total_labour_cost = total_labour_cost + (labour_with_cost[name] *  total_working)
    elif name == "Jagmohan":
        # logger.info(f"'Jagmohan' earned in 43 days = {(labour_with_cost[name] * total_working) - Jagmohan_absent_days}/-")
        total_labour_cost = total_labour_cost + ((labour_with_cost[name] * total_working) - Jagmohan_absent_days)
    elif name == "Rampyare":
        # logger.info(f"'Sumesh' earned in 50 days = {labour_with_cost[name] *  total_working}/-")
        total_labour_cost = total_labour_cost + (labour_with_cost[name] *  total_working)
logger.info(f"Total Labour Cost for 50 days = {total_labour_cost}/-")




total_days = 50

absent_days = {
    "Mahesh": 3,
    "Jagmohan": 7
}

total_cost = 0

for name, daily_cost in labour_with_cost.items():
    days_worked = total_days - absent_days.get(name, 0)
    total_cost += days_worked * daily_cost

print("Total Labour Cost:", total_cost)