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

# Copy Method
copied_labour_list = updated_labour_list.copy()
logger.info(f"{copied_labour_list}")

# Clear
copied_labour_list.clear()
logger.info(f"{copied_labour_list}")

# --------------------------------------- Dictionary Comprehension ---------------------------------------#
logger.info(f"{labour_w_cost}")

increased_amt = 100
new_wages = {}

for key, value in labour_w_cost.items():
    new_wages[key] = increased_amt + labour_w_cost.get(key,0)
logger.info(f"After salary increment - {new_wages}")

# Using Dict Comprehension
increased_amt = 100
new_dict = {key: value + increased_amt for key, value in labour_w_cost.items()}
print(new_dict)






# don't increase Jagmohan salary
new_list = {'Mahesh': 2100, 'Ramesh': 500, 'Mithilesh': 500, 'Sumesh': 400, 'Jagmohan': 1100}


increased_amt = 100
skip_name = "Jagmohan"
new_wages = {}

for key, value in new_list.items():
    if key == skip_name:
        new_wages[key] = value
    else:
        new_wages[key] = increased_amt + new_list.get(key, 0)
logger.info(f"After salary increment - {new_wages}")

# ------------------------------------ In Method in Dict ----------------------------------#

name = "Rohit Boddul"
# 1. How many times each alphabet comes in this NAME 

letter_count = {}

for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)



# Find how many 'FieldTypeName' present?
data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"5678hfjhjh","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"148877564"},{"FieldTypeName":"H3","Value":"20230930"},{"FieldTypeName":"H4","Value":"20231130"},{"FieldTypeName":"H5","Value":"2441.56"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"2411.56"},{"FieldTypeName":"H8","Value":"EUR"},{"FieldTypeName":"H9","Value":"00115190035"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"4500575382"},{"FieldTypeName":"H12","Value":"0.00"},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":""},{"FieldTypeName":"H15","Value":"F0"},{"FieldTypeName":"H16","Value":"87"},{"FieldTypeName":"H17","Value":"0.00"},{"FieldTypeName":"H18","Value":""},{"FieldTypeName":"H19","Value":""},{"FieldTypeName":"H20","Value":"No"}],"CodingLines":[],"Tables":[{"N1":"233553","N2":"3555","N3":"ASDDDD","N4":"334324","N5":"900.00","N6":"1.29","N7":"387.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"765765","N2":"67657657","N3":"ADFDFF)","N4":"667657","N5":"1000.00","N6":"1.94","N7":"1940.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"67657","N2":"76576576576","N3":"SFDFFDFSDF","N4":"7667676","N5":"1000.00","N6":"0.11456","N7":"114.56","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""}],"INININ":"148877564","SDRER":"null"},{"IDD":"frret5","BDD":"5trtry4566","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"ICI2300397"},{"FieldTypeName":"H3","Value":"20231219"},{"FieldTypeName":"H4","Value":"20240331"},{"FieldTypeName":"H5","Value":"76.44"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"76.44"},{"FieldTypeName":"H8","Value":"INR"},{"FieldTypeName":"H9","Value":"56676765"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"0.00"},{"FieldTypeName":"H12","Value":""},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":"F1"},{"FieldTypeName":"H15","Value":"87"},{"FieldTypeName":"H16","Value":"0.00"},{"FieldTypeName":"H17","Value":""},{"FieldTypeName":"H18","Value":""}],"CodingLines":[{"CODE1":0.0,"CODE2":76.44,"CODE3":"5645654","CODE4":"","CodingFields":[{"FieldName":"COL1","Value":"223DD666"},{"FieldName":"COL2","Value":"3454545"},{"FieldName":"COL3","Value":""},{"FieldName":"COL5","Value":""},{"FieldName":"COL5","Value":""}]}],"Tables":[],"INININ":"DER3434","SDRER":"null"}],"Final":"JKHJKLH0909908"}


count = 0

for rohit in data["MAINDATA"]:
    for rachana in rohit.get("HeaderFields", []):
        if "FieldTypeName" in rachana:
            count += 1

print("Total FieldTypeName count =", count)










