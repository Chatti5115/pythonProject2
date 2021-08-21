# coding=utf-8
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def atttack(self):
        print(self.name, "이가 공격을 수행합니다. [전투력 : ", self.power,"]")

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스텨 이름 : ", self.name, "/ 몬스터 종류 : ", self.type)

monster = Monster("슬라임", 10, "초급")
monster.show_info()
monster.atttack()


# 클래스 생성자
#__init__
# 클래스 소멸자
#__del__