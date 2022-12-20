# PayrollReport02.py
# This program reads employee details from a csv file, then processes the payment details and generate the output to a csv file. 
# Author: Yanan Wu
# Date: 20/11/2022

from employee import Employee

# global variables
employeeId = ''
name = '' 
position = '' 
pay = ''
employees = []
totalPayroll = 0
managesrPay = 0
salesPay = 0
adminsPay = 0
numOfPayroll = 0
averagePay = 0

# read employee information from data file
def readEmployeeInfoFromDataFile(fileName): 
    with open(fileName) as data:
        lines = data.readlines()[1:]
    for line in lines:
        employeeId, name, position, pay = line.split(',')
        pay = float(pay)
        employee = Employee(employeeId, name, position, pay)
        employees.append(employee)

# print employee information as formatted
def printEmployeeInfo(employees):
    for employee in employees:
        print(f'{employee.employeeId} {employee.name} {employee.position} ${employee.pay:,.2f}')

# calculate total payroll, managers pay, sales pay, admins pay
def calculatePayroll():
    global totalPayroll, managesrPay, salesPay, adminsPay
    for employee in employees:
        totalPayroll += employee.pay
        if employee.position == 'Manager':
            managesrPay = managesrPay + employee.pay
        elif employee.position == 'Sales':
            salesPay = salesPay + employee.pay
        else:
            adminsPay = adminsPay + employee.pay

# print payroll information
def printPayrollInfo():
    numOfPayroll = len(employees)
    averagePay = totalPayroll / numOfPayroll
    print()
    print(f'Total payroll: ${totalPayroll:,.2f}')
    print(f'Number on payroll: {numOfPayroll}')
    print(f'Average pay: ${averagePay:,.2f}')
    print('\nTotal pay for:')
    print(f'Managers ${managesrPay:,.2f}')
    print(f'Sales ${salesPay:,.2f}')
    print(f'Admin ${adminsPay:,.2f}')

# method to generate a payroll report
def generatePayrollReport(fileName):
    with open(fileName, 'w') as out:
        out.write(f'Total payroll: ${totalPayroll:,.2f}\nNumber on payroll: {numOfPayroll}\nAverage pay: ${averagePay:,.2f}\n\nTotal pay for:\nManagers ${managesrPay:,.2f}\nSales ${salesPay:,.2f}\nAdmin ${adminsPay:,.2f}')

readEmployeeInfoFromDataFile('PracticalTask2/Employees.csv')
printEmployeeInfo(employees)
calculatePayroll()
printPayrollInfo()
generatePayrollReport('PracticalTask2/PayrollReport.csv')
