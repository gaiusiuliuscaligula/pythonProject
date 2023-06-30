class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью ручки '{self.title}'.")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью карандаша '{self.title}'.")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью маркера '{self.title}'.")


# Создание экземпляров классов
pen = Pen("Шариковая ручка")
pencil = Pencil("Графитовый карандаш")
handle = Handle("Перманентный маркер")

# Вызов метода draw для каждого экземпляра
pen.draw()
pencil.draw()
handle.draw()
