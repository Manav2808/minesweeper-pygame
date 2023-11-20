import pygame
import random as rd

pygame.font.init()

screen = pygame.display.set_mode((1366, 768))

# Main Menu
TITLE_FONT = pygame.font.SysFont("leelawadee", 95)
BUTTON_FONT = pygame.font.SysFont("consolas", 85)

TITLE = TITLE_FONT.render("MINE-SWEEPER", True, (255, 200, 150))
TITLE_RECT = TITLE.get_rect(center=(683, 100))

PLAY_BUTTON = BUTTON_FONT.render("PLAY", True, (0, 50, 255))
PLAY_BUTTON_RECT = PLAY_BUTTON.get_rect(center=(100, 620))
EXIT_BUTTON = BUTTON_FONT.render("EXIT", True, (0, 50, 255))
EXIT_BUTTON_RECT = EXIT_BUTTON.get_rect(center=(100, 720))

# Game Info
flags = 35

INFO_FONT = pygame.font.SysFont("cambria", 45)
HELP_FONT = pygame.font.SysFont("calibri", 28)
GAME_END_FONT = pygame.font.SysFont("consolas", 200)
SCORE_FONT = pygame.font.SysFont("consolas", 80)

RETRY_BUTTON = INFO_FONT.render("RETRY", True, (0, 0, 255))
RETRY_BUTTON_RECT = RETRY_BUTTON.get_rect(center=(205, 725))

QUIT_BUTTON = INFO_FONT.render("QUIT", True, (255, 50, 0))
QUIT_BUTTON_RECT = QUIT_BUTTON.get_rect(center=(65, 725))

DESTROY_TEXT = HELP_FONT.render("LMB: Destroys the Grass", True, (0, 0, 0))
DESTROY_TEXT_RECT = DESTROY_TEXT.get_rect(topleft=(15, 310))

PUT_FLAG_TEXT = HELP_FONT.render("RMB: Put/Remove Flag on Grass", True, (0, 0, 0))
PUT_FLAG_TEXT_RECT = PUT_FLAG_TEXT.get_rect(topleft=(15, 350))

GAME_OVER_TEXT = GAME_END_FONT.render("GAME OVER", True, (255, 255, 0))
GAME_OVER_TEXT_RECT = GAME_OVER_TEXT.get_rect(center=(683, 384))

GAME_WON_TEXT = GAME_END_FONT.render("YOU WON", True, (255, 255, 0))
GAME_WON_TEXT_RECT = GAME_WON_TEXT.get_rect(center=(683, 384))

