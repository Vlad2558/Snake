import pygame
import random

size_x = 20
size_y = 20
pixel_size = 40
Score = 0
max_size = size_x * size_y
Game_Mode = 0
Last_state = ""
Snake = [random.randrange(max_size)]
Apple = random.randrange(max_size)
going = "center"
timer_tick = 0
timer_tick_max = 5
fps = 10 * timer_tick_max
best_score = 0
paused = False


def game_over():
    global Game_Mode
    global Score
    global best_score
    if Score > best_score:
        best_score = Score
    Game_Mode = 2
    global fps
    fps = 10 * timer_tick_max


def New_Game():
    global Game_Mode
    global Snake
    global Score
    global Apple
    global Last_state
    global going
    going = ""
    Last_state = ""
    Game_Mode = 1
    Snake = [(size_y + 1) * (size_x // 2)]  # [random.randrange(max_size)]
    Apple = random.randrange(max_size)
    Score = 0


def Left():
    global Snake
    global Apple
    if (Snake[0] % size_x == 0) or ((Snake[0] - 1) in Snake):
        game_over()
        return
    if Apple == Snake[0] - 1:  # Eating Apple
        global Score
        Score += 1
        global fps
        fps += 1
        Snake.append(0)
        Apple = random.randrange(max_size)
        while Apple in Snake or Apple == Snake[0] - 1:
            Apple = random.randrange(max_size)
    head = Snake[0] - 1
    for each in range(len(Snake) - 1, 0, -1):
        Snake[each] = Snake[each - 1]
    Snake[0] = head


def Right():
    global Snake
    global Apple
    if (Snake[0] % size_x == size_x - 1) or ((Snake[0] + 1) in Snake):
        game_over()
        return
    if Apple == Snake[0] + 1:  # Eating Apple
        global Score
        Score += 1
        global fps
        fps += 1
        Snake.append(0)
        Apple = random.randrange(max_size)
        while Apple in Snake or Apple == Snake[0] + 1:
            Apple = random.randrange(max_size)
    head = Snake[0] + 1
    for each in range(len(Snake) - 1, 0, -1):
        Snake[each] = Snake[each - 1]
    Snake[0] = head


def Up():
    global Snake
    global Apple
    if (Snake[0] < size_x) or ((Snake[0] - size_x) in Snake):
        game_over()
        return
    if Apple == Snake[0] - size_x:  # Eating Apple
        global Score
        Score += 1
        global fps
        fps += 1
        Snake.append(0)
        Apple = random.randrange(max_size)
        while Apple in Snake or Apple == Snake[0] - size_x:
            Apple = random.randrange(max_size)
    head = Snake[0] - size_x
    for each in range(len(Snake) - 1, 0, -1):
        Snake[each] = Snake[each - 1]
    Snake[0] = head


def Down():
    global Snake
    global Apple
    if Snake[0] >= size_x * (size_y - 1) or (Snake[0] + size_x) in Snake:
        game_over()
        return

    if Apple == Snake[0] + size_x:  # Eating Apple
        global Score
        Score += 1
        global fps
        fps += 1
        Snake.append(0)
        Apple = random.randrange(max_size)
        while Apple in Snake or Apple == Snake[0] + size_x:
            Apple = random.randrange(max_size)
    head = Snake[0] + size_x
    for each in range(len(Snake) - 1, 0, -1):
        Snake[each] = Snake[each - 1]
    Snake[0] = head


def Moving(go_to):
    global Last_state
    if go_to == "left":
        if Last_state != "right":
            Left()
            Last_state = go_to
        else:
            Right()
        return
    if go_to == "right":
        if Last_state != "left":
            Right()
            Last_state = go_to
        else:
            Left()
        return
    if go_to == "up":
        if Last_state != "down":
            Up()
            Last_state = go_to
        else:
            Down()
        return
    if go_to == "down":
        if Last_state != "up":
            Down()
            Last_state = go_to
        else:
            Up()
        return


pygame.init()
sc = pygame.display.set_mode([size_x * pixel_size, size_y * pixel_size])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 32, bold=True)
font_press = pygame.font.SysFont('Arial', 20, italic=True)
check_img = False
try:
    img = pygame.image.load('wallpaper.jpg')
    img = pygame.transform.scale(img, (size_x * pixel_size, size_y * pixel_size))
except:
    check_img = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                going = "left"
            if event.key == pygame.K_RIGHT:
                going = "right"
            if event.key == pygame.K_UP:
                going = "up"
            if event.key == pygame.K_DOWN:
                going = "down"
            if event.key == pygame.K_SPACE:
                if Game_Mode != 1:
                    Game_Mode = 1
                    New_Game()
                else:
                    paused = not paused
    if check_img:
        sc.fill(pygame.Color('black'), (0, 0, size_x * pixel_size, size_y * pixel_size))
    else:
        sc.blit(img, (0, 0))
    if Game_Mode == 0:
        render_score = font_score.render('Welcome to Snake', True, pygame.Color('blue'))
        sc.blit(render_score, ((size_x // 2 - 2) * pixel_size, (size_y // 2) * pixel_size))
        render_press = font_press.render('press SPACE to Start', True, pygame.Color('orange'))
        sc.blit(render_press, ((size_x // 2 - 1.5) * pixel_size, (size_y // 2 + 0.5) * pixel_size))

    if Game_Mode == 1:
        for i in Snake:
            if i == Snake[0]:
                pygame.draw.rect(sc, pygame.Color('orange'),
                                 pygame.Rect((i % size_x) * pixel_size, (i // size_y) * pixel_size, pixel_size,
                                             pixel_size))
            elif i == Snake[-1]:
                pygame.draw.rect(sc, pygame.Color('white'),
                                 pygame.Rect((i % size_x) * pixel_size, (i // size_y) * pixel_size, pixel_size,
                                             pixel_size))
            else:
                pygame.draw.rect(sc, pygame.Color('yellow'),
                                 pygame.Rect((i % size_x) * pixel_size, (i // size_y) * pixel_size, pixel_size,
                                             pixel_size))
            pygame.draw.rect(sc, pygame.Color('red'),
                             pygame.Rect((i % size_x) * pixel_size, (i // size_y) * pixel_size, pixel_size, pixel_size),
                             2)

        pygame.draw.circle(sc, pygame.Color('red'),
                           ((Apple % size_x) * pixel_size + pixel_size // 2,
                            (Apple // size_y) * pixel_size + pixel_size // 2),
                           pixel_size // 2)
        pygame.draw.circle(sc, pygame.Color('green'),
                           ((Apple % size_x) * pixel_size + pixel_size // 2,
                            (Apple // size_y) * pixel_size + pixel_size // 2),
                           pixel_size // 2, 4)
        render_score = font_score.render(f'SCORE:{Score}', True, pygame.Color('green'))
        sc.blit(render_score, (0, (size_y - 1) * pixel_size))
        if timer_tick == timer_tick_max:
            if not paused:
                Moving(going)
            timer_tick = 0
        else:
            timer_tick += 1
        if paused:
            render_score = font_score.render("PAUSE", True, pygame.Color('green'))
            sc.blit(render_score, ((size_x // 2 - 1) * pixel_size, (size_y // 2 - 1) * pixel_size))
    if Game_Mode == 2:
        render_score = font_score.render(f'GAME OVER!SCORE: {Score}', True, pygame.Color('red'))
        sc.blit(render_score, ((size_x // 2 - 2) * pixel_size, (size_y // 2) * pixel_size))
        render_score = font_score.render(f'BEST SCORE: {best_score}', True, pygame.Color('red'))
        sc.blit(render_score, ((size_x // 2 - 2) * pixel_size, (size_y // 2 + 0.5) * pixel_size))
        render_press = font_press.render('press SPACE to Start', True, pygame.Color('orange'))
        sc.blit(render_press, ((size_x // 2 - 1.5) * pixel_size, (size_y // 2 + 1) * pixel_size))

    clock.tick(fps)
    pygame.display.flip()
