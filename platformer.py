import pygame
import random
import math

"""
Plateformer Par Adil et Tom

Aide de Github Copilot, AMAZON Q Chat
V 3.2

1.0 - Ajout d'un cube
1.1 - Deplacement du cube
2.0 - Ajout d'un obstacle
2.1/2 - Collision avec obstacle
2.3 - Génération des obstacle
3.0 - Ajout d'un background
3.1 - Changement du sens d'affichage des éléments sur la fentres
3.2 - Mouvement background
4.0 - Ecran de mort
--------------------------
5.0 - Texturisation

"""

# Initialisation de pygame
pygame.init()

# Titre de la fenetre
pygame.display.set_caption("Plateformer (V4.0)")

# Dimensions de la fenetre
WIDTH, HEIGHT = 1700, 980
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Chargement du background
bg = pygame.image.load("background.png").convert()
scroll = 0
tiles = math.ceil(1500 / bg.get_width()) + 1

# Definition des couleurs
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Propriétés du cube
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_vel_x = 0
player_vel_y = 0
GRAVITY = 0.8
JUMP_VELOCITY = -20
JUMP_HEIGHT = 50
is_jumping = False

# Propriétés des obstacles
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 10, 10
obstacles = []
OBSTACLE_SPEED = 6
OBSTACLE_SPAWN_RATE = 200

# Servir plus tard pour changer le nombre de tick sur lequel le jeu tourne
clock = pygame.time.Clock()

running = True
obstacle_spawn_counter = 0

#Compteur de frame pour le score finale
frames = 0

#Fonction de mort 
def mort():
    global alive
    alive = False
    police = pygame.font.SysFont('Arial', 200)
    texte = police.render('MORT', True, RED)
    window.blit(texte, (600,300))
    police2 = pygame.font.SysFont('Arial', 100)
    texte2 = police2.render(f'Score: {frames}', True, RED)
    window.blit(texte2, (600,500))

#Chargement de guigs
player_img = pygame.image.load("playerrun.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH + 75, PLAYER_HEIGHT + 125))

player_img2 = pygame.image.load("playerjump.png").convert_alpha()
player_img2 = pygame.transform.scale(player_img, (PLAYER_WIDTH + 75, PLAYER_HEIGHT + 125))
alive = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_jumping:
                    player_vel_y = JUMP_VELOCITY
                    is_jumping = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_vel_x = 0

    # Ajoute la "gravité" au cube pour simuler une gravité
    player_vel_y += GRAVITY

    # Mise à jour de la position du cube
    player_x += player_vel_x
    player_y += player_vel_y

    # Vérifié si le cube est en dessous du sol
    if player_y >= HEIGHT - PLAYER_HEIGHT - 130:
        player_y = HEIGHT - PLAYER_HEIGHT - 130
        player_vel_y = 0
        is_jumping = False

    # Généré un nouvel obstacle au hasard
    obstacle_spawn_counter += 1
    if obstacle_spawn_counter >= OBSTACLE_SPAWN_RATE:
        obstacle_spawn_counter = 0
        obstacle_height = random.choice([50, 100])
        obstacle_width = random.choice([50, 100])
        if obstacle_height == 100:
            obstacle = pygame.Rect(1650, 750, obstacle_width, obstacle_height)
        else:
            obstacle = pygame.Rect(1650, 800, obstacle_width, obstacle_height)
        obstacles.append(obstacle)

    # Bouge les obstacles
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED
        if obstacle.x < -OBSTACLE_WIDTH:
            obstacles.remove(obstacle)

    # Vérifie si le joueur se cogne à un obstacle
    for obstacle in obstacles:
        if obstacle.colliderect((player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)):
            player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
            player_center = player_rect.center
            obstacle_center = obstacle.center

            dx = player_center[0] - obstacle_center[0]
            dy = player_center[1] - obstacle_center[1]

            if abs(dx) > abs(dy):
                if dx > 0:
                    player_x = obstacle.right
                else:
                    player_x = obstacle.left - PLAYER_WIDTH
            else:
                if dy > 0:
                    player_y = obstacle.bottom
                else:
                    player_y = obstacle.top - PLAYER_HEIGHT


    window.fill(BLACK, (0, 0, WIDTH, HEIGHT))
    i = 0
    while(i < tiles):
        window.blit(bg, (bg.get_width()*i
                         + scroll, 0))
        i += 1
    scroll -= 6
  
    if abs(scroll) > bg.get_width():
        scroll = 1
    # Dessiner le joueur
    if is_jumping:
        window.blit(player_img2, (player_x, player_y - 120))
    else:
        window.blit(player_img, (player_x, player_y - 120))

    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(window, BLUE, obstacle)

    #Afficher un écran de mort
    if player_x < -15:
        mort()

    if alive: 
        frames += 1
    
    # A modifier pour afficher le score en haut a gauche
    police = pygame.font.SysFont('Arial', 20)
    texte = police.render(f'{frames}', True, RED)
    window.blit(texte, (100,100))

    pygame.display.update()
    clock.tick(100)

pygame.quit()
