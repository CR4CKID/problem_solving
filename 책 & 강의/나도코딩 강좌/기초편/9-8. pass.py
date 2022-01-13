# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 함수가 다 완성되지 않더라도 일단은 넘김

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")