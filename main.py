import os
import time


def main_menu():
    start = True
    while True:
        if start:
            num_menu = input("\tДобрый день уважаемый гость.\n\tВас приветствует ресторан быстрого питания.\n\
            Чего желаете?\n\
            Введите 1 чтобы сделать заказ.\n\
            Введите 2 чтобы посмотреть на свой заказ.\n\
            Введите 3 чтобы оплатить свой заказ.\n\
                         ")
        else:
            num_menu = input("\
            Выберите дальнейшие действия:\n\
            Введите 1 чтобы изменить заказ.\n\
            Введите 2 чтобы посмотреть на свой заказ.\n\
            Введите 3 чтобы оплатить свой заказ.\n\
                         ")

        if num_menu == "1":
            start = False
            print(1)
            ordering_food()
        elif num_menu == "2":
            start = False
            print(2)
        elif num_menu == "3":
            print("Обработка платежа")  # для оплаты пройдите на кассу + знак загрузки добавить
            time.sleep(2)
            print("Обработка платежа. 50% выполнено.")
            time.sleep(3)
            print("Обработка платежа завершена, заказ начал готовиться. Ждём вас снова.")
            start = True
            time.sleep(4)
            os.system('cls')
        elif num_menu == "admin":
            print("смена закрыта")
            break
        else:
            print("неверное значение")


def ordering_food():
    print("\t\t Введите номер желаемого.")
    while True:
        num_food = input('\
            1) Пицца\n\
            2) Бургеры\n\
            3) Картошка\n\
            4) Наггетсы\n\
            5) Мороженое\n\
            6) Напитки\n\
                         ')


if __name__ == '__main__':
    main_menu()
