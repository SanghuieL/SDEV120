def dataEntry(): 
    person = employee()
    inputValid = validationModule(person)
    if(inputValid):
        #save employee data
        print("Employee data input successfully.")
        return person
    else:
        print("Invalid input. Please re-enter employee information.")
        return 0

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
        self.dependents = int(dep)
        self.hoursWorked = float(hours)
        self.hourlyRate = 0 #check if add later
        
def validationModule(employee):
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
    if employee.hoursWorked < 0 or employee.hoursWorked > 80:
        print("Hours worked must be between 0 and 80.")
        valid = False
        
    employee.employeeID = int(employee.employeeID)
    
    return valid

def payRateLookup(eID, database):
    
    payRateFound = False
    
    for record in database:
        if record.employeeID == eID:
            hourlyRate = record.hourlyRate
            payRateFound = True
            break
    
    if payRateFound:
        return hourlyRate
    else:
        print("Error: Invalid Employee ID.")
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
    
    return gross_pay, total_deductions, net_pay

def output():
    
    
    
    return

if __name__ == "__main__":
    person = dataEntry()
    #person.hourlyRate = payRateLookup(person.employeeID, database)
    gross, deductions, net = payCalculation(person)
    output(person)
    

