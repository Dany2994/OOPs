class Employee:
    def __init__(self, id, name, position, salary):
        self.id=id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, position, salary):
            employee = Employee(id, name, position, salary)
            self.employees.append(employee)

    def remove_employee(self, id):
        self.employees = [employee for employee in self.employees if employee.id != id] 

    def list_employees(self):
         for employee in self.employees:
              print(employee)

def main():
    manager =EmployeeManager()

    while True:
        print("\Employee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. List Employees")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee's position: ")
            salary = input("Enter employee Salary: ")
            manager.add_employee(id, name, position, salary)
            print("Employee addded successfully")            
        elif choice == "2":
            id = input("Enter employee ID to remove: ")
            manager.remove_employee(id)
            print("Employee removed successfully.")
        elif choice == "3":
            print("Employees list: \n")
            manager.list_employees()
        elif choice == "4":
            print("Exiting... ")
            break
        else:
            print("Invalid choose, please try again")

if __name__ == "__main__":
    main()
