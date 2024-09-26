class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.floors:
            print(f"Вы находитесь на этаже {new_floor} в здании {self.name}.")
        else:
            print("Такого этажа не существует.")

    def total_floors_first(self):
        print(f"Вы поднимайтесь на этаж здания {self.name}")
        for i in range(1, 8):
            print(i)

    def total_floors_second(self):
        print(f"Вы поднимайтесь на этаж здания {self.name}")
        for j in range(1, 12):
            print(j)


home1 = House("ЖК Эльбрус", 10)
home2 = House("ЖК Альбатрос", 16)

print(home1.name, home1.floors)
print(home2.name, home2.floors)

home1.total_floors_first()
home2.total_floors_second()

home1.go_to(8)
home1.go_to(15)
home2.go_to(12)
