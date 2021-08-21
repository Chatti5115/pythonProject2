# coding=utf-8
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_info(self):
        print("이름 : ", self.name, "/ 색상 : ", self.color)

car1 = Car("소나타","빨간색")
print(car1.name, "을 구매했습니다")
car1.show_info()