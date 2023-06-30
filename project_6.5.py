class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}  # Защищенный атрибут income

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

# Создание экземпляра класса Position
position = Position("John", "Doe", "Manager", 5000, 1000)

# Получение полного имени сотрудника
full_name = position.get_full_name()

# Получение дохода с учетом премии
total_income = position.get_total_income()

# Вывод результатов
print(f"Полное имя сотрудника: {full_name}")
print(f"Доход с учетом премии: {total_income}")
