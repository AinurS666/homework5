# храним баланс
Balance = 0

# записываем в словарь название покупки и их стоимость
SHOP = {}

# функция печати
def print_tekst():
    print('\n1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход\n')

def bank_account():

    while True:
        print_tekst() # печатаем стандартый текст

        choice = input('Выберите пункт меню ')

        if choice == '1':
            global Balance
            Balance+= int(input("На какую сумму будем пополнять? "))

        elif choice == '2':
            Cost = int(input("Сумма покупки? "))
            if Balance >= Cost: # если баланса хватает, то заносим в словарь
                Name_shop = input("название  покупки ")
                Balance -= Cost # уменьшаем баланс на цену покупки
                SHOP.update({Name_shop:Cost}) # заносим баланс
                # print(SHOP) этот код для отладки был
                # print('Баланс',Balance) этот код для отладки был
            else:
                print("не достаточно денег")


        elif choice == '3':
            for key, value in SHOP.items():
                print(f'покупка {(key)} за {value} рублей')

        elif choice == '4':
            break

        else:
            print('Неверный пункт меню')
