import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


# def run_game():
# # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     #display.set_mode()
#     #返回的 surface 表示整个游戏窗口。
#     # 我们激活游戏的动画循环后,每经过一次循环都将自动重绘这个 surface 。
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption("Alien Invasion")
#     #设置背景色   浅灰色
#     bg_color = (230,230,230)
#     # 开始游戏的主循环
#     while True:
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#         #每次循环时重绘屏幕:用背景色填充屏幕只接受一个实参:颜色
#         screen.fill(bg_color)
#         # 让最近绘制的屏幕可见
#         #命令 Pygame 让最近绘制的屏幕可见 它在每次执行 while 循环时都
#         # 绘制一个空屏幕,并擦去旧屏幕,使得只有新屏幕可见。
#         # 在我们移动游戏元素时, pygame.display.flip() 将不断更新屏幕,
#         # 以显示元素的新位置,并在原来的位置隐藏元素,从而营造平滑移动的效果。
#         pygame.display.flip()
# run_game()

def run_game():
    #初始化pygame 设置 屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode\
        ((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #开始游戏主循坏
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        # # #每次循环时重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # #让最近绘制的屏幕可见
        # pygame.display.flip()
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()

