from loguru import logger

# What is JOIN method?
# when you .JOIN() method - make sure you are doing with the string 



list_number = ['rohit', '45', 'boddul']
result = '~'.join(list_number)
logger.info(result)

# in case of DICT - it only takes the KEYS not values. 
dict_example = {'rohit':45, 'boddul':45} 
dict_result = "#".join(dict_example)
logger.info(dict_result)

# ------------------------------------------------ REAL LIFE EXAMPLE -----------------------------------------
# Find out all the employee name who are available in the above condition.
# You don't know the exact number of filter condition
# which will come in the above list. It can change in each run.

query = """select * from(
select e. employee name, e. state, e.zip, e.salary, d.department
from employee_tbl e
inner join department d
ON e. emp_id = d. emp_id
where salary>100000"""

# EXPECTED_OUTPUT = 
"""select * from(
select e. employee name, e. state, e.zip, e.salary, d.department
from employee_tbl e
inner join department d
ON e. emp_id = d. emp_id
where salary>100000 AND state = 'Bihar' OR department = 'IT' OR state = 'Delhi' OR department = 'Marketing'"""


state = [{'state':'Bihar', 'department':'IT'}, {'state':'Delhi', 'department':'Marketing'}]
# logger.info(f"Type of State is - {type(state)}")

result = []
for condition in state:
    for key, value in condition.items():
        result.append(f"{key} = {value}")
logger.info(result)

filter_condition = " OR ".join(result)
# logger.info(filter_condition)

final_result = query + " AND " + filter_condition 
logger.info(f"The final query becomes: {final_result};")

# ---------------------------------------- QUESTIONS -----------------------------------------------

# Q1. Swap the case of the string without using swapcase 
# inbuilt method for string

# Input:- Programming Aasan Hai
# Output:- pROGRAMMING aASAN hAI 


s = "Programming Aasan Hai"
result = s.swapcase()
print(result)


# Q2. Print the list of all unique ip addresses?

data = [
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
    "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
    "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
]

# Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
#            "10.168.155.22","10.168.167.2",
#            "10.168.179.28","10.168.155.31" ]


final_list_of_ip = []
for rohit in data:
    without_slash = rohit.split("server/")
    print(without_slash)
    last_item = without_slash[-1]
    final_list_of_ip.append(last_item)
logger.info(final_list_of_ip)







# ---------------------------------------- PRACTICE QUE 3 -------------------------------------#

inputemail = ['mverma645@gmail.com', 'ramesh345@gmail.com', 'sohansingh@gmail.com', 'swatirahatane@gmail.com']

# EXPECTED OUTPUT - 
# ['m*******5@gmail.com', 'r*******5@gmail.com', 's********h@gmail.com', 's***********e@gmail.com']

output_lst = []

for i in inputemail:
    parts = i.split("@")
    user_name = parts[0]
    masked_user_name = user_name[0] + "*"*(len(user_name) - 2) + user_name[-1]
    masked_email = masked_user_name + "@" + parts[1]
    output_lst.append(masked_email)

logger.info(output_lst)
