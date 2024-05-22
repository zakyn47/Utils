import pygame
import random

# init pygame
pygame.init()

# Create a display surface
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# name window
pygame.display.set_caption("")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)



font = pygame.font.Font(None, 36)
credit = 1000
symbols = ["7", "Bell", "Bar", "Cherry", "Orange", "Plum", "Melon", "Lemon", "Star"]
reels = [random.choice(symbols) for _ in range(9)]
spin = False
spin_start_time = None

def draw_grid():
    current_time = pygame.time.get_ticks()
    for i in range(3):
        for j in range(3):
            if spin_start_time is not None and current_time - spin_start_time < 1000:
                y_offset = (current_time - spin_start_time) * (DISPLAY_HEIGHT//3) // 1000
            else:
                y_offset = 0
            text = font.render(reels[j*3+i], True, BLACK, WHITE)
            win.blit(text, (DISPLAY_WIDTH//3 * i + 100, DISPLAY_HEIGHT//3 * j + 50 - y_offset))

def draw_spin_button():
    pygame.draw.circle(win, BLUE, (DISPLAY_WIDTH//2, DISPLAY_HEIGHT - 75), 50)
    text = font.render("SPIN", True, WHITE)
    win.blit(text, (DISPLAY_WIDTH//2 - text.get_width()//2, DISPLAY_HEIGHT - 100))

def draw_credits():
    text = font.render("Credits: " + str(credit), True, RED)
    win.blit(text, (10, 10))

def handle_spin():
    global spin, spin_start_time
    mouse = pygame.mouse.get_pos()
    if DISPLAY_WIDTH//2 - 50 < mouse[0] < DISPLAY_WIDTH//2 + 50 and DISPLAY_HEIGHT - 125 < mouse[1] < DISPLAY_HEIGHT - 25:
        spin = True
        spin_start_time = pygame.time.get_ticks()

def update_reels():
    global reels, spin, credit, spin_start_time
    if spin and pygame.time.get_ticks() - spin_start_time > 1000:
        reels = [random.choice(symbols) for _ in range(9)]
        credit -= 10
        spin = False
        spin_start_time = None

def check_win():
    global reels, credit
    for i in range(3):
        if reels[i] == reels[i+3] == reels[i+6]:  # check vertical matches
            return True
        if reels[i*3] == reels[i*3+1] == reels[i*3+2]:  # check horizontal matches
            return True
    return False

def draw_win():
    text = font.render("WIN", True, BLUE, WHITE)
    win.blit(text, (DISPLAY_WIDTH//2 - text.get_width()//2, DISPLAY_HEIGHT//2 - text.get_height()//2))

#game loop 
running = True
while running:
    win.fill(WHITE)

    draw_grid()
    draw_spin_button()
    draw_credits()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_spin()

    update_reels()
    if check_win():
        draw_win()

    pygame.display.update()
    pygame.time.delay(99)

pygame.quit()
