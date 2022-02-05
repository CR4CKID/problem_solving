import pygame 
import os
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("CRACKID Pang")


# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character_center.png"))
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height - stage_height

character_l = pygame.image.load(os.path.join(image_path, "characterleft.png"))
character_right = pygame.image.load(os.path.join(image_path, "characterright.png"))
character_center = pygame.image.load(os.path.join(image_path, "character_center.png"))
# 캐릭터 이동 방향
chracter_to_x_left, chracter_to_x_right = 0, 0
character_to_x = 0
# 캐릭터 이동 속도
chracter_speed = 1

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon4.png"))
weapon_size = weapon.get_rect().size
weapon_width, weapon_height = weapon_size[0], weapon_size[1]
re = True


# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character_center.png"))
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height - stage_height

character_l = pygame.image.load(os.path.join(image_path, "characterleft.png"))
character_right = pygame.image.load(os.path.join(image_path, "characterright.png"))
character_center = pygame.image.load(os.path.join(image_path, "character_center.png"))

# 캐릭터 이동 방향
chracter_to_x = 0

# 캐릭터 이동 속도
chracter_speed = 0.5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon4.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 공 만들기 (4개 크기에 대하여 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "monster1.png")),
    pygame.image.load(os.path.join(image_path, "monster2.png")),
    pygame.image.load(os.path.join(image_path, "monster3.png")),
    pygame.image.load(os.path.join(image_path, "monster4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-10,-9,-8,-7] # index 0,1,2,3에 해당

# 사라질 무기와 공 정보
weapon_to_remove = -1
ball_to_remove = -1


game_font = pygame.font.Font(None, 40)
total_time = 100

weapon_speed = 10
stage_num = 1
ball_speed = 0.2

while re:
    start_ticks = pygame.time.get_ticks()
    game_result = "Game Over"
    weapons = []
    stage_font = "STAGE {0}".format(stage_num)
    balls = []
    
    balls.append({
        "pos_x" : 50, # 공의 x 좌표
        "pos_y" : 50, # 공의 y 좌표
        "img_idx" : 0, # 공의 이미지 인덱스
        "to_x" : 3, # 공의 x축 이동방향
        "to_y" : -6, # 공의 y축 이동방향
        "init_spd_y" : ball_speed_y[0]}) # y축 최초속도

    running = True # 게임이 진행중인가?
    while running:

        dt = clock.tick(60) # 게임 화면의 초당 프레임 수

        # 2. 이벤트 처리(키보드, 마우스 등)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
                re = False
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    chracter_to_x_left -= chracter_speed
                    character = character_l
                elif event.key == pygame.K_RIGHT:
                    chracter_to_x_right += chracter_speed
                    character = character_right
                elif event.key == pygame.K_SPACE:
                    weapon_xpos = character_xpos + (character_width / 2) -(weapon_width / 2)
                    weapon_ypos = character_ypos
                    weapons.append([weapon_xpos, weapon_ypos])
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    chracter_to_x_left = 0
                    character = character_center
                elif event.key == pygame.K_RIGHT:
                    chracter_to_x_right = 0
                    character = character_center
        
       
                    
        
        # 3. 게임 캐릭터 위치 정의
        character_xpos += (chracter_to_x_left + chracter_to_x_right) * dt
        if character_xpos > screen_width - character_width:
            character_xpos = screen_width - character_width
        elif character_xpos < 0:
            character_xpos = 0

        # 무기 위치 조정
        weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

        # 천장에 닿은 무기 없애기
        weapons = [[w[0], w[1]] for w in weapons if w[1] >= weapon_height * -1]

        # 공 위치 정의
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]

            ball_size = ball_images[ball_img_idx].get_rect().size
            ball_width, ball_height = ball_size[0], ball_size[1]

            # 가로 위치
            if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1 # 벽에 충돌 시 반대방향으로 튕기게 함
            # 세로 위치
            if ball_pos_y >= screen_height - stage_height - ball_height:
                ball_val["to_y"] = ball_val["init_spd_y"]
            elif ball_pos_y < 0:
                ball_pos_y = 0
                ball_val["to_y"] = (ball_val["to_y"]) * -1
            else:
                ball_val["to_y"] += ball_speed

            ball_val["pos_x"] += ball_val["to_x"] 
            ball_val["pos_y"] += ball_val["to_y"]

        # 4. 충돌 처리
        
        # 캐릭터 rect
        character_rect = character.get_rect()
        character_rect.left = character_xpos
        character_rect.top = character_ypos

        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]

            # 공 rect
            ball_rect = ball_images[ball_img_idx].get_rect()
            ball_rect.left = ball_pos_x
            ball_rect.top = ball_pos_y

            # 공과 캐릭터 충돌 처리
            if character_rect.colliderect(ball_rect):
                running = False
                break
            
            # 무기 rect
            for weapon_idx, weapon_val in enumerate(weapons):
                weapon_xpos, weapon_ypos = weapon_val[0], weapon_val[1]

                weapon_rect = weapon.get_rect()
                weapon_rect.left = weapon_xpos
                weapon_rect.top = weapon_ypos

                # 무기 공 충돌 체크
                if weapon_rect.colliderect(ball_rect):
                    weapon_to_remove = weapon_idx
                    ball_to_remove = ball_idx
                    
                    # 가장 작은 공이 아닐경우 공 쪼개기
                    if ball_img_idx < 3:
                        
                        # 현재 공 크기 정보
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1]

                        # 나눠진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width, small_ball_height = small_ball_rect.size[0], small_ball_rect.size[1]

                        # 왼쪽으로 튕겨나가는 작은 공
                        balls.append({
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                            "img_idx" : ball_img_idx + 1,# 공의 이미지 인덱스
                            "to_x" : -3, # 공의 x축 이동방향, -는 왼쪽
                            "to_y" : -6, # 공의 y축 이동방향
                            "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # y축 최초속도
                        
                        # 오른쪽으로 튕겨나가는 작은 공a
                        balls.append({
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                            "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                            "to_x" : 3, # 공의 x축 이동방향, -는 왼쪽
                            "to_y" : -6, # 공의 y축 이동방향
                            "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # y축 최초속도
                    break
            else:
                continue
            break  
        # 충돌된 공 or 무기 없애기
        if ball_to_remove > -1:
            del balls[ball_to_remove]
            ball_to_remove = -1
        
        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1

        # 모든 공을 없앤 경우 게임 종료
        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False
            stage_num += 1
            ball_speed += 0.2
            ball_speed_y = list(x * 1.3 for x in ball_speed_y)

        # 5. 화면에 그리기 
        screen.blit(background, (0,0))
        for weapon_xpos, weapon_ypos in weapons: # 순서대로 화면에 그려짐
            screen.blit(weapon, (weapon_xpos, weapon_ypos))
        
        for idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
        
        screen.blit(stage, (0, screen_height - stage_height))
        screen.blit(character, (character_xpos, character_ypos))
        
        # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) /  1000 # ms -> s
        timer = game_font.render("Time: {0}".format(int(total_time - elapsed_time)), True, (255,255,255))
        screen.blit(timer, (10,10))
        
        smsg = game_font.render(stage_font, True, (255,255,0))
        smsg_rect = smsg.get_rect().size

        screen.blit(smsg, (screen_width- 10 - smsg_rect[0],10))
        
        # 시간 초과 시
        if total_time - elapsed_time <= 0:
            game_result = "Time Over"
            running = False
        
        
        pygame.display.update()

    if re == False:
        break
    

    # 게임 오버 메시지
    msg = game_font.render(game_result, True, (255,255, 0))
    msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
    screen.blit(msg, (msg_rect))
    pygame.display.update()

    
    pygame.time.delay(1000)


pygame.quit()