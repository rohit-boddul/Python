from loguru import logger
import math

# LISTS

labours = ["Mahesh", "Mithilesh", "Sumesh"]
logger.info(f"Second person in the list is '{labours[1]}'")

# append method
labours.append("Ram")
logger.info(f"Fourth person in the list is '{labours[3]}'")

# EXTEND method
new_added_labours = ["Sitesh", "Ayush"]
labours.extend(new_added_labours)
logger.info(f"New added labours are {labours}")

# INSERT method
labours.insert(0, "Krishna")
logger.info(f"{labours}")
logger.info(f"Negative based indexing in lists {labours[-1]}")
# -------------------------------------------------------------------------------------


# MULTI-DIMENTIONAL LISTS
jobs = [["Amazon", "Pune"], ["Adobe", "Hyderabad"], ["TIAA", "Banglore"]]
logger.info(f"Company name present in Maharashtra is {jobs[0][0]} and the location is {jobs[0][1]}")


