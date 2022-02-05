# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("현재 체력은 {0}입니다.".format(self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("현재 체력은 {0}입니다.".format(self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            self.speed += 1
            self.damage += 5
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다.".format(self.name))

# 탱크 클래스
class Tank(AttackUnit):
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seizemode = False

    def set_seizemode(self):
        if Tank.seize_developed == False:
            return
        
        # 시즈모드가 아닐때
        if self.seizemode == False:
            self.seizemode = True
            self.damage *= 2
            self.speed = 0
            print("{0} : 시즈모드가 활성화되었습니다.".format(self.name))
        # 시즈모드일떄
        else:
            self.seizemode = False
            self.damage /= 2
            self.speed = 1
            print("{0} : 시즈모드가 비활성화되었습니다.".format(self.name))
        
# 공중 유닛
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(self.name, location, self.flying_speed))

# 공중 공격 유닛
class flyable_attackunit(AttackUnit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0 , damage) # 지상 스피드는 0으로 처리
        flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(location)

class Wraith(flyable_attackunit):
    def __init__(self):
        flyable_attackunit.__init__(self, "레이스", 80, 20, 5)
        self.cloack = False

    def cloacking(self):
        if self.cloack == False:
            self.cloack = True
            print("{0} : 클로킹 모드가 활성화되었습니다.".format(self.name))
        else:
            self.cloack = False
            print("{0} : 클로킹 모드가 비활성화되었습니다.".format(self.name))

def game_start():
    print("[알림] 게임이 시작되었습니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일관 관리
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동
for unit in attack_unit:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드가 개발되었습니다.")

# 공격모드 준비, isinstance를 사용하여 특정 인스턴스가 클래스 내에 있는지 확인할 수 있다.
for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seizemode()
    elif isinstance(unit, Wraith):
        unit.cloacking()

# 전군 공격
for unit in attack_unit:
    unit.attack("1시")

# 전군 피해
from random import *
for unit in attack_unit:
    unit.damaged(randint(5, 100))

# 게임 종료
game_over()