import os
import shutil
import platform
import use_functions_bank_balance # модуль баланса с покупками
import victory_function # модуль викторины

def create_folder(path):
    new_folder_name = input("Введите имя новой папки: ")
    os.makedirs(os.path.join(path, new_folder_name), exist_ok=True) # даем возможность создать еще и вложенные папки
    print(f"Папка '{new_folder_name}' успешно создана.")


def delete_item(path):
    item_name = input("Введите имя файла или папки для удаления: ")
    item_path = os.path.join(path, item_name)

    if os.path.exists(item_path): # если путь существует, то
        if os.path.isdir(item_path): # если по указзанному пути  - папка ,
            os.rmdir(item_path) # то удаляем пустую папку (для непустой папки надо другую функцию применить)
            print(f"Папка '{item_name}' успешно удалена.")
        else:
            os.remove(item_path) # иначе удаляем файл (не папка)
            print(f"Файл '{item_name}' успешно удалён.")
    else:
        print(f"'{item_name}' не найдено.")


def copy_item(path):
    item_name = input("Введите имя файла или папки для копирования: ")
    item_path = os.path.join(path, item_name)

    if os.path.exists(item_path): # если путь существует, то
        destination = input("Введите путь назначения: ")
        shutil.copytree(item_path, os.path.join(destination, item_name)) if os.path.isdir(item_path) else shutil.copy(
            item_path, destination) # копируем в заданный путь
        print(f"'{item_name}' успешно скопирован.")
    else:
        print(f"'{item_name}' не найдено.")


def list_directory(path):
    items = os.listdir(path)
    print("Содержимое рабочей директории:")

    for item in items:
        print(item)


def list_folders(path):
    items = os.listdir(path)
    print("Папки в текущей директории:")
    for item in items:
        if os.path.isdir(os.path.join(path, item)): # если папка, то печатаем папку
            print(item)


def list_files(path):
    items = os.listdir(path)
    print("Файлы в текущей директории:")
    for item in items:
        if os.path.isfile(os.path.join(path, item)): # если файл, то печатаем
            print(item)


def system_info():
    print("Информация об операционной системе:")
    print(platform.platform())
    print(os.getenv("TMP"))


def creator_info():
    print("Создатель программы: Айнур")


def change_directory():
    new_path = input("Введите новый путь директории: ")
    if os.path.isdir(new_path):
        return new_path
    else:
        print("Неправильный путь. Остаёмся в текущей директории.")
        return current_directory


if __name__ == "__main__":  # если здесь вызвана функция, то выполняем
    current_directory = os.getcwd() # считать текущую директорию
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_folder(current_directory)
        elif choice == "2":
            delete_item(current_directory)
        elif choice == "3":
            copy_item(current_directory)
        elif choice == "4":
            list_directory(current_directory)
        elif choice == "5":
            list_folders(current_directory)
        elif choice == "6":
            list_files(current_directory)
        elif choice == "7":
            system_info()
        elif choice == "8":
            creator_info()
        elif choice == "9":
            victory_function.play_quiz()
        elif choice == "10":
            use_functions_bank_balance.bank_account()
        elif choice == "11":
            current_directory = change_directory()
        elif choice == "12":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите пункт из меню.")