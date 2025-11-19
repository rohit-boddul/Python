from loguru import logger

dict = {"order_id":"AMZ-2025-00123","order_date":"2025-02-15","customer":{"customer_id":"CUST-9087","name":"Rohit B","email":"rohit.b@example.com"},"shipping_address":{"street":"201, Green Valley","city":"Pune","state":"MH","pincode":"411045"},"items":[{"item_id":"ITEM-1001","product_name":"Wireless Mouse","quantity":1,"price":499.00,"category":["electronics","accessories"]},{"item_id":"ITEM-1002","product_name":"USB-C Cable Pack","quantity":2,"price":299.00,"category":["electronics","mobile"]}],"payment":{"mode":"UPI","transaction_id":"TXN-884422","status":"SUCCESS","total_amount":1097.00},"delivery":{"status":"Out for Delivery","expected_date":"2025-02-18","tracking":{"courier":"Amazon Logistics","tracking_id":"AMZ-TRK-445522","events":[{"date":"2025-02-16","location":"Warehouse","status":"Packed"},{"date":"2025-02-17","location":"Pune Hub","status":"Dispatched"}]}}}

# logger.info(f"Received order id: {dict["order_id"]}")
# logger.info(f"Name of the customer: {dict["customer"]["name"]}")
# logger.info(f"Items are: {dict["items"]}")

for r in range(len(dict['items'])):
    logger.info(f"Item ID for the customer 'Rohit' is - {dict['items'][r]['item_id']}")



