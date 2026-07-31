# Shopping Cart Management System
from dataclasses import dataclass

#decorator 
def after_total(func):
    def wrapper(*args):
        print("\nGrand Total is calculating...")
        res = func(*args)
        print("...Thank You for shopping , Visit Again !!!")
        return res
    return wrapper

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
        for i in range(n):
            item_name = input(f"\nName of Item no. {i+1} : ")
            while True:
                item_price = int(input("Price of the Item  : "))
                if item_price > 0:
                    item_dict[item_name] = item_price
                    break   
                else:
                    print(" !!! Invalid Input !!! ")
            i+=1
        return item_dict

# Composite Class 2 
class Calculations:
    def __init__(self, gst):
        self.gst = gst
        self.prod = ProductDetail(n)  

    def calc_total (self):
        products = self.prod.item_details()
        total = sum(products.values())
        gst_temp = gst / 100
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
        disc_temp *= gst_total
        disc_total = gst_total - disc_temp
        return disc_total

class Bill:
    def __init__(self): 
        pass

    @after_total
    def bill_func(self,customer_name , customer_id , item_dict , n , total ,gst ,  gst_total , disc_total):
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
cust_obj = Customer("123" , "Madhav")
customer_id , customer_name = cust_obj.customer_details()

print("""
....Welcome to SCM (Shopping Cart Management) System (CLI MODE)....

=> ...Fill the below fields to generate the BILL... <=
""")

n = int(input("Enter the number of items : "))

if n > 0:
    gst = int(input("Enter the rate of gst (withuot '%' sign) : "))
    # Calculation class instance 
    cal_obj = Calculations(gst)
    total , gst_total , item_dict = cal_obj.calc_total()
    
    #discount value input 
    while True:
        discount = int(input("""
=> Before Generating bill , 

If you wish then enter the rate of discount you want to give to the customer (withuot '%' sign) 
or else write 0 : """))
        if 0 <= discount <= 100:

            #Discount class instance 
            d_total = Discount(gst_total)
            disc_total = d_total.calc_discount(discount)

            #Bill class instance 
            bill_obj = Bill()
            bill = bill_obj.bill_func(customer_name , customer_id , item_dict , n , total , gst , gst_total  , disc_total)

            break

        else:
            print("!!Invalid input!! , Discount can't be less than 0 or more than 100..")
   
else:
    print("!!Invalid Input!!, Bill should contains atleast one item...")