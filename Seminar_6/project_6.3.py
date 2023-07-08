# Задание 3.
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"  # Приватный атрибут color, изначально установлен в "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("The traffic light is red")
                time.sleep(7)  # Продолжительность состояния "red" - 7 секунд
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("The traffic light is yellow")
                time.sleep(2)  # Продолжительность состояния "yellow" - 2 секунды
                self.__color = "green"
            elif self.__color == "green":
                print("The traffic light is green")
                time.sleep(5)  # Продолжительность состояния "green" - 5 секунд
                self.__color = "red"
            else:
                print("Invalid traffic light color")
                break


# Создание экземпляра класса TrafficLight
traffic_light = TrafficLight()

# Запуск светофора
traffic_light.running()
