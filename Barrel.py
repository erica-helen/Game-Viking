import random
import configs
from configs import *


class Barrel:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = configs.Img.BARREL
        # self.random_position()
        self.total_frames = 0
        self.is_hit = False

    def random_position(self):
        self.__x = random.randint(15, 1100)
        self.__y = random.randint(600, 620)

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def drink_barrel(self, vik):
        if self.colides_with(vik):
            vik.make_energy_full()
            #vik.gain_life()
            self.total_frames = 0
            self.random_position()
            print("Colidiu com barrel")

    def get_ready(self):
        self.total_frames += 1

    def ready(self):
        if self.total_frames >= 900:
            return True


    def barrel_collide_with(self, dragon):
        if self.colides_with(dragon):
            self.__x = random.randint(15, 1100)

    def hit(self, vik):
        if self.drink_barrel(vik):
            self.total_frames = 0

    def reset_hit(self):
        self.is_hit = False

