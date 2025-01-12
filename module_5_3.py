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

    def __eq__(self, other):
        return self.floor_number == other.floor_number


    def __add__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError('Правый оператор должен иметь тип Int')
        self.floor_number = self.floor_number + value
        return self


    def __iadd__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError('Правый оператор должен иметь тип Int или являться объектом House')
        self.floor_number += other
        return self


    def __radd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError('Левый оператор должен иметь тип Int или являться объектом House')
        self.floor_number = value + self.floor_number
        return self

    def __gt__(self, other):
        return self.floor_number > other.floor_number

    def __ge__(self, other):
        return self.floor_number >= other.floor_number

    def __lt__(self, other):
        return self.floor_number < other.floor_number

    def __le__(self, other):
        return self.floor_number <= other.floor_number

    def __ne__(self, other):
        return self.floor_number != other.floor_number

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#eq
print(h1)
print(h2)
print(h1 == h2)

#add
h1 = h1 + 10
print(h1)
print(h1 == h2)

#iadd
h1 += 10
print(h1)

#radd
h2 = 10 + h2
print(h2)

#gt
print(h1 > h2)

#ge
print(h1 >= h2)

#lt
print(h1 < h2)

#le
print(h1 <= h2)

#ne
print(h1 != h2)


