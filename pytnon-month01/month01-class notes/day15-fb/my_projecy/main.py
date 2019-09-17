#包名.子包名.模块  导入函数
# from my_projecy.skill_system.shill_deployer import skill_deployer
#目录名.子包名 导入模块
from my_projecy.skill_system import *


skill_deployer.skill_deployer()

class Main:
    @classmethod
    def my_main(cls):
        print('my main')
