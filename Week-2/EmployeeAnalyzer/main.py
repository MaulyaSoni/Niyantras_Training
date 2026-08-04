from reader import load_employees

from api import predict_nationality

def main():
    print(" .............EMPLOYEE ANALYSING SYSTEM ...........")

    load_employees("tech_company_employee_data_1000.csv")

    emp_name = input("Enter employee name to guess it's nationality: ")
    result = predict_nationality(emp_name)

    if "error" in result:
        print(result["error"])
    else:

        print(f"Employee Name : {result['name']}")
        print(f"Predictions   : {result['count']}")
        print("\nPossible Nationalities:\n")

        for country in result["countries"][:3]:
            print(
                f"{country['country_name']} "
                f"({country['country_code']}) "
                f"{country['probability']}%"
            )
    

if __name__ == "__main__":
    main()