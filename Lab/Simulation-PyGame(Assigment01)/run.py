import pygame
from agent import Agent
from environment import Environment

pygame.init()

width, height = 600, 400
environment = Environment(width, height)
agent = Agent("Agent1", environment, speed = 0)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agent Movement with Sprite")


PURPLE = (216, 191, 216)
P = (128, 0, 128)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)


all_sprites = pygame.sprite.Group()
all_sprites.add(agent) 


running = True
while running:
    screen.fill(PURPLE) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("Up")
        agent.speed += 1
    if keys[pygame.K_DOWN]:
        agent.move("Down")
        agent.speed += 1
    if keys[pygame.K_LEFT]:
        agent.move("Left")
        agent.speed += 1
    if keys[pygame.K_RIGHT]:
        agent.move("Right")
        agent.speed += 1

    position_text = font.render(f"Position: {tuple(agent.position)}", True, P)
    speed_text = font.render(f"Speed: {agent.speed}", True, P)
    ##direction_text = font.render(f"Direction: {agent.direction}", True, P)
    new_text = font.render(f"MidPosition: {tuple(agent.position)}", True, P)
    

    screen.blit(position_text, (10, 10))
    screen.blit(speed_text, (475, 10))
    ##screen.blit(direction_text, (10, 35))
    screen.blit(new_text, (200, 200))

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
