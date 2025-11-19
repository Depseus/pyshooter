import pygame   
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # This here draws the little triangle that is our character
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # Here we take in delta time and create the rotation of the player character
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # This is called every game loop, looking for what the user is pressing to control the character
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # If 'A' is pressed, rotate counter clockwise
        if keys[pygame.K_a]:
            self.rotate(dt)
        # If 'D' is pressed, rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(-dt)
        # If 'W' is pressed, move forward
        if keys[pygame.K_w]:
            self.move(dt)
        # If 'S' is pressed, move backward
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector