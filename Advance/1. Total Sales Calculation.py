def calculate_sales(sales):
    employees = len(sales)
    months = len(sales[0])
    

    employee_sales = [0] * employees
    for i in range(employees):
        for j in range(months):
            employee_sales[i] += sales[i][j]
    
    month_sales = [0] * months
    for j in range(months):
        for i in range(employees):
            month_sales[j] += sales[i][j]
    
    total_sales = 0
    for emp_total in employee_sales:
        total_sales += emp_total
    
    return employee_sales, month_sales, total_sales

sales_data = [
    [100, 200, 150],
    [80, 120, 130],
    [90, 160, 110]
]
emp_sales, month_sales, total_sales = calculate_sales(sales_data)
print("Employee Sales:", emp_sales)
print("Monthly Sales:", month_sales)
print("Total Sales of Organization:", total_sales)
