# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))

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

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp ,0)
        super().__init__(name, hp, 0) # super() 사용 시 self는 붙이면 안됨
        self.location
        

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


