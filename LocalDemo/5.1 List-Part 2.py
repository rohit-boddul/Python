from loguru import logger 

#----------------------------- index slicing in lists -----------------------------#
labours = ["Ram", "Mitesh", "Sitesh", 200, 500, 300]

#1. start to end indexing 
logger.info(f"start to indexing: {labours[1:]}")

#2. start to specific value indexing 
logger.info(f"start to specific value indexing: {labours[1:3]}")

#3. reverse the string
logger.info(f"Reversed string: {labours[::-1]}")

#4. length method
logger.info(f"Elements present in the list is '{len(labours)}'")

#5. POP method using index
labours.append("Ayush")
logger.info(f"new updated list is {labours}")
value_to_be_deleted = labours.pop(-1)

logger.info(f"deleted value: {value_to_be_deleted}")

logger.info(f"{labours}")
labours.append(300)
logger.info(f"Duplicated list = {labours}")


deleted_value_by_remove_mtd = labours.remove(300)
logger.info(f"Newly list = {labours}")
# ---------------------------------------------------------

lord_names = ["Krishna", "Govinda", "Madhava", "Radha", "Radhama"]
logger.info(f"Lord names = {lord_names}") 

lord_names[-1] = "Radhamadhava"

corrected_lord_names = lord_names[-1]
logger.info(f"tweaked names = {lord_names}")
# -----------------------------------------------------------------------------
mobile = ["aple", "iphne", "samng", "jo"]
mobile[0:4] = ["apple", "iphone", "samsung", "jio"]
updated_mobile_list = mobile[0:4]

logger.info(f"Updated mobile list = {updated_mobile_list}")
logger.info(f"Removed the elements from the list = {updated_mobile_list.clear()}")

#----------------------------- Split Method -----------------------------#

api_endpoint = "https://github.com/manisnitt/myresume/blob/main/manish_resume_github.pdf"
new_updated_api = api_endpoint.split("/")

logger.info(f"Newly Updated List = {new_updated_api}")
logger.info(f"Last element from list = {new_updated_api[-1]}")

























