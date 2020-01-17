class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__ (self, carBrand, carModel):
        self.carBrand = carBrand
        self.carModel = carModel

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        if type(cars) == type([]):
        self.cars = cars
    else:
        print("Ошибка! Неверный тип данных!!!")
        exit

    def addСar(self, car):
        self.cars.append(car)

    def __getItem__(self, position):
        return self.cars[position]

    def __len__(self):
        return len(self.cars)

    def delete(self, index):
        del self.cars[index]