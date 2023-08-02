import pygame
import self as self
import random
import configs
from Ray import Ray
from Beer import Beer


class Cloud:
    def __init__(self, x, y, speed):
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__img = configs.Img.CLOUD
        self.__is_waiting = False
        self.rays = []
        self.__total_frames = 0
        self.__direction = 4
        self.beers = []
        self.__total_frames_beer = 0
        self.point = 0

    def speed(self):
        self.__speed = 10

    def shoot(self):
        ray = Ray(self.__x + 23, self.__y + 52)
        self.rays.append(ray)

    def drop_beer(self):
        beer = Beer(self.__x + 10, self.__y + 52)
        self.beers.append(beer)

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])
        for ray in self.rays:
            ray.draw(surface)
        for beer in self.beers:
            beer.draw(surface)

    def move(self):
        self.__total_frames += 2
        self.__total_frames_beer += 2

        if self.__x >= configs.Window.MARGIN['right']:
            self.__direction = -4
        elif self.__x <= configs.Window.MARGIN['left']:
            self.__direction = 4

        self.__x += self.__direction

        take_shoot = random.randint(1, 100) <= 50

        if self.__total_frames == 200:
            self.__total_frames = 0
            if take_shoot:
                self.shoot()

        for ray in self.rays:
            ray.move()

        beers = random.randint(1, 100) <= 50

        if self.__total_frames_beer == 400:
            self.__total_frames_beer = 0

            if beers:
                self.drop_beer()

        for beer in self.beers:
            beer.move()

    def limit_boundaries(self):
        if self.__x < configs.Window.MARGIN['left']:
            self.__x = configs.Window.MARGIN['left']
        elif self.__x > configs.Window.MARGIN['right']:
            self.__x = configs.Window.MARGIN['right']
        elif self.__y < configs.Window.MARGIN['top']:
            self.__y = configs.Window.MARGIN['top']
        elif self.__y > configs.Window.MARGIN['bottom']:
            self.__y = configs.Window.MARGIN['bottom']

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def drink_beer(self, vik):
        for beer in self.beers:
            if beer.colides_with(vik):
                configs.Sound.AH.play()
                configs.Sound.AH.set_volume(0.05)
                vik.gain_life()
                vik.gain_energy(beer)
                self.point += 1
                self.beers.remove(beer)

    def kill(self, vik):
        for ray in self.rays:
            if ray.colides_with(vik):
                vik.lose_life()
                configs.Sound.SHOCK.play()
                self.rays.remove(ray)
                if vik.is_dead():
                    return True
        return False

    def ray_collide_with(self, dragon):
        for ray in self.rays:
            if ray.colides_with(dragon):
                self.rays.remove(ray)

    def beer_collide_with(self, dragon):
        for beer in self.beers:
            if beer.colides_with(dragon):
                self.beers.remove(beer)

    def ray_collide_with(self, barrel):
        for ray in self.rays:
            if ray.colides_with(barrel):
                self.rays.remove(ray)

    def ray_beer_collide_with(self, wizard):
        for ray in self.rays:
            if ray.colides_with(wizard):
                self.rays.remove(ray)
        for beer in self.beers:
            if beer.colides_with(wizard):
                self.beers.remove(beer)

    def points(self, surface):
        font = pygame.font.Font("Font/Play-Bold.ttf", 45)
        text = font.render("Score: " + str(self.point), True, (0, 0, 0))
        surface.blit(text, (560, 20))
