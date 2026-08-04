import csv      
import sys
import logging

<<<<<<< HEAD
# two custom exception classes 
=======
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372
class AgeException(Exception):
    """Age can't be in negative or have the value Zero"""
    pass

class OSException(Exception):
    """Incompatible platform."""
    pass
 
<<<<<<< HEAD
# is_linux function for OSException 
def is_linux():
    #
=======
def is_linux():
    
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372
    if "linux" not in sys.platform:
        raise OSException("This code can only run on Linux systems.")
    print("Doing the exception handling in the linux system")

<<<<<<< HEAD
logging.basicConfig(filename='processing_file.log', level=logging.ERROR)
=======
logging.basicConfig(
    filename="processing_file_W2.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# def match_case(data):
#     age = data  
#     match data:
#         case data if age <= 0:
#             print("working")
#         case TypeError:
#             print("TypeError")
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372

try:
    is_linux ()

<<<<<<< HEAD
    with open('tech_company_employee_data_1000.csv','r',newline='') as file:
        reader = list(csv.reader(file))
        for row in reader[:10]:
            # if index > 10:
            #     break
            try:
                if len(row) < 3:
                    raise IndexError("Row does'nt contain age column")

                age = int(row[2])  
                # print(f"processed row : {row}")
=======
    with open('csv2.csv','r',newline='') as file:
        reader = list(csv.reader(file))
        for row in reader[:10]:
            
            try:
                if len(row) < 3:
                    raise IndexError("Row does'nt contain age column")
                age = int(row[2])  
              
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372
                if age <= 0:
                    raise AgeException(f"Age : {age} can't be negative or Zero") 
                                 
            except (ValueError , AgeException ,IndexError) as e :
                print(f"Bad row detected {e}")
                logging.error(f"Failed to process row: {row} | Error: {e}")
<<<<<<< HEAD
                #print(e)
=======
             
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372

except OSException as error:
    print(error)

else:
    print("No errors or Exceptions are found !....(Executing the else block)....")

finally:
<<<<<<< HEAD
    print("Executing the final block")

=======
    print("Executing the final block")
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372
