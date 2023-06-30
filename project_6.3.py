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
