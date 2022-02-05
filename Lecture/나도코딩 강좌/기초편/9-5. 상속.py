class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 같은 멤버 변수를 가질 시 상속을 활용할 수 있다.
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        print(self.name, self.hp, self.damage)

firebat1 = AttackUnit("파이어뱃", 50, 16)
