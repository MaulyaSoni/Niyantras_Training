import sys
import csv
from reader import load_data

def high_and_low(file_name):

    with open(file_name,"r") as file:
        reader = csv.reader(file)
        next(reader)
        t_max = 0
        res = sys.maxsize    
        for row in reader:
            transact_id = row[0]
            cust_id = row[2]
            amt = int(row[8])
         
            t_max = max(t_max ,amt)    
            res = res if res < amt else amt

        return t_max , res