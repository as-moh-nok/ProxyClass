from audioop import minmax


class WorkPlace:
    instances = [] #static variable

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)
    
    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass #pass 

    def calc_capacity(self):
        pass #pass

    def upgrade(self):
        self.level +=1
        self.capacity = self.calc_capacity()  #correct this
        
    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person) #mybe need
            person.work_place = self

    def get_expertise(self):
        return self.expertise

    def calc(self):
        return -(self.calc_costs())

    @staticmethod
    def calc_all():
        sum = 0
        for i in WorkPlace.instances:
            sum += i.calc()

class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"

class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}

class Person:
            pass


w = WorkPlace("quera")
w.expertise = "mine"
w.capacity = 3
p = Person()
p.name = 'sina'
p.work_place = None
w.hire(p)
p2 = Person()
p2.name = 'mina'
p2.work_place = None
w.hire(p2)

for wp in WorkPlace.instances:
    print(wp.name, wp.capacity)

for p in w.employees:
    print(p.name, p.work_place)