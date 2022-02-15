

def main_menu():
    while True:
        num_menu = input("введи номер")
        if num_menu == "1":
            print(1)
        elif num_menu == "2":
            print(2)
        elif num_menu == "3":
            print(3)
        else:
            print("завершение")
            break



if __name__ == '__main__':
    main_menu()
