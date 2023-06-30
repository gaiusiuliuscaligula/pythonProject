class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости! Снизьте скорость.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости! Снизьте скорость.")


class PoliceCar(Car):
    pass


# Создание экземпляров классов
town_car = TownCar(70, "Серый", "Городская машина")
sport_car = SportCar(100, "Красный", "Спортивная машина")
work_car = WorkCar(50, "Желтый", "Рабочая машина")
police_car = PoliceCar(80, "Синий", "Полицейская машина", is_police=True)

# Получение значений атрибутов
print(f"Атрибуты Городской машины: Скорость - {town_car.speed}, Цвет - {town_car.color}, Имя - {town_car.name}, "
      f"Полицейская - {town_car.is_police}")
print(f"Атрибуты Спортивной машины: Скорость - {sport_car.speed}, Цвет - {sport_car.color}, Имя - {sport_car.name}, "
      f"Полицейская - {sport_car.is_police}")
print(f"Атрибуты Рабочей машины: Скорость - {work_car.speed}, Цвет - {work_car.color}, Имя - {work_car.name}, "
      f"Полицейская - {work_car.is_police}")
print(f"Атрибуты Полицейской машины: Скорость - {police_car.speed}, Цвет - {police_car.color}, Имя - {police_car.name}, "
      f"Полицейская - {police_car.is_police}")

# Вызов методов
town_car.go()
town_car.turn("налево")
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.turn("направо")
sport_car.show_speed()
sport_car.stop()

work_car.go()
work_car.turn("направо")
work_car.show_speed()
work_car.stop()

police_car.go()
police_car.turn("направо")
police_car.show_speed()
police_car.stop()
