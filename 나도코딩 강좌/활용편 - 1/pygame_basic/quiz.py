import pygame 
from random import randint


###################################################################################
# 기본 과정
pygame.init() # 초기화 작업 (pygame 임포트 시 반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\CRACKID\\Desktop\\\
PythonWorkspace\\pygame_basic\\back1.jpg")
character = pygame.image.load("C:\\Users\\CRACKID\\Desktop\\\
PythonWorkspace\\pygame_basic\\human.png")
poop = pygame.image.load("C:\\Users\\CRACKID\\Desktop\\\
PythonWorkspace\\pygame_basic\\poop2.png")

character_size = character.get_rect().size
character_w, character_h = character_size[0], character_size[1]
character_x = (screen_width / 2) - (character_w / 2)

poop_size = poop.get_rect().size
poop_w, poop_h = poop_size[0], poop_size[1]
poop_x = randint(0, screen_width - poop_w)
poop_y = 0

# 이동 좌표 및 속도
to_x = 0
speed = 1

# 카운터 폰트
game_font = pygame.font.Font(None, 80)
count = 0

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= speed
            elif event.key == pygame.K_d:
                to_x += speed
                    
        if event.type == pygame.KEYUP:
            to_x = 0

    # 3. 게임 캐릭터 위치 정의

    screen.blit(background,(0,0))
    screen.blit(character, (character_x, screen_height - character_h))
    screen.blit(poop, (poop_x, poop_y))
    
    # 카운트가 늘어날 수록 똥이 떨어지는 스피드가 빨라짐
    character_x += to_x * dt
    pspeed = 0.3 * dt
    poop_y += pspeed
    if 10 > count >= 3 :
        poop_y += pspeed * 1.4
    elif 15 > count >= 10 :
        poop_y += pspeed * 1.4
    elif 20 > count >= 15 :
        poop_y += pspeed * 1.4
    elif count >= 20:
        poop_y += pspeed * 1.4

    # 캐릭터가 배경을 벗어나지 않도록 함
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_w:
        character_x = screen_width - character_w

    # 똥이 지나가면 카운트를 하나 세고 다음 똥이 또 떨어짐
    if poop_y > screen_height:
        count += 1
        poop_y = 0
        poop_x = randint(0, screen_width - poop_w)

    # 카운터 표시
    counter = game_font.render(str(count), True, (255,255,255))
    screen.blit(counter, (0,0))
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = screen_height - character_h

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x
    poop_rect.top = poop_y

    if character_rect.colliderect(poop_rect):
        print("충돌했어용")
        running = False
        pygame.time.delay(1000)

    # 5. 화면에 그리기 
    pygame.display.update()

# pygame 종료
pygame.quit()
