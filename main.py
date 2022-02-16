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
            num_menu = input("\n\t\tВыберите дальнейшие действия:\n"
                             "\tВведите 1 чтобы изменить заказ.\n"
                             "\tВведите 2 чтобы посмотреть на свой заказ.\n"
                             "\tВведите 3 чтобы оплатить свой заказ.\n")

        if num_menu == "1":
            os.system('cls')
            start = False
            ordering_food()

        elif num_menu == "2":
            os.system('cls')
            start = False
            info_food = DataBase.read(f"SELECT * FROM food WHERE count_food > {0}")
            if info_food:
                number_in_table = 1
                sum_price = 0
                for food in info_food:
                    print(f"{number_in_table}) {food[0]}.")
                    number_in_table += 1
                    sum_price += (int(food[2])*int(food[1]))
                print(f"\nОбщая сумма заказа составляет: {sum_price}₽")
            else:
                print(f"Ваша корзина пуста.")

        elif num_menu == "3":
            os.system('cls')
            info_food = DataBase.read(f"SELECT * FROM food WHERE count_food > {0}")
            if info_food:
                print("Обработка платежа")  # для оплаты пройдите на кассу + знак загрузки добавить
                time.sleep(2)
                print("Обработка платежа. 50% выполнено.")
                time.sleep(3)
                DataBase.update(0,"*")
                print("Обработка платежа завершена, заказ начал готовиться. Ждём вас снова.")
                start = True
                time.sleep(4)
                os.system('cls')
            else:
                print("Вам пока нечего оплачивать.")

        elif num_menu == "admin":
            print("смена закрыта")
            break
        else:
            print("неверное значение")


def ordering_food():

    while True:

        print("\n\t\t Введите номер желаемого.")

        info_food = DataBase.read(f"SELECT * FROM food")
        number_for_food_intable = 1
        for food in info_food:
            print(f"{number_for_food_intable}) {food[0]}. Цена: {food[2]}₽")
            number_for_food_intable += 1


        try:
            num_food = int(input(""))
        except:
            num_food = 100

        if int(num_food) >= 1 and int(num_food) <= 14:
            try:
                num_food = str(num_food)
                count_food = int(input("Выберите количество этого товара: "))
                if count_food > 10:
                    count_food = 0
                    print("Товар не добавлен в корзину. Введено слишком большое количество.")
            except:
                print("Введено неверное значение.")


        if num_food == "1":
            os.system('cls')
            DataBase.update(count_food,"Острый бургер")
            print("Острый бургер был добавлен в ваш заказ")
        elif num_food == "2":
            print(2)
        elif num_food == "3":
            print(3)
        elif num_food == "4":
            print(4)
        elif num_food == "5":
            break
        else:
            print("Введено неверное значениепппп.")


        close_order = str(input("Желаете продолжить выбор продуктов? (да/нет) "))
        if close_order == "нет":
            break


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
        sql.execute("INSERT INTO food VALUES (?, ?, ?)",
                        (name, count, price))
        conn.commit()
        sql.close()
        conn.close()

    @staticmethod
    def update(new_count, name_food):
        conn = sqlite3.connect('food_base')
        sql = conn.cursor()
        if name_food == "*":
            sql.execute(f'UPDATE food SET count_food = "{new_count}"')
        else:
            sql.execute(f'UPDATE food SET count_food = "{new_count}" WHERE name_food = "{name_food}"')
        conn.commit()
        sql.close()
        conn.close()




















if __name__ == '__main__':
    main_menu()






















    # DataBase.insert("Острый бургер",0,158)
    # DataBase.insert("Бургер классический",0,148)
    # DataBase.insert("Картошка фри",0,55)
    # DataBase.insert("Картошка фри по-деревенски",0,70)
    # DataBase.insert("Пломбир",0,40)
    # DataBase.insert("Пломбир с ванилью",0,50)
    # DataBase.insert("Пломбир с шоколадом",0,52)
    # DataBase.insert("Пломбир со вкусом малины",0,55)
    # DataBase.insert("Пепси 0,5л",0,79)
    # DataBase.insert("Чай чёрный 0,3",0,49)
    # DataBase.insert("Чай зелёный 0,3",0,49)
    # DataBase.insert("Кофе 0,3",0,57)
    # DataBase.insert("Кока-кола 0,5л",0,79)
    # DataBase.insert("Спрайт 0,5л",0,79)