# Game
position_grid = [
    [
        (390, 15),
        (452, 15),
        (514, 15),
        (576, 15),
        (638, 15),
        (700, 15),
        (762, 15),
        (824, 15),
        (886, 15),
        (948, 15),
        (1010, 15),
        (1072, 15),
        (1134, 15),
        (1196, 15),
        (1258, 15),
    ],
    [
        (390, 77),
        (452, 77),
        (514, 77),
        (576, 77),
        (638, 77),
        (700, 77),
        (762, 77),
        (824, 77),
        (886, 77),
        (948, 77),
        (1010, 77),
        (1072, 77),
        (1134, 77),
        (1196, 77),
        (1258, 77),
    ],
    [
        (390, 139),
        (452, 139),
        (514, 139),
        (576, 139),
        (638, 139),
        (700, 139),
        (762, 139),
        (824, 139),
        (886, 139),
        (948, 139),
        (1010, 139),
        (1072, 139),
        (1134, 139),
        (1196, 139),
        (1258, 139),
    ],
    [
        (390, 201),
        (452, 201),
        (514, 201),
        (576, 201),
        (638, 201),
        (700, 201),
        (762, 201),
        (824, 201),
        (886, 201),
        (948, 201),
        (1010, 201),
        (1072, 201),
        (1134, 201),
        (1196, 201),
        (1258, 201),
    ],
    [
        (390, 263),
        (452, 263),
        (514, 263),
        (576, 263),
        (638, 263),
        (700, 263),
        (762, 263),
        (824, 263),
        (886, 263),
        (948, 263),
        (1010, 263),
        (1072, 263),
        (1134, 263),
        (1196, 263),
        (1258, 263),
    ],
    [
        (390, 325),
        (452, 325),
        (514, 325),
        (576, 325),
        (638, 325),
        (700, 325),
        (762, 325),
        (824, 325),
        (886, 325),
        (948, 325),
        (1010, 325),
        (1072, 325),
        (1134, 325),
        (1196, 325),
        (1258, 325),
    ],
    [
        (390, 387),
        (452, 387),
        (514, 387),
        (576, 387),
        (638, 387),
        (700, 387),
        (762, 387),
        (824, 387),
        (886, 387),
        (948, 387),
        (1010, 387),
        (1072, 387),
        (1134, 387),
        (1196, 387),
        (1258, 387),
    ],
    [
        (390, 449),
        (452, 449),
        (514, 449),
        (576, 449),
        (638, 449),
        (700, 449),
        (762, 449),
        (824, 449),
        (886, 449),
        (948, 449),
        (1010, 449),
        (1072, 449),
        (1134, 449),
        (1196, 449),
        (1258, 449),
    ],
    [
        (390, 511),
        (452, 511),
        (514, 511),
        (576, 511),
        (638, 511),
        (700, 511),
        (762, 511),
        (824, 511),
        (886, 511),
        (948, 511),
        (1010, 511),
        (1072, 511),
        (1134, 511),
        (1196, 511),
        (1258, 511),
    ],
    [
        (390, 573),
        (452, 573),
        (514, 573),
        (576, 573),
        (638, 573),
        (700, 573),
        (762, 573),
        (824, 573),
        (886, 573),
        (948, 573),
        (1010, 573),
        (1072, 573),
        (1134, 573),
        (1196, 573),
        (1258, 573),
    ],
    [
        (390, 635),
        (452, 635),
        (514, 635),
        (576, 635),
        (638, 635),
        (700, 635),
        (762, 635),
        (824, 635),
        (886, 635),
        (948, 635),
        (1010, 635),
        (1072, 635),
        (1134, 635),
        (1196, 635),
        (1258, 635),
    ],
    [
        (390, 697),
        (452, 697),
        (514, 697),
        (576, 697),
        (638, 697),
        (700, 697),
        (762, 697),
        (824, 697),
        (886, 697),
        (948, 697),
        (1010, 697),
        (1072, 697),
        (1134, 697),
        (1196, 697),
        (1258, 697),
    ],
]

grass_grid = []

grass_pos_grid = [
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
]

bomb_grid = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]

bombs = 35

game_over = False
game_won = False

NO_GRASS = pygame.image.load("Assets/No_Grass.png").convert_alpha()
BOMB = pygame.image.load("Assets/Bomb.png").convert_alpha()
GRASS = pygame.image.load("Assets/Grass.png").convert_alpha()
FLAG = pygame.image.load("Assets/Flag.png").convert_alpha()


