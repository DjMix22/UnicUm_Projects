class LengthConverter:
    def __init__(self, kilometers):
        self.kilometers = kilometers

    def to_meters(self):
        return self.kilometers * 1000

    def to_yards(self):
        return self.kilometers * 1093.61

    def to_miles(self):
        return self.kilometers * 0.621371

    def to_centimeters(self):
        return self.kilometers * 100000

    def to_millimeters(self):
        return self.kilometers * 1000000

    def to_feet(self):
        return self.kilometers * 3280.84


class TimeConverter:
    def __init__(self, seconds):
        self.seconds = seconds

    def to_minutes(self):
        return self.seconds / 60

    def to_hours(self):
        return self.seconds / 3600

    def to_days(self):
        return self.seconds / 86400

    def to_weeks(self):
        return self.seconds / 604800

    def to_months(self, days_per_month=30.4375):
        return self.seconds / (86400 * days_per_month)

    def to_years(self, days_per_year=365.2425):
        return self.seconds / (86400 * days_per_year)


def main():
    print("Выберите, что вы хотите:\n1) Конвертер расстояния\n2) Конвертер времени\n3) Завершить работу программы")
    while True:
        action = input("--> ")
        if action == "1":
            kms = LengthConverter(int(input("Введите кол-во километров: ")))
            length = {
                "1": kms.to_meters,
                "2": kms.to_feet,
                "3": kms.to_miles,
                "4": kms.to_yards
            }
            print("Введите действие:\n1) В метры\n2) В футы\n3) В мили\n4) В йарды")
            move = input("--> ")
            if move in length:
                print(length[move]())

        elif action == "2":
            ...
            # Код, который переводит время (он как в предыдущем ифе, просто не успел дописать)

        elif action == "3":
            print("До свидания!")
            exit()


if __name__ == '__main__':
    main()
