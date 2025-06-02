
import pgzrun
import random
from pygame import Rect

WIDTH = 640
HEIGHT = 480
TITLE = "Dungeon Escape"
TILE_SIZE = 64
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

music.set_volume(0.3)
sounds_enabled = True

hero = Actor("hero_walk1", (TILE_SIZE // 2, TILE_SIZE // 2))
hero.grid_x = 0
hero.grid_y = 0
hero.frame = 0
hero.animation_counter = 0
hero.facing = "right"

goal = Actor("drawknife1", (WIDTH - TILE_SIZE//2, HEIGHT - TILE_SIZE//2))
goal.grid_x = GRID_WIDTH - 1
goal.grid_y = GRID_HEIGHT - 1

enemies = []

class Enemy:
    def __init__(self, grid_x, grid_y):
        self.actor = Actor("enemy_walk1", (grid_x * TILE_SIZE + TILE_SIZE // 2, grid_y * TILE_SIZE + TILE_SIZE // 2))
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.frame = 0
        self.counter = 0
        self.facing = "right"

    def update(self):
        self.counter += 1
        if self.counter % 30 == 0:
            dx = hero.grid_x - self.grid_x
            dy = hero.grid_y - self.grid_y
            if abs(dx) + abs(dy) <= 4:
                move_x = 1 if dx > 0 else -1 if dx < 0 else 0
                move_y = 1 if dy > 0 else -1 if dy < 0 else 0
            else:
                move_x, move_y = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

            new_x = self.grid_x + move_x
            new_y = self.grid_y + move_y
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                self.grid_x = new_x
                self.grid_y = new_y

        self.actor.x = self.grid_x * TILE_SIZE + TILE_SIZE // 2
        self.actor.y = self.grid_y * TILE_SIZE + TILE_SIZE // 2

        self.facing = "left" if hero.grid_x < self.grid_x else "right"
        self.animate()

    def animate(self):
        self.frame = (self.frame + 1) % 2
        if self.facing == "right":
            self.actor.image = f"enemy_walk{self.frame+1}"
        else:
            self.actor.image = f"enemy_walk{self.frame+1}_copia"

def spawn_enemies():
    enemies.clear()
    for _ in range(3):
        x = random.randint(3, GRID_WIDTH - 1)
        y = random.randint(3, GRID_HEIGHT - 1)
        enemies.append(Enemy(x, y))

moving = False
move_dx = 0
move_dy = 0

def update():
    global moving, move_dx, move_dy, menu_mode
    if not menu_mode:
        if not moving:
            if keyboard.left and hero.grid_x > 0:
                move_dx, move_dy = -1, 0
                hero.facing = "left"
                moving = True
            elif keyboard.right and hero.grid_x < GRID_WIDTH - 1:
                move_dx, move_dy = 1, 0
                hero.facing = "right"
                moving = True
            elif keyboard.up and hero.grid_y > 0:
                move_dx, move_dy = 0, -1
                moving = True
            elif keyboard.down and hero.grid_y < GRID_HEIGHT - 1:
                move_dx, move_dy = 0, 1
                moving = True
            if moving and sounds_enabled:
                sounds.footstep00.play()

        if moving:
            hero.frame = (hero.frame + 1) % 2
            if hero.facing == "right":
                hero.image = f"hero_walk{hero.frame+1}"
            else:
                hero.image = f"hero_walk{hero.frame+1}_copia"
            hero.x += move_dx * 4
            hero.y += move_dy * 4
            if abs(hero.x - (hero.grid_x + move_dx) * TILE_SIZE - TILE_SIZE // 2) < 5 and \
               abs(hero.y - (hero.grid_y + move_dy) * TILE_SIZE - TILE_SIZE // 2) < 5:
                hero.grid_x += move_dx
                hero.grid_y += move_dy
                hero.x = hero.grid_x * TILE_SIZE + TILE_SIZE // 2
                hero.y = hero.grid_y * TILE_SIZE + TILE_SIZE // 2
                moving = False

        for e in enemies:
            e.update()

        # Verificar colisão com inimigo
        for e in enemies:
            if hero.grid_x == e.grid_x and hero.grid_y == e.grid_y:
                menu_mode = True
                hero.grid_x, hero.grid_y = 0, 0
                hero.x = hero.grid_x * TILE_SIZE + TILE_SIZE // 2
                hero.y = hero.grid_y * TILE_SIZE + TILE_SIZE // 2
                music.stop()

        # Verificar chegada ao objetivo
        if hero.grid_x == goal.grid_x and hero.grid_y == goal.grid_y:
            menu_mode = True
            hero.grid_x, hero.grid_y = 0, 0
            hero.x = hero.grid_x * TILE_SIZE + TILE_SIZE // 2
            hero.y = hero.grid_y * TILE_SIZE + TILE_SIZE // 2
            print("YOU WIN!")
            music.stop()

def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("bg", (x * TILE_SIZE, y * TILE_SIZE))

def draw_menu():
    screen.clear()
    screen.fill((0, 0, 50))
    screen.draw.text("Main Menu", center=(WIDTH//2, 80), fontsize=50, color="white")
    screen.draw.filled_rect(buttons[0], "green")
    screen.draw.text("Start Game", center=buttons[0].center, color="white")
    screen.draw.filled_rect(buttons[1], "blue")
    screen.draw.text("Toggle Sound", center=buttons[1].center, color="white")
    screen.draw.filled_rect(buttons[2], "red")
    screen.draw.text("Quit", center=buttons[2].center, color="white")

def draw():
    if menu_mode:
        draw_menu()
    else:
        draw_background()
        goal.draw()
        hero.draw()
        for e in enemies:
            e.actor.draw()

menu_mode = True
buttons = [Rect(220, 150, 200, 50), Rect(220, 220, 200, 50), Rect(220, 290, 200, 50)]

def on_mouse_down(pos):
    global menu_mode, sounds_enabled
    if menu_mode:
        if buttons[0].collidepoint(pos):
            menu_mode = False
            music.play("theme")
            spawn_enemies()
        elif buttons[1].collidepoint(pos):
            sounds_enabled = not sounds_enabled
            if not sounds_enabled:
                music.stop()
            else:
                music.play("theme")
        elif buttons[2].collidepoint(pos):
            exit()

pgzrun.go()
