class House:
    def __init__(self, name, floor_number):
        self.name = name
        self.floor_number = floor_number
    def go_to(self, new_floor):
        if new_floor <= self.floor_number and new_floor > 1:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)