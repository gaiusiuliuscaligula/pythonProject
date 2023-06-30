class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        if isinstance(item, OfficeEquipment):
            if item.name in self.inventory:
                self.inventory[item.name] += item.quantity
            else:
                self.inventory[item.name] = item.quantity
            print(f"Оргтехника '{item.name}' добавлена на склад.")
        else:
            print("Ошибка: Можно добавлять только объекты класса 'OfficeEquipment' на склад.")

    def transfer_item(self, item_name, quantity, department):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                print(f"{quantity} единиц оргтехники '{item_name}' переданы в подразделение '{department}'.")
            else:
                print("Ошибка: Недостаточно оргтехники на складе.")
        else:
            print("Ошибка: Оргтехника с таким наименованием отсутствует на складе.")

    def display_inventory(self):
        print("Остатки оргтехники на складе:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity} шт.")


class OfficeEquipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, color):
        super().__init__(name, quantity)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, resolution):
        super().__init__(name, quantity)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, speed):
        super().__init__(name, quantity)
        self.speed = speed


# Функция для отображения меню
def display_menu():
    print("Меню:")
    print("1. Добавить оргтехнику на склад")
    print("2. Передать оргтехнику в подразделение")
    print("3. Вывести остатки оргтехники на складе")
    print("4. Выйти из программы")


# Пример использования классов

# Создаем объект склада
warehouse = Warehouse()

while True:
    display_menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        name = input("Введите наименование оргтехники: ")
        quantity = int(input("Введите количество единиц оргтехники: "))
        color = input("Введите цвет (для принтера): ")
        printer = Printer(name, quantity, color)
        warehouse.add_item(printer)

    elif choice == "2":
        name = input("Введите наименование оргтехники: ")
        quantity = int(input("Введите количество единиц оргтехники: "))
        department = input("Введите название подразделения: ")
        warehouse.transfer_item(name, quantity, department)

    elif choice == "3":
        warehouse.display_inventory()

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Ошибка: Введите правильный пункт меню.")