class Grass:
    def __init__(self, position, info, i, j):
        self.image = GRASS
        self.rect = self.image.get_rect(topleft=position)
        self.no_grass_img = NO_GRASS
        self.no_grass_img_rect = self.rect
        self.grid_pos = (i, j)
        self.flagged = False
        self.destroyed = False
        self.bombed = False
        self.empty = True
        self.number = False

        if info == "B":
            self.bomb = BOMB
            self.bomb_rect = self.image.get_rect(
                topleft=(position[0] + 7, position[1] + 6)
            )
            self.bombed = True
            self.empty = False
        elif info == "-":
            pass
        else:
            self.number_img = INFO_FONT.render(str(info), True, (255, 255, 255))
            self.number_rect = self.number_img.get_rect(
                topleft=(position[0] + 17, position[1] + 2)
            )
            self.empty = False
            self.number = True

    def draw(self):
        if self.destroyed:
            if self.number:
                screen.blit(self.no_grass_img, self.rect)
                screen.blit(self.number_img, self.number_rect)
            if self.empty:
                screen.blit(self.no_grass_img, self.no_grass_img_rect)
            if self.bombed:
                screen.blit(self.no_grass_img, self.rect)
                screen.blit(self.bomb, self.bomb_rect)
        else:
            screen.blit(self.image, self.rect)

    def put_flag(self):
        global flags

        if self.flagged == False:
            if flags > 0:
                self.flagged = True
                flags -= 1
        else:
            self.flagged = False
            flags += 1

    def destroy(self):
        self.destroyed = True


def generate_bomb_matrix():
    global bomb_grid
    global bombs

    def check_for_bombs(i, j):
        bomb_count = 0

        if bomb_grid[i][j] != "B":
            if i == 0 and j == 0:
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j + 1] == "B":
                    bomb_count += 1
            if i == 0 and j == 14:
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j - 1] == "B":
                    bomb_count += 1
            if i == 11 and j == 0:
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j + 1] == "B":
                    bomb_count += 1
            if i == 11 and j == 14:
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1
            if i == 0 and j > 0 and j < 14:
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
            if i == 11 and j > 0 and j < 14:
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
            if i > 0 and i < 11 and j == 0:
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
            if i > 0 and i < 11 and j == 14:
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
            if i > 0 and i < 11 and j > 0 and j < 14:
                if bomb_grid[i - 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i - 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j + 1] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j] == "B":
                    bomb_count += 1
                if bomb_grid[i + 1][j - 1] == "B":
                    bomb_count += 1
                if bomb_grid[i][j - 1] == "B":
                    bomb_count += 1

        return bomb_count

    while bombs > 0:
        row = rd.randint(0, 11)
        col = rd.randint(0, 14)
        if bomb_grid[row][col] == "B":
            continue
        else:
            bomb_grid[row][col] = "B"
            bombs -= 1

    for i in range(12):
        for j in range(15):
            bombs = check_for_bombs(i, j)
            if bombs != 0:
                bomb_grid[i][j] = bombs

            grass = Grass(position_grid[i][j], bomb_grid[i][j], i, j)
            grass_grid.append(grass)
            grass_pos_grid[i][j] = grass


def main_menu():
    screen.fill((127, 127, 127))

    screen.blit(TITLE, TITLE_RECT)
    screen.blit(PLAY_BUTTON, PLAY_BUTTON_RECT)
    screen.blit(EXIT_BUTTON, EXIT_BUTTON_RECT)


def game_info(flags):
    screen.fill((127, 127, 127))

    TIME_TEXT = INFO_FONT.render(f"Time:", True, (255, 255, 255))
    TIME_TEXT_RECT = TIME_TEXT.get_rect(center=(70, 30))
    screen.blit(TIME_TEXT, TIME_TEXT_RECT)

    current_time = int(pygame.time.get_ticks() / 1010)
    TIME = INFO_FONT.render(f"{current_time}", True, (255, 255, 255))
    TIME_RECT = TIME.get_rect(center=(170, 30))
    screen.blit(TIME, TIME_RECT)

    FLAGS = INFO_FONT.render(f"Flags: {flags}", True, (255, 255, 255))
    FLAGS_RECT = FLAGS.get_rect(center=(100, 90))
    screen.blit(FLAGS, FLAGS_RECT)

    screen.blit(DESTROY_TEXT, DESTROY_TEXT_RECT)
    screen.blit(PUT_FLAG_TEXT, PUT_FLAG_TEXT_RECT)

    screen.blit(RETRY_BUTTON, RETRY_BUTTON_RECT)
    screen.blit(QUIT_BUTTON, QUIT_BUTTON_RECT)


