from loguru import logger

lst=[202,165,89,76,12]
num_to_insert=18

index=0

for number in lst:
    if number<num_to_insert:
        index=index
        break
    else:
        index=index+1
logger.info(f"{index}")

lst.append(None)

for i in range(len(lst)-1,index,-1):
    lst[i]=lst[i-1]
    lst[index]=num_to_insert
logger.info(f"{lst}")