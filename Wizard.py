import pygame
import configs
import random
from Direction import Direction
from Magic import Magic


class Wizard:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = configs.Img.WIZARD
        self.magic = []
        self.__total_frames_magic = 0
        self.__total_frames_wizard = 0
        self.lifes = 10
        self.is_hit = False
        self.hit_cooldown = 1000
        self.last_hit_time = pygame.time.get_ticks()


    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])
        for magic in self.magic:
            magic.draw(surface)

    def get_ready(self):
        self.__total_frames_wizard += 1

    def move(self):
        self.__total_frames_magic += 1
        take_shoot = random.randint(1, 100) <= 50
        if self.__total_frames_magic == 300:
            self.__total_frames_magic = 0
            if take_shoot:
                self.shoot()
        for magic in self.magic:
            magic.move()

    def shoot(self):
        magic = Magic(self.__x + 10, self.__y)
        self.magic.append(magic)

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def kill_magic(self, vik):
        for magic in self.magic:
            if magic.colides_with(vik):
                vik.lose_life()

                self.magic.remove(magic)
                if vik.is_dead():
                    return True

        return False

    def wizard_is_dead(self):
        return self.lifes <= 0

    def lose_life(self):
        self.lifes -= 1
        print("Wizard Perde vida")

    def ready(self):
        if self.lifes <= 0:
            return False

        return self.__total_frames_wizard >= 10000

    def hit(self):
        current_time = pygame.time.get_ticks()
        if not self.is_hit and current_time - self.last_hit_time >= self.hit_cooldown:
            self.lose_life()
            self.is_hit = True
            self.last_hit_time = current_time

        if self.wizard_is_dead():
            self.__total_frames_wizard = 0

    def reset_hit(self):
        self.is_hit = False

    def give_life(self, surface):
        if self.lifes == 10:
            surface.blit(configs.Img.WIZARDENERGY10, [10, 50])
        elif self.lifes == 9:
            surface.blit(configs.Img.WIZARDENERGY9, [10, 50])
        elif self.lifes == 8:
            surface.blit(configs.Img.WIZARDENERGY8, [10, 50])
        elif self.lifes == 7:
            surface.blit(configs.Img.WIZARDENERGY7, [10, 50])
        elif self.lifes == 6:
            surface.blit(configs.Img.WIZARDENERGY6, [10, 50])
        elif self.lifes == 5:
            surface.blit(configs.Img.WIZARDENERGY5, [10, 50])
        elif self.lifes == 4:
            surface.blit(configs.Img.WIZARDENERGY4, [10, 50])
        elif self.lifes == 3:
            surface.blit(configs.Img.WIZARDENERGY3, [10, 50])
        elif self.lifes == 2:
            surface.blit(configs.Img.WIZARDENERGY2, [10, 50])
        elif self.lifes == 1:
            surface.blit(configs.Img.WIZARDENERGY1, [10, 50])
