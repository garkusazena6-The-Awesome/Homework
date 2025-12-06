import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 1
        self.money = 150
        self.alive = True
    def to_study(self):
        print("Time to study!")
        self.progress += 0.20
        self.gladness -= 3
    def to_sleep(self):
        print("ZZZZZZzzzzzz")
        self.gladness +=3
        self.progress += 0.20
    def to_chill(self):
        print("Gotta chill for awhile")
        self.gladness +=5
        self.progress -= 0.2
        self.money = -25
    def to_work(self):
        print("I need money so bad..")
        self.gladness -= 2.5
        self.money += 35
    def is_alive(self):
        if self.progress <= -0.5:
            print("He cant take anymore , he..hangs himself.")
            self.alive = False
        elif  self.progress <= 0.01:
            print("He fells..depressing..")
            self.alive = False
        elif self.progress >= 5:
            print("He made it!")
            self.alive = False
    def is_wealthy(self):
        if self.money <=0:
            print("He so poor , he cant pay for school anymore and lives on the streets")
            self.alive = False
        elif self.money >= 300:
            print("Why study if you can buy the school?")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
        print(f"Money = {self.money}")
    def live(self,day):
        day = "Day" + str(day) + "For" + self.name + "Live"
        print(f"{day:=^50}")
        choose = random.randint(1,4)
        if choose == 1:
            self.to_study()
        elif choose == 2:
            self.to_sleep()
        elif choose == 3:
            self.to_chill()
        elif choose == 4:
            self.to_work()
        self.is_alive()
        self.end_of_day()
Student = Student(name="Student")
for day in range(365):
    if Student.alive == False:
        break
    Student.live(day)
