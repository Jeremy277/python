import sys
#在终端运行是,需要添加路径,为所在包的上一级目录
sys.path.append('/home/tarena/pytnon-month01/month01-石博文笔记/day16-shibw/project')
print(sys.path)
#目录.包 导入模块
from game import game_2048#在文件名右键 点击mark再点root
#模块名.成员
game_2048.fun01()

#目录.包.模块 导入 成员
# from project.game.game_2048 import fun01
#
# fun01()

# import demo01