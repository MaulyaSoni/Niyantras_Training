from reader import load_employees
# from analysis import analyze_data
# from api_service import get_motivational_quote
# from report import display_report

def main():
    print(" .............EMPLOYEE ANALYSING SYSTEM ...........")

    employee_list = load_employees(
        "tech_company_employee_data_1000.csv"
    )

    emp_name = input("Enter employee name to guess it's age: ")
    result = predict_emp_age(emp_name)

    if "error" in result:
        print(result["error"])
    else:
        print("\nPredicted Information")
        print(f"Name           : {result['name']}")
        print(f"Predicted Age  : {result['age']}")
        print(f"Predictions    : {result['count']}")
    # # Analyze dataset
    # analysis_result = analyze_data(employees)

    # # Call API
    # quote = get_motivational_quote()

    # # Display final report
    # display_report(
    #     analysis_result,
    #     quote,
    # )


if __name__ == "__main__":
    main()