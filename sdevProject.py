import pandas

def dataEntry(checks): 
    
    person = employee()
    inputValid = validationModule(person, checks)
    checks.append(inputValid)
    
    if(inputValid):
        #save employee data
        person.dependents = int(person.dependents)
        person.employeeID = int(person.employeeID)
        #print("Employee data input successfully.\n")
        return person, 1
    else:
        print("Invalid input. Please re-enter employee information.\n")
        return person, 0

class employee:
    def __init__(self):
        first = input("Enter employee first name: ")
        last = input("Enter employee last name: ")
        ID = input("Enter employee ID: ")
        dep = input("Enter number of dependents: ")
        hours = input("Enter number of hours worked: ")
        
        self.firstName = first
        self.lastName = last
        self.employeeID = ID
        self.dependents = dep
        self.hoursWorked = float(hours)
        self.hourlyRate = 0 #check if add later
        
def validationModule(employee, checks):
    valid = True
    
    if not employee.firstName:
        print("First name cannot be blank.")
        valid = False
    if not employee.lastName:
        print("Last name cannot be blank.")
        valid = False
    if not employee.employeeID.isnumeric():
        print("Employee ID must be a number.")
        valid = False
    if not employee.dependents.isnumeric():
        print("Dependents must be a number")
        valid = False
    if employee.hoursWorked < 0 or employee.hoursWorked > 80:
        print("Hours worked must be between 0 and 80.")
        valid = False
        
    return valid

def payRateLookup(eID, database, checks):
    
    payRateFound = False
    
    for record in database:
        if record == eID:
            hourlyRate = database[record]
            payRateFound = True
            break
    
    checks.append(payRateFound)
    
    if payRateFound:
        return hourlyRate
    else:
        print("Error: Invalid Employee ID.\n")
        return 0
    
def payCalculation(person):
    
    if person.hoursWorked > 40:
        overtime_hours = person.hoursWorked - 40
        gross_pay = (40 * person.hourlyRate) + (overtime_hours * person.hourlyRate * 1.5)
    else:
        gross_pay = person.hoursWorked * person.hourlyRate
        
    dependent_deduction = person.dependents * 25
    state_tax = gross_pay * 0.056
    federal_tax = gross_pay * 0.079
    total_deductions = state_tax + federal_tax + dependent_deduction
    net_pay = gross_pay - total_deductions
    
    #print("finish payCalculation")
    return gross_pay, total_deductions, net_pay

def addToArray(person, record, check, row, gross = 0, deductions = 0, net = 0):
    
    if gross:
        printOutput(person, gross, deductions, net)
    
    record.append(data(person, gross, deductions, net, check))
    #print("finish addToArray")
    return

def printOutput(person, gross, deductions, net):
    
    print(person.firstName, person.lastName, person.employeeID, person.dependents)
    print(person.hourlyRate, person.hoursWorked)
    print(gross, deductions, net)

    return

def data(person, gross, deductions, net, checks):
    
    out = [person.firstName, person.lastName, person.employeeID, person.dependents, person.hoursWorked]
    out.append(checks[0])
    if len(checks)> 1:
        out.append(person.hourlyRate)
        out.append(checks[1])
    if gross:
        out.append(gross)
        out.append(deductions)
        out.append(net)
        
    return out

if __name__ == "__main__":
    payRate = {0:23, 1:7.25, 2:12.50, 3:15, 4:9.60, 5:19.40, 
               6:12.65, "0007":11.85, 8:16.60, 9:18, 10:15.35}
    file = r'C:\Users\slee\Desktop\result.xlsx'
    counter = 0
    record = []
    
    start = input("Is there an employee to create a report for? (y/n) ")
    while start.lower() == "y":
        check = []
        person, good = dataEntry(check)
        if (not good):
            addToArray(person, record, check, counter)
            counter += 1
            continue
        
        person.hourlyRate = payRateLookup(person.employeeID, payRate, check)
        if (not person.hourlyRate):
            addToArray(person, record, check, counter)
            counter += 1
            continue
        
        gross, deductions, net = payCalculation(person)
        addToArray(person, record, check, counter, gross, deductions, net)
        
        counter += 1
        start = input("Is there another employee to create a report for? (y/n) ")
    
    df = pandas.DataFrame(record, columns=["First Name", "Last Name", "Employee ID", "Dependents",
                                           "Hours Worked", "Input Valid Check", "Hourly Rate", "Valid ID Check"
                                           "Gross Pay", "Deductions", "Net Pay"]).T
    df.to_excel(excel_writer=file)
    print("End of program \n results saved at" + file)
    

