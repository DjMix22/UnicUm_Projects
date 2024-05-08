class Car:
    def __init__(self):
        self._model = None
        self._mark = None
        self._engine = None
        self._color = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, mark):
        self._mark = mark

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.engine < other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __le__(self, other):
        if isinstance(other, Car):
            return self.engine <= other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.engine == other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __ne__(self, other):
        if isinstance(other, Car):
            return self.engine != other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.engine > other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __ge__(self, other):
        if isinstance(other, Car):
            return self.engine >= other.engine
        else:
            raise TypeError("Сравнение возможно только с объектами класса Car")

    def __str__(self):
        return f"Машина моделью {self._model}, объемом двигателя {self._engine}, маркой {self._mark}, цветом {self._color}"


def main():
    cars = []
    print("Выберите действие:\n1) Создать машину\n2) Сравнить машины\n3) Вывести все машины\n4) Завершить программу")
    while True:
        action = input("--> ")
        if action == '1':
            car = Car()
            car.model = str(input("Введите модель машины: "))
            car.engine = int(input("Введите объем двигателя машины: "))
            car.mark = str(input("Введите марку машины: "))
            car.color = str(input("Введите цвет машины: "))
            cars.append(car)

        elif action == '2':
            if len(cars) < 2:
                print("Вы создали менее 2 машин!")
            else:
                print(f"car[0] != car[1]: {cars[0].ne(cars[1])}")
            # Ещё сравнения
              
        elif action == '3':
            print(",\n".join(cars))
          
        elif action == '4':
            print("До свидания!")
            exit()


if __name__ == '__main__':
    main()
