from colorama import Fore, Style


class Dog:
    def __init__(self):
        self.__age = None
        self.__name = None
        self.__voice = None

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def voice(self):
        return self.__voice

    @age.setter
    def age(self, age):
        if 0 <= age <= 35:
            self.__age = age
        else:
            print(Fore.RED + "Недопустимый возраст!" + Style.RESET_ALL)

    @name.setter
    def name(self, name):
        self.__name = name

    @voice.setter
    def voice(self, voice):
        voice = voice.lower()
        found = any(letter in voice for letter in ["гав", "gav", "ау"])
        if found:
            self.__voice = voice
        else:
            print(Fore.RED + "Недопустимый лай!" + Style.RESET_ALL)

    def print_dog(self):
        print(f"Имя собаки: {self.__name}, Возраст собаки: {self.__age}, Лай собаки: {self.__voice}")


def create_dog():
    dog = {
        "age": int(input("Введите возраст собаки: ")),
        "name": input("Введите имя собаки: "),
        "voice": input("Введите лай собаки: ")
    }
    return dog


def main():
    dog = Dog()
    dog.age = int(input("Введите возраст собаки: "))
    dog.name = input("Введите имя собаки: ")
    dog.voice = input("Введите лай собаки: ")
    dog.print_dog()
    return dog


if __name__ == "__main__":
    dogs = []
    while True:
        print("Добавьте свою собаку:")
        dogs.append(main())
