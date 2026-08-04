# Shopping Cart Management System
from dataclasses import dataclass
from week1_day1_grade_calc import get_int_input

def after_total(func):
    def wrapper(*args):
        print("\nGrand Total is calculating...")
        res = func(*args)
        print("...Thank You for shopping , Visit Again !!!")
        return res
    return wrapper


<<<<<<< HEAD:Test1_SCM_system.py
def get_int(prompt, error_message):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

=======
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372:Week-1/Test1_SCM_system.py
@dataclass
class Customer:
    customer_id : int
    customer_name : str 

    def customer_details(self):
        return self.customer_id , self.customer_name 

# Composite Class 1 
class ProductDetail:
    def __init__(self,n : int):
        self.n = n

    def item_details(self):
        item_dict = {}
        i=0
        for i in range(self.n):
            item_name = input(f"\nName of Item no. {i+1} : ")
            while True:
<<<<<<< HEAD:Test1_SCM_system.py
                item_price = get_int("Price of the Item  : ", "Please enter a whole number for the item price.")
=======
                item_price = get_int_input("Price of the Item  : ", "Please enter a whole number for the item price.")
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372:Week-1/Test1_SCM_system.py
                if item_price > 0:
                    item_dict[item_name] = item_price
                    break   
                else:
                    print(" !!! Invalid Input !!! ")
        return item_dict

# Composite Class 2 
class Calculations:
    def __init__(self, gst, n):
        self.gst = gst
        self.n = n
        self.prod = ProductDetail(self.n)  

    def calc_total (self):
        products = self.prod.item_details()
        total = sum(products.values())
        gst_temp = self.gst / 100
        gst_temp *=total
        gst_total = total
        gst_total += gst_temp
        return total, gst_total , products

class Discount:
    def __init__(self,gst_total):
        self.gst_total = gst_total
   
    def calc_discount(self,discount):
        self.discount = discount
        disc_temp = discount / 100
        disc_temp *= self.gst_total
        disc_total = self.gst_total - disc_temp
        return disc_total

class Bill:
    def __init__(self): 
        pass

    @after_total
    def bill_func(self,customer_name , customer_id , item_dict , n , total ,gst ,  gst_total , discount , disc_total):
        print(f"""
    Id of the Customer : {customer_id} \n
    Name of the Customer : {customer_name} \n
    List of the items : {item_dict} \n
    Total number of items : {n} \n
    Total = {total} \n
    GST rate = {gst}% \n
    Total with GST = {gst_total} \n
    Discount percent = {discount}% \n
    That makes your Payable Amount = {disc_total}
        """)

# Customer Class instance 
cust_obj = Customer(123 , "Madhav")
customer_id , customer_name = cust_obj.customer_details()

print("""
....Welcome to SCM (Shopping Cart Management) System (CLI MODE)....

=> ...Fill the below fields to generate the BILL... <=
""")

<<<<<<< HEAD:Test1_SCM_system.py
n = get_int("Enter the number of items : ", "Please enter a whole number for the number of items.")

if n > 0:
    gst = get_int("Enter the rate of gst (withuot '%' sign) : ", "Please enter a whole number for GST.")
    # Calculation class instance 
=======
n = get_int_input("Enter the number of items : ", "Please enter a whole number for the number of items.")

if n > 0:
    gst = get_int_input("Enter the rate of gst (withuot '%' sign) : ", "Please enter a whole number for GST.")
 
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372:Week-1/Test1_SCM_system.py
    cal_obj = Calculations(gst, n)
    total , gst_total , item_dict = cal_obj.calc_total()
    
    
    while True:
<<<<<<< HEAD:Test1_SCM_system.py
        discount = get_int("""
=======
        discount = get_int_input("""
>>>>>>> a69d5510c615d93ff77b54d140c83e3f3f4a5372:Week-1/Test1_SCM_system.py
=> Before Generating bill , 

If you wish then enter the rate of discount you want to give to the customer (withuot '%' sign) 
    or else write 0 : """, "Please enter a whole number for discount.")
        if 0 <= discount <= 100:

            d_total = Discount(gst_total)
            disc_total = d_total.calc_discount(discount)

            bill_obj = Bill()
            bill = bill_obj.bill_func(customer_name , customer_id , item_dict , n , total , gst , gst_total , discount , disc_total)

            break

        else:
            print("!!Invalid input!! , Discount can't be less than 0 or more than 100..")
   
else:
    print("!!Invalid Input!!, Bill should contains atleast one item...")