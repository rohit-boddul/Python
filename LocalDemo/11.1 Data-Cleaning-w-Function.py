from loguru import logger

# simple data cleaning approach in dataset 
empname = "   rohit  "
empbasic = 10000
empbonus = 1500
empdept = ""

def validdata (name):
    return name.strip().title()

def total_salary(sal, bonus):
    return sal + bonus

def defaultvalue (dept):
    if dept.strip() == "":
        return "Not Applicable"
    return dept.title() 

empname = "   rohit  "
empbasic = 10000
empbonus = 1500
empdept = ""

name = validdata(empname)
salary = total_salary(empbasic, empbonus)
dept = defaultvalue(empdept)

logger.info(f"Updated Name from '{empname}' to {name}")
logger.info(f"Updated Salary = {salary}")
logger.info(f"Updated Dept from '{empdept}' to {dept}")
# ------------------------------------------------------------------------------------------------------------ #

emp = {
    "name":"   kamran   ",
    "basesalary":25000,
    "DA":7500,
    "city":""
}

def namechange(names):
    return names.strip().title()

def fullsalary(da, base):
    return da + base

def cleandept(depts):
    if depts.strip() == "":
        return "Not Filled"
    return depts.title()

emp = {
    "name":"   kamran   ",
    "basesalary":25000,
    "DA":7500,
    "city":""
}

emp["name"] = namechange(emp["name"])
emp["salary"] = fullsalary(emp["basesalary"], emp["DA"])
emp["city"] = cleandept(emp["city"])

logger.info(f"Employee name is '{emp["name"]}'")
logger.info(f"'{emp["name"]}' total salary is {emp["salary"]}/-")
logger.info(f"'{emp["name"]}' city is '{emp["city"]}'")

# ----------------------------------------------------------------------------------------------------------- #
studentname = "   yOGesh  kumAR"
marks1 =25 
marks2 = 65 
marks3 = 23 
marks4 = 45 
marks5 = 87 
city = "deLHi  "
email = "yoGESH    @G    mail.com"



def studentnamecleanup(stname):
    return " ".join(stname.split()).strip().title()
cleaned_name = studentnamecleanup(studentname)

def total_marks_of_students (m1, m2, m3, m4, m5):
    total_marks = m1 + m2 + m3 + m4 + m5
    return total_marks
total = total_marks_of_students(25, 65, 23, 45, 87)

total_subjects = 5

def percentage(total_subjects, total_marks):
    percentage = ((total_marks/total_subjects))
    return percentage
perc = percentage(total_subjects,total)

def cleancity(cityname):
    return cityname.strip().title()
cleaned_city = cleancity(city)

def cleanemail(emailid):
    return "".join(emailid.split()).strip().lower()
cleaned_email = cleanemail(email)

logger.info(f"After cleaning student name = '{cleaned_name}'")
logger.info(f"'{cleaned_name}' has gotten total = {total} marks and his/her percentage has come to = '{perc}%'")
logger.info(f"After cleaning city name = '{cleaned_city}'")
logger.info(f"After cleaning email = '{cleaned_email}'")


















