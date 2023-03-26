def DisplayStaticInfo():
    heading=("""
               Sunway College Account Department
                    Maitidevi ,Kathmandu
                      Welcome to
              Salary & Tax Calculate System(STCS)""")
    print(heading)
    
DisplayStaticInfo()

#creating list
staff_data={}
#defining function for collection staf information
n = int(input("Enter the number of Staff: "))
def StaffInfo():
        staff_data = {} #dicti define
        # first for loop for different customers
        for i in range(n):
            staff_data[i] = {}  # nested dic. or multiple dic.
            # input for details
            staff_data[i]['name'] = input(f"Enter the name of Staff [{i+1}]: ")
            staff_data[i]['address'] = input(f"Enter the address of staff [{i+1}]: ")
            staff_data[i]['email'] = input(f"Enter the email of staff [{i+1}]: ")
            staff_data[i]['pan'] = input(f"Enter the pan of staff [{i+1}]: ")
            staff_data[i]['married_status'] = input(f"Enter the married status of staff [{i+1}]: ")
            staff_data[i]['FY'] = input(f"Enter the FY  of staff [{i+1}]: ")
            montly_income = int(input(f"Enter the monthly income of staff : "))
            staff_data[i]['Annual_income'] = montly_income*12
        return staff_data


#function to calculate tax
def Calculate_Tax_Of_Staff(staff_data):
        for i in range(len(staff_data)):
            Annual_income = staff_data[i]['Annual_income']
            tax=0
            if Annual_income<=400000:
                tax=tax+Annual_income*0.01
            elif Annual_income<=500000:
                tax=tax+(Annual_income-400000)*0.1
            elif Annual_income<=700000:
                tax=tax+400000*0.01+100000*0.1+(Annual_income-500000)*0.2
            elif Annual_income<=1300000:
                tax=tax+400000*0.01+100000*0.1+200000*0.2+(Annual_income-700000)*0.3
            else:
                tax=tax+400000*0.01+100000*0.1+200000*0.2+600000*0.3+(Annual_income-1300000)*0.36
            staff_data[i]['tax'] = tax
        return staff_data


staff_data=StaffInfo()
staff_data=Calculate_Tax_Of_Staff(staff_data)
print(staff_data)
def FinalDispalay(staff_dataname):
    for i in range(n):
        print (f''' 
        Customer name: {staff_data[i]['name']}                   Customer Address: {staff_data[i]['address']}
        Customer email: {staff_data[i]['email']}
        Customer pan: {staff_data[i]['pan']}
        Married Status:{staff_data[i]['married_status']}
        Annual Income: {staff_data[i]['Annual_income']}
        Payable Tax Amount: {staff_data[i]['tax']}              ''')
    
FinalDispalay(staff_data)
