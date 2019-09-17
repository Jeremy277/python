# 玩飞机大战   抽象  数据 行为
# 定义Hero类
# 定义Enemy类
# 定义Bullet类

# 定义Hero类
class Her0:
    def __init__(self,red,orange,yellow,green):
        self.red = red
        self.orange = orange
        self.yellow = yellow
        self.green = green
    def hero_skill(self,fast,double):
        self.fast = fast
        self.double = double
# 定义Enemy类
class Enemy:
    def __init__(self,red,orange,yellow,green):
        self.red = red
        self.orange = orange
        self.yellow = yellow
        self.green = green
    def enemy_skill(self,fast,double):
        self.fast = fast
        self.double = double
# 定义Bullet类
class Bullet:
    def __init__(self, small=None, middle=None, big=None):
        self.small = small
        self.middle = middle
        self.big = big

    def bullet_skill(self,fast,double):
        self.fast = fast
        self.double = double


