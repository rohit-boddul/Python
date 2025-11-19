from loguru import logger

empoldcol = {
    'id':101,
    'name':'rohit',
    'dept':'IT'
}
logger.info(f"Old Employee Data: {empoldcol}")

empnewcol = {
    'id':'empid',
    'name':'empname',
    'dept':'empdept'
}
logger.info(f"Employee New Columns to be mapped: {empnewcol}")

# Que1. Map the columns from old to new
new_emp_set = {
    empnewcol['id']:empoldcol['id'],
    empnewcol['name']:empoldcol['name'],
    empnewcol['dept']:empoldcol['dept']
}

logger.info(f"New Emp Data Set: {new_emp_set}")