# 클래스 내 정의된 변수
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수
        self.damage = damage # 멤버 변수
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

wraith1 = Unit("레이스", 80, 5)
print("{0}의 공격력은 {1}이다.".format(wraith1.name, wraith1.damage))
# 클래스 외부에서 멤버 변수를 사용하기 위해서는 유닛.변수 형식으로 사용 가능

wraith2 = Unit("클로킹 레이스", 80, 5)
wraith2.clocking = True # 클래스 외부에서 원하는 변수를 확장할 수 있다.

if wraith2.clocking == True:
    print("레이스가 클로킹되었습니다.")