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

    def __len__(self):
        return self.floor_number

    def __str__(self):
        text = f'Название: {self.name}, кол-во этажей: {self.floor_number}'
        return text

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1.go_to(5)
h2.go_to(10)

print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))
