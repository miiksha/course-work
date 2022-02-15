

def main_menu():
    while True:
        num_menu = input("введи номер 1,2,3. 4 для выхода")
        if num_menu == "1":
            print(1)
        elif num_menu == "2":
            print(2)
        elif num_menu == "3":
            print(3)
        elif num_menu == "4":
            print("выход")
            break
        else:
            print("неверное значение")




if __name__ == '__main__':
    main_menu()
