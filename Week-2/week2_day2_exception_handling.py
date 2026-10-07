import csv      
import sys
import logging

class AgeException(Exception):
    """Age can't be in negative or have the value Zero"""
    pass

class OSException(Exception):
    """Incompatible platform."""
    pass
 
# is_linux function for OSException 
def is_linux():
    #
    if "linux" not in sys.platform:
        raise OSException("This code can only run on Linux systems.")
    print("Doing the exception handling in the linux system")

logging.basicConfig(
    filename='processing_file.log', 
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    is_linux ()

    with open('csv2.csv','r',newline='') as file:
        reader = list(csv.reader(file))
        for row in reader[:10]:
            
            try:
                if len(row) < 3:
                    raise IndexError("Row does'nt contain age column")
                age = int(row[2])  
              
                if age <= 0:
                    raise AgeException(f"Age : {age} can't be negative or Zero") 
                                 
            except (ValueError , AgeException ,IndexError) as e :
                print(f"Bad row detected {e}")
                logging.error(f"Failed to process row: {row} | Error: {e}")
                

except (OSException,Exception) as error:
    print(error)

else:
    print("No errors or Exceptions are found !....(Executing the else block)....")

finally:
    print("Executing the final block")

