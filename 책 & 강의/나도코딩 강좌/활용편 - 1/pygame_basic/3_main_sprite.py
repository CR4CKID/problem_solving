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

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\CRACKID\\\
Desktop\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해줌
character_width, character_height = character_size[0], character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
# 화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 시
            running = False

    screen.blit(background, (0,0)) # blit을 통해 배경을 실제로 그릴 수 있다
    
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() # pygame에서는 매 프레임 화면을 불러와야 한다

# pygame 종료
pygame.quit()