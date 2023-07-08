# Задание 4.
# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length  # Защищенный атрибут length
        self._width = width  # Защищенный атрибут width

    def calculate_asphalt_mass(self, asphalt_mass_per_sqm, thickness):
        area = self._length * self._width
        asphalt_mass = area * asphalt_mass_per_sqm * thickness
        return asphalt_mass

# Создание экземпляра класса Road
road = Road(20, 5000)

# Расчет массы асфальта для покрытия дорожного полотна
asphalt_mass_per_sqm = 25  # Масса асфальта для покрытия одного квадратного метра дороги
thickness = 5  # Толщина полотна в сантиметрах
total_asphalt_mass = road.calculate_asphalt_mass(asphalt_mass_per_sqm, thickness)

# Вывод результата
print(f"Масса асфальта, необходимого для покрытия дорожного полотна: {total_asphalt_mass} тонн")
