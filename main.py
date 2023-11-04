import random


class human:
    def __init__(self, name = "Human", job = None, Home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = Home
        self.car = car

    def get_home(self):
        self.home = House()
        
    def get_car(self):
        self.car = Auto(brands_of_car)

    def to_repair(self):
        if self.car:
            self.car.strength = brand_of_car[self.car.brand]["strength"]

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = job(job_list)


Class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(brand_list)
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("You can't drive")


class job:
    def __init__(self, joblist):
        self.Value(random.randint(0, len(joblist)))


job_list = {
    "Java developer": {"Salary": 50, "gladness_less": 10},
    "Python developer": {"Salary": 40, "gladness_less": 3},
    "C++ developer": {"Salary": 60, "gladness_less": 25},
    "Rust developer": {"Salary": 70, "gladness_less": 15},
}


brands_of_car = {
    "AUDI": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel" : 50, "strength": 40, "consumption": 10},
    "BMW": {"fuel": 80, "strength": 150, "consumption": 8},
    "Mercedes": {"fuel": 80, "strength": 120, "consumption": 14},
}
        
        
        