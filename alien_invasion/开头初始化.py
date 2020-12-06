#外星人入侵  开头
import pygame as ga
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from  scoreboard import Scoreboard
from button import Button


# noinspection PyInterpreter,PyInterpreter,PyInterpreter
def run_game():
    #初始化游戏并创建一个屏幕对象
    ga.init()   #初始化设置
    ai_settings = Settings()
    screen = ga.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) #设置尺寸大小
    ga.display.set_caption("外星人入侵")

    #创建play按钮
    play_button = Button(ai_settings, screen, 'play')

    #创建一个用于存储游戏统计信息的实例,并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一个外星人
    #alien = Alien(ai_settings, screen)

    #设置背景色
    bg_color = (230,230,230)

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)

    #开始游戏循环
    while True :
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #gf.update_bullets(ai_settings,screen, ship, aliens, bullets)
            #gf.update_aliens(ai_settings, stats,screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        #gf.update_screen(ai_settings, screen, ship, aliens, bullets)
           # gf.create_fleet(ai_settings, screen, ship, aliens)
        #gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        gf. update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

