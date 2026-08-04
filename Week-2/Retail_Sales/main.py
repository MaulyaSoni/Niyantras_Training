import csv 
from reader import load_data
from file import high_and_low
def main():
    print(".......Welcome to the Retail Sales Data Analyzer......")

    list_d = load_data("retail_sales_dataset.csv")
    max_amt , min_amt = high_and_low("retail_sales_dataset.csv")
    print(max_amt , min_amt)

if __name__ == "__main__":
    main()  