import pygame

class Agent(pygame.sprite.Sprite):
    def __init__(self, name, environment, speed, color = (128, 0, 128), size = (20, 20)):
        super().__init__() 
        self.name = name
        self.environment = environment
        self.position = [100, 100]
        self.direction = None
        self.speed = speed

        self.image = pygame.Surface(size)   
        self.image.fill(color)             
        self.rect = self.image.get_rect()   
        self.rect.topleft = self.position   

    def move(self, direction):
        self.direction = direction

        if direction == "Up":
            self.position[1] -= self.speed  
        elif direction == "Down":
            self.position[1] += self.speed  
        elif direction == "Left":
            self.position[0] -= self.speed 
        elif direction == "Right":
            self.position[0] += self.speed 

        self.position = self.environment.limit_position(self.position)
    
        self.rect.topleft = self.position

