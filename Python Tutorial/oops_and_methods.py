class Employee:
    company = "Google"
    salary = 400
    bonus = 500

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employpee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning, Sir")

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

    @property
    def totalSalary(self):
        return self.salary + self.bonus

harry = Employee("Dharm", 500, "web developer")
harry.getDetails()
print(harry.totalSalary)