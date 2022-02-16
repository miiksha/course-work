import os
import time
import sqlite3



def main_menu():
    start = True
    while True:
        if start:
            num_menu = input("\tДобрый день уважаемый гость.\n\tВас приветствует ресторан быстрого питания.\n"
                             "\t\tЧего желаете?\n"
                             "\tВведите 1 чтобы сделать заказ.\n"
                             "\tВведите 2 чтобы посмотреть на свой заказ.\n"
                             "\tВведите 3 чтобы оплатить свой заказ.\n")
        else:
            num_menu = input("\t\tВыберите дальнейшие действия:\n"
                             "\tВведите 1 чтобы изменить заказ.\n"
                             "\tВведите 2 чтобы посмотреть на свой заказ.\n"
                             "\tВведите 3 чтобы оплатить свой заказ.\n")

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
            1) Аппетитные Бургеры\n\
            2) Картошка фри\n\
            3) Жаренные наггетсы\n\
            4) Вкусное мороженое\n\
            5) Освежающие напитки.\n\
            6) Выйти из меню заказа.\n\
                         ')

        if num_food == "1":
            print(1)
        elif num_food == "2":
            print(2)
        elif num_food == "3":
            print(3)
        elif num_food == "4":
            print(4)
        elif num_food == "5":
            print(5)
        elif num_food == "6":
            break
        else:
            print("Введено неверное значение.")






class DataBase:
    @staticmethod
    def create_table():
        connect = sqlite3.connect('food_base')
        sql = connect.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS food (
            name_food TEXT,
            count_food INT,
            PRICE INT
        )""")
        connect.commit()
        connect.close()

    @staticmethod
    def read(select):
        conn = sqlite3.connect('food_base')
        sql = conn.cursor()
        sql.execute(select)
        result = sql.fetchall()
        sql.close()
        conn.close()
        return result

    @staticmethod
    def insert(name,count,price):
        conn = sqlite3.connect('food_base')
        sql = conn.cursor()
        #user_data = DataBase.read(f"SELECT user_id FROM users WHERE user_id = '{message.from_user.id}'")
        #if not user_data:
        sql.execute("INSERT INTO food VALUES (?, ?, ?)",
                        (name, count, price))
        conn.commit()
        sql.close()
        conn.close()


if __name__ == '__main__':
    #main_menu()
    DataBase.create_table()
