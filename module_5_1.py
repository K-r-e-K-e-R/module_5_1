class House:
    class House:
        def __init__(self, name, floors):
            self.name = name
            self.floors = floors

        def go_to(self, new_floor):
            if 1 <= new_floor <= self.floors:
                print(f"Вы поднимаетесь на этаж {new_floor} в здании {self.name}.")
                for i in range(1, new_floor + 1):
                    print(f"Этаж {i}")
            else:
                print("Такого этажа не существует.")

    home1 = House("ЖК Эльбрус", 10)
    home2 = House("ЖК Альбатрос", 16)

    print(home1.name, home1.floors)
    print(home2.name, home2.floors)

    home1.go_to(5)
    home2.go_to(17)
