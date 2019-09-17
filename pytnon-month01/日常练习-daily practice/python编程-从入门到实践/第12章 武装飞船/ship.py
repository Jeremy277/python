import pygame

class Ship:
    def __init__(self, ai_settings,screen):
        '''初始化飞船并设置其初始位置'''
        #引用 self 和 screen ,其中后者指定了要将飞船绘制到什么地方
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        #处理 rect 对象时,可使用矩形四角和中心的 x 和 y 坐标。
        # 可通过设置这些值来指定矩形的位置。
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)
        #将每艘新飞船放在屏幕底部中央
        #将 self.rect.centerx (飞船中心的 x 坐标)
        # 设置为表示屏幕的矩形的属性 centerx
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #移动标志 向右
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '根据移动标志调整飞船的位置'
        if self.moving_right:
            self.rect.centerx += 1
            # self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= 1
            # self.center -= self.ai_settings.ship_speed_factor
            #根据self.center更新rect对象
            # self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)