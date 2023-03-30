# Income-Tax-Calculation

## Salary and Tax Calculate System (STCS)
This is a Python program that allows you to calculate the salary and tax of the staff at Sunway College Account Department. The program takes inputs from the user and calculates the tax for each staff member based on their annual income.

## Instructions for use
1. Run the program in a Python environment such as IDLE, Jupyter notebook or the terminal.
2. The program will display a welcome message with the name and location of the department.
3. Enter the number of staff members for whom you want to calculate the salary and tax.
4. or each staff member, enter their details such as name, address, email, PAN, marital status and financial year.
5. After entering the details for all staff members, the program will calculate their annual income and tax amount based on the tax bracket they fall under.
6. The program will display the details of all staff members including their name, address, email, PAN, marital status, annual income and payable tax amount.

## Program functions
DisplayStaticInfo(): This function displays a welcome message with the name and location of the department.

### StaffInfo(): 
This function allows the user to input the details of staff members such as name, address, email, PAN, marital status and financial year. It returns a dictionary containing the staff data.

### Calculate_Tax_Of_Staff(staff_data): 
This function takes the staff data as input and calculates the tax amount for each staff member based on their annual income. It returns a dictionary containing the staff data with added tax information.

### FinalDispalay(staff_data): 
This function takes the staff data as input and displays the details of each staff member including their name, address, email, PAN, marital status, annual income and payable tax amount.
