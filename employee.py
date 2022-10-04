"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary, hourlyWage, numberHours, fixedBonus, numberContracts, comissionPerContract):
        self.name = name
        self.monthlySalary = monthlySalary
        self.hourlyWage = hourlyWage
        self.numberHours = numberHours
        self.fixedBonus = fixedBonus
        self.numberContracts = numberContracts
        self.comissionPerContract = comissionPerContract

    def get_pay(self):
        return self.monthlySalary + self.hourlyWage * self.numberHours + self.fixedBonus + self.numberContracts * self.comissionPerContract

    def __str__(self):
        if self.monthlySalary > 0 and self.fixedBonus > 0:
            return f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a bonus commission of {self.fixedBonus}.  Their total pay is {self.get_pay()}."
        elif self.monthlySalary > 0 and self.comissionPerContract > 0:
            return f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a commission for {self.numberContracts} contract(s) at {self.comissionPerContract}/contract. Their total pay is {self.get_pay()}."
        elif self.monthlySalary > 0:
            return f"{self.name} works on a monthly salary of {self.monthlySalary}. Their total pay is {self.get_pay()}."
        elif self.hourlyWage > 0 and self.fixedBonus > 0:
            return f"{self.name} works on a contract of {self.numberHours} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.fixedBonus}.  Their total pay is {self.get_pay()}."
        elif self.hourlyWage > 0 and self.comissionPerContract > 0:
            return f"{self.name} works on a contract of {self.numberHours} hours at {self.hourlyWage}/hour and receives a commission for {self.numberContracts} contract(s) at {self.comissionPerContract}/contract. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.numberHours} hours at {self.hourlyWage}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 600, 0, 0)
