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