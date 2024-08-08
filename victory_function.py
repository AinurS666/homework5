import random

def play_quiz():

    # исходные данные
    family = {'Пушкин': '26.05.1799',
              'Грозный': '25.08.1530',
              'Чехов': '16.04.1860',
              'Пастернак': '30.01.1890',
              'Бианки': '12.12.1811',
              'Лермонтов': '3.10.1814',
              'Крылов': '13.02.1769',
              'Распутин': '9.01.1869',
              'Толстой': '9.09.1828',
              'Тютчев': '5.12.1803'

              }

    months = {
        '01': 'январь',
        '02': 'февраль',
        '03': 'март',
        '04': 'апрель',
        '05': 'май',
        '06': 'июнь',
        '07': 'июль',
        '08': 'август',
        '09': 'сентябрь',
        '10': 'октябрь',
        '11': 'ноябрь',
        '12': 'декабрь'
    }

    days = {
        '1': 'первое',
        '2': 'второе',
        '3': 'третье',
        '4': 'четвёртое',
        '5': 'пятое',
        '6': 'шестое',
        '7': 'седьмое',
        '8': 'восьмое',
        '9': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцати первое',
        '22': 'двадцати второе',
        '23': 'двадцати третье',
        '24': 'двадцати четвёртое',
        '25': 'двадцати пятое',
        '26': 'двадцати шестое',
        '27': 'двадцати седьмое',
        '28': 'двадцати восьмое',
        '29': 'двадцати девятое',
        '30': 'тридцатое',
        '31': 'тридцати первое'
    }
    # days,months,year=family.values().split('.')
    # созадем список от 1 до 10
    numbers = list(range(1, 11,))

    # храним последовательность чисел рандомных,5шт
    n=5 # кол-во вопросов должно быть меньше 10
    # result = random.sample(numbers, n)

    answer_true = 0  # кол-во правильных ответов
    percent_true = 0.0  # кол-во правильных ответов в %
    answer = ''  # здесь храним данные по ответам





    # Преобразуем ключи в список
    key_index=list(family.keys())

    player_want = 1  # пожелание играть 1= хотим,0 - не хотим
    while player_want != '0':# играем пока пользователь хочет
        # печатаю порядковые номера, по которым будем спрашивать по викторине
        result = random.sample(numbers, n)
        print('номера вопросов в словаре для контроля \n', result)
        for i in range(len(result)):
            print(f'Введите дату рождения {key_index[result[i]-1]} : ')
            answer = input("")
            if answer == family[key_index[result[i]-1]]:
                answer_true += 1
            else:
                day, month, year = family[key_index[result[i]-1]].split('.')
                print(f"не верно, {key_index[result[i]-1]} родился ", days[day], months[month], year,'года \n')


        print('кол-во верных ответов = ', answer_true)
        print('кол-во верных ответов в % = ', answer_true * 100 / (len(result)))
        print('кол-во Не верных ответов = ', len(result) - answer_true)
        print('кол-во Не верных ответов в % = ', 100 - answer_true * 100 / (len(result)))
        answer_true = 0  # обнуляем

        player_want = input("Повторим викторину ? (1/0) ")