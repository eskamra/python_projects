import pygame, sys, time
from random import randint, uniform

class Nurse(pygame.sprite.Sprite):
    def __init__(self, groups):

        # based setup
        super().__init__(groups) # init the parent class
        self.image = pygame.image.load("../nurse_covid_game/graphics/nurse.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH /2, WINDOW_HEIGHT /2))
        self.mask = pygame.mask.from_surface(self.image) # it hepls to get rid of blank space around image
        self.can_throw = True # -> set timer
        self.throw_time = None # -> set timer
        self.throw_sound = pygame.mixer.Sound("../nurse_covid_game/sounds/throw.wav")
        self.end_game_sound = pygame.mixer.Sound("../nurse_covid_game/sounds/siren.wav")

    def throw_timer(self): # timer of throwing a syringe
        if not self.can_throw:
            current_time = pygame.time.get_ticks()
            if current_time - self.throw_time > 500: # a break between syringe throwing
                self.can_throw = True

    def input_position(self): # position of the nurse, moving via mouse
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def syringe_throw(self): # left button on mouse -> click = throw a syringe
        if pygame.mouse.get_pressed()[0] and self.can_throw:
            self.can_throw = False
            self.throw_time = pygame.time.get_ticks()
            Syringe(self.rect.midtop, syringe_group)
            self.throw_sound.play()

    def virus_collision(self):
        if pygame.sprite.spritecollide(self, covid_group, True, pygame.sprite.collide_mask):
            self.end_game_sound.play()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    def update(self):
        self.throw_timer()
        self.input_position()
        self.syringe_throw()
        self.virus_collision()


class Syringe(pygame.sprite.Sprite):
    def __init__(self, pos, groups):

        # basic setup
        super().__init__(groups)
        self.image = pygame.image.load("../nurse_covid_game/graphics/syringe.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.mask = pygame.mask.from_surface(self.image)

        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600
        self.exposion_sound = pygame.mixer.Sound("../nurse_covid_game/sounds/explosion.wav")

    def virus_collision(self):
        if pygame.sprite.spritecollide(self, covid_group, True, pygame.sprite.collide_mask):
            # collide_mask -> Collision detection between two sprites, using masks.
            self.kill() # after covid collide with syringe, the syringe disappear -> saves a memory
            self.exposion_sound.play()

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom < 0:
            self.kill() # it saves the memory -> it gets rid of the sprite
        self.virus_collision()


class Covid19(pygame.sprite.Sprite):
    def __init__(self, pos, groups):

        # basic setup
        super().__init__(groups)
        self.image = pygame.image.load("../nurse_covid_game/graphics/covid.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 700)

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.top > WINDOW_HEIGHT:
            self.kill() # it saves the memory -> it gets rid of the sprite


class Game_Time:
    def __init__(self):
        self.font = pygame.font.Font("../nurse_covid_game/graphics/gta.otf", 30)

    def display(self):
        time_text = f"Time: {pygame.time.get_ticks() // 1000}" # time in seconds
        text_surf = self.font.render(time_text, True, "white")
        text_rect = text_surf.get_rect(topright=(WINDOW_WIDTH - 50, WINDOW_HEIGHT - 700))
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface, "white", text_rect.inflate(15, 15), width=5, border_radius=5)

# Initialize pygame
pygame.init()

# Display window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Nurse Covid-Killer")
clock = pygame.time.Clock()

# background
bg_surf = pygame.image.load("../nurse_covid_game/graphics/background.jpg").convert()

# sprite groups
nurse_group = pygame.sprite.Group()
syringe_group = pygame.sprite.Group()
covid_group = pygame.sprite.Group()

# sprite creation
nurse = Nurse(nurse_group)

# timer
covid_timer = pygame.event.custom_type()
pygame.time.set_timer(covid_timer, 400)
game_time = Game_Time()
bg_music = pygame.mixer.Sound("../nurse_covid_game/sounds/background.wav")
bg_music.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == covid_timer:
            covid_y_pos = randint(-150, -50)
            covid_x_pos = randint(-100, WINDOW_WIDTH + 100)
            Covid19((covid_x_pos, covid_y_pos), covid_group)

    # delta time
    dt = clock.tick() / 1000

    display_surface.blit(bg_surf, (0, 0))

    # updates
    nurse_group.update()
    syringe_group.update()
    covid_group.update()

    # game time
    game_time.display()

    # draw objects in display surface
    nurse_group.draw(display_surface)
    syringe_group.draw(display_surface)
    covid_group.draw(display_surface)

    pygame.display.update()