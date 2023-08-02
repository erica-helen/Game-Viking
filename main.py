import pygame
from pygame.locals import *
from configs import *
from Orientation import *
from Vik import *
from Cloud import Cloud
from Beer import Beer
from Dragon import Dragon
from Hammer import Hammer
import math
from Barrel import Barrel
from Wizard import Wizard

pygame.init()
screen = Window.create()


clock = pygame.time.Clock()
vik = Vik(10, 600, 8)
cloud = Cloud(30, 100, 3)
hammer = Hammer(29, 650, 20)
barrel = Barrel(15, 620)
dragon = Dragon(700, 450)
dragon.start_time = pygame.time.get_ticks()
wizard = Wizard(1090, 450)

def show_main_menu():
    start_button_rect = Img.START_IMG.get_rect(topleft=(585, 310))
    options_button_rect = Img.OPTIONS_IMG.get_rect(topleft=(583, 375))
    exit_button_rect = Img.EXIT_IMG.get_rect(topleft=(583, 450))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return "start"
                elif options_button_rect.collidepoint(event.pos):
                    options()
                    return "options"
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    return "exit"

        screen.blit(Img.MAIN_MENU_IMG, [0, 0])
        screen.blit(Img.START_IMG, start_button_rect)
        screen.blit(Img.OPTIONS_IMG, options_button_rect)
        screen.blit(Img.EXIT_IMG, exit_button_rect)

        pygame.display.update()


def options():
    bg_width = Window.WIDTH

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

        screen.blit(Img.TUTORIAL, [0, 0])
        pygame.display.update()
        pygame.time.Clock().tick(60)


def start_game():
    return_to_menu = False

    while True:
        option = show_main_menu()
        if option == "start":
            game_loop()
        elif option == "options":
            return_to_menu = options()
        elif option == "exit":
            pygame.quit()
            break
        if return_to_menu:
            return_to_menu = False
            show_main_menu()


def initialize_game():
    global vik, cloud, beer, hammer, barrel, dragon, wizard
    vik = Vik(10, 600, 8)
    cloud = Cloud(30, 100, 3)
    hammer = Hammer(29, 650, 20)
    barrel = Barrel(15, 620)
    dragon = Dragon(700, 450)
    dragon.start_time = pygame.time.get_ticks()
    wizard = Wizard(1090, 450)


def game_loop():
    Sound.THUNDER.play(loops=-1)
    #Sound.THUNDER.set_volume(0.05)

    bg_width = Window.WIDTH
    scroll = 0
    scroll_speed = 1
    tiles = math.ceil(Window.WIDTH / bg_width) + 1

    LOSE_ENERGY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(LOSE_ENERGY_EVENT, 4000)

    game_over = False

    while not game_over:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == LOSE_ENERGY_EVENT:
                vik.lose_energy()
        for i in range(0, tiles):
            if dragon.ready():
                screen.blit(Img.BGNIGHT, [i * bg_width + scroll, 0])
            elif wizard.ready():
                screen.blit(Img.BGMAGIC, [i * bg_width + scroll, 0])
            else:
                screen.blit(Img.BG, [i * bg_width + scroll, 0])

        scroll -= scroll_speed

        if scroll <= -bg_width:
            scroll = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            hammer.move_forward()

        if key[pygame.K_LEFT]:
            vik.move(Direction.LEFT)
            hammer.follow_x(vik.get_x())
            hammer.follow_y(vik.get_y() + 50)
        elif key[pygame.K_RIGHT]:
            vik.move(Direction.RIGHT)
            hammer.follow_x(vik.get_x() + 21)
            hammer.follow_y(vik.get_y() + 50)

        if key[pygame.K_SPACE]:
            vik.inicial_y()
            vik.move_jump()

        vik.give_life(screen)
        vik.update_jump()
        vik.draw(screen)
        vik.energy(screen)
        cloud.points(screen)
        hammer.move()
        hammer.draw(screen)
        vik.change_appearance(hammer.is_moving())
        cloud.move()
        cloud.draw(screen)

        if cloud.kill(vik) or vik.is_dead_energy() or dragon.kill_fire(vik) or wizard.kill_magic(vik):
            print("Vik morto")
            screen.blit(Img.GAMEOVER, [0, 0])
            pygame.display.update()
            pygame.time.wait(2000)
            game_over = True

        if cloud.drink_beer(vik):
            print("Score: " + str(cloud.point))

        dragon.get_ready()
        if dragon.ready():
            dragon.draw(screen)
            dragon.move()
            dragon.give_life(screen)
            Sound.DRAGON.play()
            Sound.DRAGON.set_volume(0.01)
            cloud.ray_collide_with(dragon)
            cloud.beer_collide_with(dragon)
            if vik.colides_with(dragon):
                vik.lose_life()
                vik.resetPosition()

            if hammer.colides_with(dragon):
                dragon.hit()
                if dragon.is_hit:
                    dragon.reset_hit()

        barrel.get_ready()
        if barrel.ready():
            barrel.draw(screen)
            cloud.ray_collide_with(barrel)
            cloud.beer_collide_with(barrel)
            if vik.colides_with(barrel):
                barrel.drink_barrel(vik)
            elif dragon.colides_with(barrel):
                barrel.random_position()
                if barrel.drink_barrel(vik):
                    dragon.hit()
                    if dragon.is_hit:
                        dragon.reset_hit()


        wizard.get_ready()
        if wizard.ready():
            wizard.draw(screen)
            Sound.MAGIC.play()
            Sound.MAGIC.set_volume(0.05)
            wizard.move()
            wizard.give_life(screen)
            #wizard.colides_with(vik)
            cloud.ray_beer_collide_with(wizard)
            if wizard.colides_with(barrel):
                barrel.random_position()
            if hammer.colides_with(wizard):
                wizard.hit()
                if wizard.is_hit:
                    wizard.reset_hit()

        if wizard.wizard_is_dead():
            print("Parabéns, venceu o jogo!!!")
            screen.blit(Img.WIN, [0, 0])
            cloud.points(screen)
            pygame.display.update()
            pygame.time.wait(2000)
            game_over = True

        pygame.display.update()

    show_main_menu()

def start_game():
    while True:
        option = show_main_menu()

        if option == "start":
            initialize_game()
            game_loop()
        elif option == "options":
            return_to_menu = options()
            if return_to_menu:
                return_to_menu = False
                show_main_menu()
        elif option == "exit":
            pygame.quit()
            break

start_game()
pygame.quit()
