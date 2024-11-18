#1) If a manager has direct reports in more than one city, print their phone number
#2) If a manager has anyone in his chain of reports in more than one city, print their phone number

import csv
import os.path
import sys

def main():
    if not os.path.exists(sys.argv[1]):
        print("Invalid file path given. Exiting.")
        sys.exit(1)

    employees = []
    managers = {}
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].isdigit():
                emp = Employee(row[0], row[1], row[2], row[3])
                employees.append(emp)

                mgrid = emp.mgr_id

                #Check to see if this employee's manager is in the list of managers yet
                #If it isn't, add that ID with an empty list for its value
                if mgrid not in managers.keys():
                    managers[mgrid] = []

                #manager should be in the managers list now so add this employee to the mgr's value list
                managers[mgrid].append(emp)

    #this is a coding exercise so I'm assuming the correct args are provided, otherwise I'd check for empty args/help 
    if sys.argv[2] == '1':
        print("Problem 1: Here are the phone numbers of any managers whose reports live in multiple cities")
        for key, value in managers.items():
            locations = [emp.city for emp in value]

            # Cast the list to a set to dedupe. 
            # If the set's length is greater than one, this manager's reports live in multiple cities
            if len(set(locations)) > 1:
                # The key in the managers dict is the emp ID of the manager
                # Loop through the employees to find the manager in question and print their phone number
                for emp in employees:
                    if emp.emp_id == key:
                        print(f"Manager's phone number: {emp.phone}")



class Employee:
    def __init__(self, emp_id, mgr_id, city, phone):
        self.emp_id = int(emp_id)
        self.mgr_id = int(mgr_id)
        self.city = city
        self.phone = phone

    def __repr__(self):
        return f"Employee ID:{self.emp_id}, Manager ID:{self.mgr_id}, City:{self.city}, Phone #:{self.phone}"
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.emp_id)


if __name__ == '__main__':
    main()