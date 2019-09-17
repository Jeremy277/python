class Settings:
    '''存储 外星人入侵 的所有设置类'''
    def __init__(self):
        '''初始化游戏设置'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,200,250)
        #飞船移动初始值设置为1.5像素
        self.ship_speed_factor = 1.5