import csv
import logging
from collections import namedtuple
import sys

logging.basicConfig(
    filename="processing_file_RSD.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

RetailSalesData = namedtuple(
    "RetailSalesData",
    [
        "Transaction_ID",
        "Date",
        "Customer_ID",
        "Gender",
        "Age",
        "Product_Category",
        "Quantity",
        "Price_per_Unit",
        "Total_Amount",
    ],
)

class NullQuantityException(Exception):
    """Quantity of Product can't be Null """
    pass

class NullIDException(Exception):
    """Transaction ID or the Customer ID can't be null """
    pass

def validate_row(row):
    transact_id = row[0]
    cust_id = row[2]
    
    if transact_id is None or transact_id == "":
        raise NullIDException("...Transaction ID can't be null...") 
 
    if cust_id is None or cust_id == "":
        raise NullIDException("...Customer ID can't be null...") 
 
    quantity =  int(row[6])
    if quantity <= 0:
        raise NullQuantityException(f"Quantity can't be null or negative ,  value of quantity : {quantity}")

def load_data(file_name):
    data_list = []
    with open(file_name,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                validate_row(row)
                data_record = RetailSalesData._make(row)
                data_list.append(data_record)

            except(ValueError , NullIDException , NullQuantityException) as error:
                logging.error(f"Row : {row} | the error : {error}")


    return data_list