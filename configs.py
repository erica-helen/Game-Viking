import pygame

pygame.init()


class Window:
    WIDTH = 1280
    HEIGHT = 768
    MARGIN = {
        'top': 0,
        'bottom': 768,
        'left': 0,
        'right': 1050
    }
    TITLE = "Game Viking"
    ICON = pygame.image.load("img/icon.png")

    @staticmethod
    def create():
        screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption(Window.TITLE)
        pygame.display.set_icon(Window.ICON.convert_alpha())
        return screen


pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))


class Img:
    BG = pygame.image.load("img/background_nature.png").convert_alpha()
    BGNIGHT = pygame.image.load("img/BGnight.png").convert_alpha()
    BGMAGIC = pygame.image.load("img/BGmagic.png").convert_alpha()
    VIK = pygame.image.load("img/vikmartelo.png").convert_alpha()
    VIKLEFT = pygame.image.load("img/vikmarteloleft.png").convert_alpha()
    LIFEHEART = pygame.image.load("img/lifeheart.png").convert_alpha()
    GAMEOVER = pygame.image.load("img/gameover.jpg").convert_alpha()
    CLOUD = pygame.image.load("img/cloude02.png").convert_alpha()
    RAY = pygame.image.load("img/raio.png").convert_alpha()
    VIKCHOQUE = pygame.image.load("img/vikchoque2.png").convert_alpha()
    BEER = pygame.image.load("img/beer.png").convert_alpha()
    ENERGY0 = pygame.image.load("img/0.png").convert_alpha()
    ENERGY1 = pygame.image.load("img/1.png").convert_alpha()
    ENERGY2 = pygame.image.load("img/2.png").convert_alpha()
    ENERGY3 = pygame.image.load("img/3.png").convert_alpha()
    ENERGY4 = pygame.image.load("img/4.png").convert_alpha()
    ENERGY5 = pygame.image.load("img/5.png").convert_alpha()
    ENERGY6 = pygame.image.load("img/6.png").convert_alpha()
    ENERGY7 = pygame.image.load("img/7.png").convert_alpha()
    ENERGY8 = pygame.image.load("img/8.png").convert_alpha()
    DRAGON = pygame.image.load("img/dragonsemfogo2.png").convert_alpha()
    FIRE = pygame.image.load("img/fire2.png").convert_alpha()
    NOTHING = pygame.image.load("img/verde.png").convert_alpha()
    HAMMER = pygame.image.load("img/hammer.png").convert_alpha()
    HAMMERLEFT = pygame.image.load("img/hammerleft.png")
    VIKWITHOUTHAMMER = pygame.image.load("img/Vikedit.png").convert_alpha()
    VIKWITHOUTHAMMERLEFT = pygame.image.load("img/vikeditleft.png").convert_alpha()
    BARREL = pygame.image.load("img/barril2.png").convert_alpha()
    WIZARD = pygame.image.load("img/wizard.png").convert_alpha()
    WIN = pygame.image.load("img/win.png").convert_alpha()
    MAIN_MENU_IMG = pygame.image.load("img/main_menu.png").convert_alpha()
    START_IMG = pygame.image.load("img/start_button.png").convert_alpha()
    OPTIONS_IMG = pygame.image.load("img/options_button.png").convert_alpha()
    EXIT_IMG = pygame.image.load("img/exit_button.png").convert_alpha()
    TUTORIAL = pygame.image.load("img/instrucoes1.png").convert_alpha()
    ENERGYD4 = pygame.image.load("img/4d.png").convert_alpha()
    ENERGYD3 = pygame.image.load("img/3d.png").convert_alpha()
    ENERGYD2 = pygame.image.load("img/2d.png").convert_alpha()
    ENERGYD1 = pygame.image.load("img/1d.png").convert_alpha()
    WIZARDENERGY10 = pygame.image.load("img/wizardbarra10.png").convert_alpha()
    WIZARDENERGY9 = pygame.image.load("img/wizardbarra9.png").convert_alpha()
    WIZARDENERGY8 = pygame.image.load("img/wizardbarra8.png").convert_alpha()
    WIZARDENERGY7 = pygame.image.load("img/wizardbarra7.png").convert_alpha()
    WIZARDENERGY6 = pygame.image.load("img/wizardbarra6.png").convert_alpha()
    WIZARDENERGY5 = pygame.image.load("img/wizardbarra5.png").convert_alpha()
    WIZARDENERGY4 = pygame.image.load("img/wizardbarra4.png").convert_alpha()
    WIZARDENERGY3 = pygame.image.load("img/wizardbarra3.png").convert_alpha()
    WIZARDENERGY2 = pygame.image.load("img/wizardbarra2.png").convert_alpha()
    WIZARDENERGY1 = pygame.image.load("img/wizardbarra1.png").convert_alpha()


    MAGIC = [
        pygame.image.load("img/magics/bola1.png").convert_alpha(),
        pygame.image.load("img/magics/bola2.png").convert_alpha(),
        pygame.image.load("img/magics/bola3.png").convert_alpha(),
        pygame.image.load("img/magics/bola4.png").convert_alpha(),
    ]

class Sound:
    THUNDER = pygame.mixer.Sound("sounds/thunder.ogg")
    SHOCK = pygame.mixer.Sound("sounds/shock.ogg")
    AH = pygame.mixer.Sound("sounds/ah.ogg")
    MAGIC = pygame.mixer.Sound("sounds/magic.ogg")
    DRAGON = pygame.mixer.Sound("sounds/dragon.ogg")
