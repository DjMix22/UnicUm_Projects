import json


class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return self.orders

    def __str__(self):
        return f"Пользователь: {self.name}"


class Menu:
    def __init__(self):
        with open('menu.json', 'r', encoding='utf-8') as file:
            self._menu = json.load(file)

    def get_menu(self):
        return self._menu


class Pizzeria:
    def __init__(self):
        self._shop_list = []

    @property
    def shop_list(self):
        return self._shop_list

    @property
    def product(self):
        if self._shop_list:
            return self._shop_list[-1]

    @product.setter
    def product(self, product):
        self._shop_list.append(product)

    def clear_shop_list(self):
        self._shop_list.clear()


def main():
    pizzeria = Pizzeria()
    user = User(input("Введите ваше имя: "))

    print("Выберите действие:\n"
          "1) Вывести корзину\n"
          "2) Добавить продукт в корзину\n"
          "3) Оформить заказ\n"
          "4) Посмотреть историю заказов\n"
          "5) Выйти из программы")

    while True:
        menu = Menu()
        products = menu.get_menu()

        action = input('--> ')

        if action == '1':
            if pizzeria.shop_list:
                print(', '.join(pizzeria.shop_list))
            else:
                print('Ваша корзина пуста!')

        elif action == '2':
            print(f'Продукты:')
            for product in products.keys():
                print(f"{product}) {products[product]}")
            product_input = input('Введите номер продукта, чтобы добавить его в корзину: ')
            if product_input in products:
                pizzeria.product = products[product_input]
                print('Продукт успешно добавлен!')

        elif action == '3':
            if pizzeria.shop_list:
                order = ', '.join(pizzeria.shop_list)
                user.place_order(order)
                pizzeria.clear_shop_list()
                print('Заказ оформлен!')

            else:
                print('Ваша корзина пуста!')

        elif action == '4':
            print('История заказов:')
            for order in user.get_order_history():
                print(order)

        elif action == '5':
            print('До свидания!')
            exit()


if __name__ == '__main__':
    main()
