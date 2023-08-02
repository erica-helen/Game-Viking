import pygame
import configs
import random
from Direction import Direction
from Fire import Fire


class Dragon:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = configs.Img.DRAGON
        self.fires = []
        self.__total_frames_fire = 0
        self.__total_frames_dragon = 0
        self.lifes = 3
        self.hammer_collisions = 0
        self.is_hit = False
        self.hit_cooldown = 1000
        self.last_hit_time = pygame.time.get_ticks()
        self.game_duration = 2 * 60 * 1000


    def check_time_limit(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.game_duration:
            self.get_ready = lambda: False

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])
        for fire in self.fires:
            fire.draw(surface)

    def get_ready(self):
        self.check_time_limit()
        self.__total_frames_dragon += 1

    def move(self):
        self.__total_frames_fire += 1
        take_shoot = random.randint(1, 100) <= 50
        if self.__total_frames_fire == 300:
            self.__total_frames_fire = 0
            if take_shoot:
                self.shoot()
        for fire in self.fires:
            fire.move()

    def shoot(self):
        fire = Fire(self.__x + 70, self.__y)
        self.fires.append(fire)

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def kill_fire(self, vik):
        for fire in self.fires:
            if fire.colides_with(vik):
                self.fires.remove(fire)
                vik.lose_life()
                if vik.is_dead():
                    return True
        return False

    def dragon_is_dead(self):
        return self.lifes < 0

    def lose_life(self):
        self.lifes -= 1
        print("Dragão Perde vida")

    def ready(self):
        if self.__total_frames_dragon >= 3000:
            return True

    def hit(self):
        current_time = pygame.time.get_ticks()
        if not self.is_hit and current_time - self.last_hit_time >= self.hit_cooldown:
            self.lose_life()
            self.is_hit = True
            self.last_hit_time = current_time
        if self.dragon_is_dead():
            self.__total_frames_dragon = 0
            self.lifes = 3

    def reset_hit(self):
        self.is_hit = False

    def give_life(self, surface):
        if self.lifes == 1:
            surface.blit(configs.Img.ENERGYD2, [10, 53])
        elif self.lifes == 2:
            surface.blit(configs.Img.ENERGYD3, [10, 53])
        elif self.lifes == 3:
            surface.blit(configs.Img.ENERGYD4, [10, 53])
        elif self.lifes < 1:
            surface.blit(configs.Img.ENERGYD1, [10, 53])

