import configs
from configs import *
from Orientation import *
import configs
from configs import *
from Beer import Beer


class Vik:
    def __init__(self, x, y, speed):
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__img = Img.VIK
        self.__jumping = False
        self.__jump_height = 400
        self.__lifes = 3
        self.__energy = 9
        self.__imgheart = configs.Img.LIFEHEART
        self.__direction = Direction.RIGHT

    def start_jump(self):
        self.__jumping = True

    def change_appearance(self, dropped_hammer):
        if dropped_hammer:
            if self.__direction == Direction.RIGHT:
                self.__img = configs.Img.VIKWITHOUTHAMMER
            elif self.__direction == Direction.LEFT:
                self.__img = configs.Img.VIKWITHOUTHAMMERLEFT
        else:
            if self.__direction == Direction.RIGHT:
                self.__img = configs.Img.VIK
            else:
                self.__img = configs.Img.VIKLEFT

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def get_speed(self):
        return self.__speed

    def resetPosition(self):
        self.__x = 10
        self.__y = 600

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self, direction):
        if self.__energy == 9:
            self.__speed = 10
        elif self.__energy == 8:
            self.__speed = 9
        elif self.__energy == 7:
            self.__speed = 8
        elif self.__energy == 6:
            self.__speed = 7
        elif self.__energy == 5:
            self.__speed = 6
        else:
            self.__speed = 5

        if direction == Direction.UP:
            self.__y -= self.__speed
        elif direction == Direction.DOWN:
            self.__y += self.__speed
            if self.__y > 600:
                self.__y = 600
        elif direction == Direction.RIGHT:
            self.__x += self.__speed
        elif direction == Direction.LEFT:
            self.__x -= self.__speed

        self.limit_boundaries()
        self.__direction = direction

    def move_jump(self):
        if not self.__jumping:
            self.__jumping = True
    def update_jump(self):
        if self.__jumping:
            if self.__y >= self.__jump_height:
                self.__y -= 8
            else:
                self.__jumping = False

        elif self.__y <= 590:
            self.__y += 8
    def inicial_y(self):
        self.__y = 600
    def give_life(self, surface):
        if self.__lifes >= 1:
            surface.blit(self.__imgheart, [10, 20])
        if self.__lifes >= 2:
            surface.blit(self.__imgheart, [50, 20])
        if self.__lifes >= 3:
            surface.blit(self.__imgheart, [90, 20])
    def energy(self, surface):
        if self.__energy >= 1:
            surface.blit(configs.Img.ENERGY0, [890, 20])
        if self.__energy >= 2:
            surface.blit(configs.Img.ENERGY1, [890, 20])
        if self.__energy >= 3:
            surface.blit(configs.Img.ENERGY2, [890, 20])
        if self.__energy >= 4:
            surface.blit(configs.Img.ENERGY3, [890, 20])
        if self.__energy >= 5:
            surface.blit(configs.Img.ENERGY4, [890, 20])
        if self.__energy >= 6:
            surface.blit(configs.Img.ENERGY5, [890, 20])
        if self.__energy >= 7:
            surface.blit(configs.Img.ENERGY6, [890, 20])
        if self.__energy >= 8:
            surface.blit(configs.Img.ENERGY7, [890, 20])
        if self.__energy >= 9:
            surface.blit(configs.Img.ENERGY8, [890, 20])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def lose_life(self):
        if self.__lifes > 0:
            self.__lifes -= 1
            print("Perde vida")
    def lose_energy(self):
        current_time = pygame.time.get_ticks()
        if current_time > 4000:
            if self.__energy > 0:
                self.__energy -= 1

    def is_dead(self):
        return self.__lifes == 0

    def is_dead_energy(self):
        return self.__energy == 0

    def limit_boundaries(self):
        if self.__x < configs.Window.MARGIN['left']:
            self.__x = configs.Window.MARGIN['left']
        elif self.__x > configs.Window.MARGIN['right']:
            self.__x = configs.Window.MARGIN['right']
        elif self.__y < configs.Window.MARGIN['top']:
            self.__y = configs.Window.MARGIN['top']
        elif self.__y > configs.Window.MARGIN['bottom']:
            self.__y = configs.Window.MARGIN['bottom']

    def gain_life(self):
        if self.__lifes <= 2:
            self.__lifes += 1


    def gain_energy(self, beer):
        if self.__energy <= 8:
            self.__energy += 1

    def make_energy_full(self):
        self.__energy = 9



