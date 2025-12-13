import random
class Human:
    def __init__(self,name="human"):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.society = 50
        self.home = Home()
        self.car = Car()
        self.job = Job()
    def eat(self):
        if self.home.food <= 0:
            self.shopping("Buy food")
        self.society = min(100,self.society + 20)
    def work(self):
        if not self.car.drive():
            print("You need to repair car")
            self.car.repair()
            self.money -= 20
        else:
            print("Go to work")
            self.money += self.job.salary
            self.gladness -= 5
            self.society -= 10
    def chill(self):
        self.society -=5
    def mess_home(self):
        print("Clean my home")
        self.gladness -= 5
        self.home.mess = 0
    def shopping(self,type):
        if type == "Shop":
            print("Buy food")
            self.money -= 30
            self.home.food += 30
        elif type == "Fuel":
            print("Fuel car")
            self.money -= 40
            self.car.fuel += 40
    def walk(self):
        print("Time for a walk")
        self.gladness += 5
    def is_alive(self):
        if self.society <= 0 : print("To hungry"); return False
        if self.gladness <= 0 : print("To depressed"); return False
        if self.money <= 0 : print("To poor"); return False
        return True
    def day_live(self):
        print(f"\n----- Day {day} life {self.name} -----")
        print(f"Money: {self.money} Satiety {self.society} Gladness {self.gladness} Food {self.eat}")
        if self.society < 20: self.eat()
        elif self.gladness < 20: self.chill()
        elif self.car.fuel < 20: self.shopping("Fuel")
        elif self.home.mess > 20: self.clean.home()
        elif self.gladness < 15: self.walk()
        else:
            random.choice([self.eat, self.work, self.chill])()


class Car:
    def __init__(self):
        self.fuel = 50
        self.strenght = 50
    def drive(self):
        if self.fuel > 5 and self.strenght > 0:
            self.fuel -= 5
            self.strenght -= 1
            return True
    def repair(self):
        self.strenght += 10
class Job:
    def __init__(self):
        self.salary = random.choice([30,40,50,60,70])
class Home:
    def __init__(self):
        self.food = 20
        self.mess = 0
class Park:
    def __init__(self):
        self.walk = 0
    def walk(self):
        self.walk += 10
        self.gladness += 5
Player = Human("Player")
for day in range(1,8):
    if not Player.is_alive():
        break
    Player.day_live()