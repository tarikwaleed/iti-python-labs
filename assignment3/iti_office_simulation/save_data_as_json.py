import json
from assignment3.iti_office_simulation.employee import Employee
from assignment3.iti_office_simulation.office import Office

itiOffice = Office("ITI")
emp1 = Employee("Ahmed", 1, "Car1", "ahmed@example.com", 5000, 20)
emp2 = Employee("Mohamed", 2, "Car2", "mohamed@example.com", 6000, 30)
itiOffice.hire(emp1)
itiOffice.hire(emp2)

with open("iti_office.json", "w") as f:
    json.dump(itiOffice.__dict__, f, indent=4)
