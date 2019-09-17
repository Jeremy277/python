#我们将首先把管理事件的代码移到一个名为 check_events() 的函数中,
# 以简化 run_game() 并隔离事件管理循环。
# 通过隔离事件循环,可将事件管理与游戏的其他方面(如更新屏幕)分离
import sys
import pygame

def check_events(ship):
    '''相应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞船 按键一次 向右移动1像素
                ship.moving_right = True
                #添加左移
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    """ 更新屏幕上的图像,并切换到新屏幕 """
    #每次循坏时重绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
