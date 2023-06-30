class PhonebookEntry:
    def __init__(self, first_name, last_name, middle_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}: {self.phone_number}"


class Phonebook:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, first_name, last_name):
        for entry in self.entries:
            if entry.first_name == first_name and entry.last_name == last_name:
                self.entries.remove(entry)
                return True
        return False

    def update_entry(self, first_name, last_name, new_entry):
        for entry in self.entries:
            if entry.first_name == first_name and entry.last_name == last_name:
                entry.first_name = new_entry.first_name
                entry.last_name = new_entry.last_name
                entry.middle_name = new_entry.middle_name
                entry.phone_number = new_entry.phone_number
                return True
        return False

    def search_entry(self, search_query):
        results = []
        for entry in self.entries:
            if search_query.lower() in entry.first_name.lower() or search_query.lower() in entry.last_name.lower():
                results.append(entry)
        return results

    def export_to_txt(self, file_name):
        with open(file_name, "w") as file:
            for entry in self.entries:
                file.write(f"{entry.last_name},{entry.first_name},{entry.middle_name},{entry.phone_number}\n")

    def import_from_txt(self, file_name):
        self.entries = []
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 4:
                    entry = PhonebookEntry(data[1], data[0], data[2], data[3])
                    self.add_entry(entry)


def print_entries(entries):
    if len(entries) > 0:
        for entry in entries:
            print(entry)
    else:
        print("Нет результатов.")


def print_menu():
    print("Меню:")
    print("1. Вывести все записи")
    print("2. Добавить запись")
    print("3. Удалить запись")
    print("4. Изменить запись")
    print("5. Поиск записей")
    print("6. Экспорт в файл")
    print("7. Импорт из файла")
    print("0. Выход")


def run_phonebook():
    phonebook = Phonebook()

    while True:
        print()
        print_menu()
        choice = input("Выберите команду: ")

        if choice == "1":
            print("Все записи:")
            print_entries(phonebook.entries)
        elif choice == "2":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            entry = PhonebookEntry(first_name, last_name, middle_name, phone_number)
            phonebook.add_entry(entry)
            print("Запись успешно добавлена.")
        elif choice == "3":
            first_name = input("Введите имя для удаления записи: ")
            last_name = input("Введите фамилию для удаления записи: ")
            if phonebook.remove_entry(first_name, last_name):
                print("Запись успешно удалена.")
            else:
                print("Запись не найдена.")
        elif choice == "4":
            update_first_name = input("Введите имя для изменения записи: ")
            update_last_name = input("Введите фамилию для изменения записи: ")
            new_first_name = input("Введите новое имя: ")
            new_last_name = input("Введите новую фамилию: ")
            new_middle_name = input("Введите новое отчество: ")
            new_phone_number = input("Введите новый номер телефона: ")
            new_entry = PhonebookEntry(new_first_name, new_last_name, new_middle_name, new_phone_number)
            if phonebook.update_entry(update_first_name, update_last_name, new_entry):
                print("Запись успешно изменена.")
            else:
                print("Запись не найдена.")
        elif choice == "5":
            search_query = input("Введите имя или фамилию для поиска: ")
            results = phonebook.search_entry(search_query)
            print("Результаты поиска:")
            print_entries(results)
        elif choice == "6":
            file_name = input("Введите имя файла для экспорта: ")
            phonebook.export_to_txt(file_name)
            print("Данные успешно экспортированы в файл.")
        elif choice == "7":
            file_name = input("Введите имя файла для импорта: ")
            phonebook.import_from_txt(file_name)
            print("Данные успешно импортированы из файла.")
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


run_phonebook()
