import random
import pygame
import configs
from Vik import Vik
from Orientation import Direction


class Hammer:
    def __init__(self, x, y, speed):
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__moving = False
        self.point = 0
        self.temporary_y = y
        self.temporary_x = 0
        self.__img = configs.Img.NOTHING

    def is_moving(self):
        return self.__moving

    def left(self):
        self.__img = configs.Img.HAMMER

    def right(self):
        self.__img = configs.Img.NOTHING

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self):
        if self.__moving:
            self.__x += self.__speed
            if self.__x >= configs.Window.WIDTH:
                self.__x = self.temporary_x
                self.__y = self.temporary_y
                self.__moving = False
                self.__img = configs.Img.NOTHING

    def follow_y(self, new_y):
        self.temporary_y = new_y
        if not self.__moving:
            self.__y = new_y

    def follow_x(self, new_x):
        self.temporary_x = new_x
        if not self.__moving:
            self.__x = new_x

    def move_forward(self):
        self.__img = configs.Img.HAMMER
        self.start_movement()
        if self.__x >= configs.Window.MARGIN['right']:
            self.__img = configs.Img.NOTHING

    def start_movement(self):
        self.__moving = True

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])
