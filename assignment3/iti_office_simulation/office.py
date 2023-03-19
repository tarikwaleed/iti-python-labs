class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, emp):
        self.employees.append(emp)
        self.__class__.employeesNum += 1

    def fire(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                self.employees.remove(emp)
                self.__class__.employeesNum -= 1
                break

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp is not None:
            targetHour = 9
            distance = emp.distanceToWork
            velocity = emp.car.velocity
            is_late = not self.calculate_lateness(targetHour, moveHour, distance, velocity)
            if is_late:
                emp.mood = 'tired'
                emp.healthRate -= 10
                emp.salary -= 10
            else:
                emp.mood = 'happy'
                emp.salary += 10

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrivalTime = moveHour + (distance / velocity)
        return arrivalTime <= targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
