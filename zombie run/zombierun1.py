import pgzrun
import random
from pgzhelper import *
from pygame import Rect

# Game screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
Black = (0, 0, 0)
Brown = (71, 34, 18)
Red = (212, 47, 47)
White = (255, 255, 255)

# Game state
menu_active = True
music_on = True
score = 0
game_over = False

# Moon
moon = Actor('moon', (700, 80))
moon.scale = 0.3

# Bats
bat = Actor('bat1', (900, 100))
bat.scale = 0.1
bat.images = ['bat1', 'bat2', 'bat3', 'bat4']
bat.fps = 10

# Zombie
zombie = Actor('walk1', (100, 470))
zombie.images = ['walk1', 'walk2', 'walk3', 'walk4', 'walk5', 'walk6', 'walk7', 'walk8', 'walk9', 'walk10']
zombie.fps = 30

# Ghost
ghost = Actor('ghost', (random.randint(800, 1200), random.randint(250, 350)))

# Obstacles (spikes)
obstacles = []  # List that will hold the spikes
obstacles_timeout = 0  # Counter to control the spike generation rate

velocity = 0  # Velocity of the zombie
gravity = 1

# Buttons
start_button = Rect(300, 200, 200, 50)
music_button = Rect(300, 300, 200, 50)
exit_button = Rect(300, 400, 200, 50)
restart_button = Rect(300, 400, 200, 50)  # Restart button for game over screen

def start_game():
    global menu_active, score, game_over, obstacles, zombie
    menu_active = False
    score = 0
    game_over = False
    obstacles = []
    zombie.pos = (100, 470)
    if music_on:
        music.play('music')

def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        music.play('music')
    else:
        music.stop()

def exit_game():
    quit()

def restart_game():
    global menu_active, score, game_over, obstacles, zombie
    game_over = False
    score = 0
    obstacles = []
    zombie.pos = (100, 470)
    if music_on:
        music.play('music')

def update():
    global velocity, score, obstacles_timeout, game_over

    if menu_active or game_over:
        return

    # Zombie animation
    zombie.animate()

    # Jump
    if keyboard.up and zombie.y == 470:
        velocity = -18

    zombie.y += velocity
    velocity += gravity

    # Stop the zombie from falling off the screen
    if zombie.y > 470:
        velocity = 0
        zombie.y = 470

    # Bat movement
    bat.animate()
    bat.x -= 3
    if bat.x < -50:
        bat.x = random.randint(1000, 1500)
        bat.y = random.randint(100, 250)

    # Ghost movement
    ghost.x -= 5
    if ghost.x < -50:
        ghost.x = random.randint(900, 5000)
        ghost.y = random.randint(250, 350)

    # Collision with ghost
    if zombie.colliderect(ghost):
        sounds.collect.play()
        ghost.x = random.randint(900, 5000)
        ghost.y = random.randint(250, 350)
        score += 5

    #### SPIKES ####
    obstacles_timeout += 1
    if obstacles_timeout >= 100:  # Generate spikes every 100 frames
        spike = Actor('spike', (random.randint(800, 1000), 470))  # Position on the ground
        spike.scale = 0.3
        obstacles.append(spike)
        obstacles_timeout = 0

    # Move spikes across the screen
    for spike in obstacles[:]:
        spike.x -= 8
        if spike.x < -50:
            obstacles.remove(spike)
            score += 1

        if zombie.colliderect(spike):
            game_over = True
            sounds.gameover.play()

def draw():
    screen.clear()
    if menu_active:
        screen.draw.text('Zombie Run', center=(WIDTH//2, 100), color=White, fontname='creepster', fontsize=60)
        screen.draw.filled_rect(start_button, Red)
        screen.draw.text('Start Game', center=start_button.center, color=White, fontname='creepster', fontsize=30)
        screen.draw.filled_rect(music_button, Red)
        screen.draw.text('Toggle Music', center=music_button.center, color=White, fontname='creepster', fontsize=30)
        screen.draw.filled_rect(exit_button, Red)
        screen.draw.text('Exit', center=exit_button.center, color=White, fontname='creepster', fontsize=30)
    elif game_over:
        screen.draw.text('Game Over', center=(WIDTH//2, 150), color=Red, fontname='creepster', fontsize=80)
        screen.draw.text(f'Score: {score}', center=(WIDTH//2, 300), color=White, fontname='creepster', fontsize=60)
        music.stop()

        # Draw the restart button
        screen.draw.filled_rect(restart_button, Red)
        screen.draw.text('Restart', center=restart_button.center, color=White, fontname='creepster', fontsize=30)
    else:
        screen.draw.filled_rect(Rect(0, 0, 800, 500), Black)  # Sky
        screen.draw.filled_rect(Rect(0, 500, 800, 100), Brown)  # Ground
        moon.draw()
        bat.draw()
        zombie.draw()
        ghost.draw()
        screen.draw.text(f'Score: {score}', (20, 20), color=Red, fontname='creepster', fontsize=30)
        for spike in obstacles:
            spike.draw()

def on_mouse_down(pos):
    if menu_active:
        if start_button.collidepoint(pos):
            start_game()
        elif music_button.collidepoint(pos):
            toggle_music()
        elif exit_button.collidepoint(pos):
            exit_game()
    elif game_over:
        if restart_button.collidepoint(pos):
            restart_game()

# Play music when the game starts (on the main menu)
if music_on:
    music.play('music')

game = pgzrun.go()

