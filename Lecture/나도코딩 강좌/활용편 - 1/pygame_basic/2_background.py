import pygame

pygame.init() # 초기화 작업 (pygame 임포트 시 반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("CRACKID")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\CRACKID\\\
Desktop\\PythonWorkspace\\pygame_basic\\background.png")


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 시
            running = False

    screen.blit(background, (0,0)) # blit을 통해 배경을 실제로 그릴 수 있다
    # screen.fill((0, 255, 0)) # fill을 통하여 튜플형태의 RGB값을 전달할 수 있다

    pygame.display.update() # pygame에서는 매 프레임 화면을 불러와야 한다

# pygame 종료
pygame.quit()