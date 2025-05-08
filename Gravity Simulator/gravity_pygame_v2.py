# Calculate Accleration
# Update Velocity
# Update Position

class Planet:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.radius = 15 * math.cbrt(mass)
        
        self.x = position[0]
        self.y = position[1]

        self.velo_x = velocity[0] * math.cos(velocity[1])
        self.velo_x = velocity[0] * math.sin(velocity[1])
        
        self.accl_x = 0
        self.accl_y = 0

    def update_acceleration(self):
        for n in range(len(all_planets)):

            other = all_planets[n]

            if self == other:
                return
            
            distance = math.sqrt((self.x -other.x)**2 + (self.y - other.y)**2)
            acceleration = GRAVITY * other.mass / distance

            self.accl_x = acceleration * cosine
            self.accL_y = accleration * sine

    def move(self):
        self.velo_x += self.accl_x
        self.velo_y += self.accl_y

        self.x += self.velo_x
        self.y += self.velo_y

    def draw(self):
        pygame.draw.ellipse(screen, self.color,
                            [self.x - self.radius, self.y - self.radius,
                             2 * self.radius, 2 * self.radius])


def main():
    all_planets = []

    for n in range(len(all_planets)):
        update_acceleration(all_planets[n])
        
    for n in range(len(all_planets)):
        move(all_planets[n])
