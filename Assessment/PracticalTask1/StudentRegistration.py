# StudentRegistration.py
# This program processes student details to register them into courses and then displays this information onto the screen.  
# Author: Yanan Wu
# Date: 12/11/2022

from tkinter.simpledialog import askfloat, askstring

# method to print headings in the console
def printHeadings():
    print('---HOLMESGLEN INSTITUTE---')
    print('ID\tNAME\t\tCOURSE\t\tFEE\n\n')


# method to get student details
def inputStudentDetails():
    studentId = askstring('Student Details', 'Input student id: ')
    if studentId == '' or studentId is None:
        return
    studentName = askstring('Student Details', 'Input student name: ')
    if studentName == '' or studentId is None:
        return 
    course = askstring('Student Details', 'Input course name: ')  
    if course == '' or studentId is None:
        return 
    fee = askfloat('Student Details', 'Input course fee: ')
    if fee == '' or studentId is None:
        return

    print(f'{studentId}\t{studentName}\t\t{course}\t\t${fee:,.2f}')
    return fee

# method to print total fee
def outputTotalFee(totalFees):
    print(f'\n\nTotal fee: ${totalFees:,.2f}')

if __name__ == '__main__':
    printHeadings()

    totalFees = float(0)
    while True:
        result = inputStudentDetails()
        if result:
            totalFees = totalFees + result
        else:
            break
    outputTotalFee(totalFees)