def draw_grass():
    for grass in grass_grid:
        grass.draw()

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(387, 12, 935, 749), 3)


def draw_flags():
    for grass in grass_grid:
        if grass.flagged:
            screen.blit(FLAG, (grass.rect.x + 10, grass.rect.y + 5))


def game_over_overlay():
    screen.blit(GAME_OVER_TEXT, GAME_OVER_TEXT_RECT)

    pygame.display.update()

    pygame.time.delay(3300)


def game_won_overlay():
    SCORE_TEXT = SCORE_FONT.render(
        f"YOUR SCORE:{int(pygame.time.get_ticks() / 1010)}", True, (255, 255, 0)
    )
    SCORE_TEXT_RECT = SCORE_TEXT.get_rect(center=(683, 484))

    screen.blit(GAME_WON_TEXT, GAME_WON_TEXT_RECT)
    screen.blit(SCORE_TEXT, SCORE_TEXT_RECT)

    pygame.display.update()

    pygame.time.delay(3300)


def check_for_bombs(grass):
    global game_over

    if grass.bombed:
        grass.destroy()

        for grass in grass_grid:
            if grass.bombed:
                grass.destroy()

        game_over = True


def check_for_win():
    global game_won

    grass_counter = 0

    for grass in grass_grid:
        if not grass.bombed and grass.destroyed:
            grass_counter += 1

    if grass_counter == 85:
        game_won = True


def destroy_grass(grass, pos_0, pos_1):
    if pos_0 >= 0 and pos_1 >= 0 and pos_0 <= 11 and pos_1 <= 14:
        grass = grass_pos_grid[pos_0][pos_1]

        if not grass.destroyed and not grass.bombed:
            if grass.number:
                grass.destroy()
                return
            else:
                grass.destroy()
                destroy_grass(grass, grass.grid_pos[0] - 1, grass.grid_pos[1] - 1)
                destroy_grass(grass, grass.grid_pos[0] - 1, grass.grid_pos[1])
                destroy_grass(grass, grass.grid_pos[0] - 1, grass.grid_pos[1] + 1)
                destroy_grass(grass, grass.grid_pos[0], grass.grid_pos[1] + 1)
                destroy_grass(grass, grass.grid_pos[0] + 1, grass.grid_pos[1] + 1)
                destroy_grass(grass, grass.grid_pos[0] + 1, grass.grid_pos[1])
                destroy_grass(grass, grass.grid_pos[0] + 1, grass.grid_pos[1] - 1)
                destroy_grass(grass, grass.grid_pos[0], grass.grid_pos[1] - 1)
    else:
        return


def game_reset():
    global flags
    global game_over
    global game_won

    flags = 35

    if game_over:
        game_over = False

    if game_won:
        game_won = False


def main():
    screen_counter = 1

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_counter == 1:
                    if PLAY_BUTTON_RECT.collidepoint(event.pos):
                        screen_counter = 2
                        generate_bomb_matrix()
                    if EXIT_BUTTON_RECT.collidepoint(event.pos):
                        running = False
                if screen_counter == 2:
                    if RETRY_BUTTON_RECT.collidepoint(event.pos):
                        game_reset()
                        generate_bomb_matrix()
                    if QUIT_BUTTON_RECT.collidepoint(event.pos):
                        running = False

                    for grass in grass_grid:
                        if grass.rect.collidepoint(event.pos):
                            if event.button == 1:
                                check_for_bombs(grass)
                                destroy_grass(
                                    grass, grass.grid_pos[0], grass.grid_pos[1]
                                )
                                check_for_win()
                            elif event.button == 3:
                                if not grass.destroyed:
                                    grass.put_flag()

        if screen_counter == 1:
            main_menu()
        elif screen_counter == 2:
            game_info(flags)
            draw_grass()
            draw_flags()

        if game_over:
            game_over_overlay()
            running = False

        if game_won:
            game_won_overlay()
            running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
