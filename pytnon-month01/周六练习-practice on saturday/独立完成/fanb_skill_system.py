'''
    技能管理系统
'''
class SkillEffect:
    '''技能影响效果'''
    def impact(self):
        pass
#伤害效果
class DamageEffect(SkillEffect):
    def __init__(self,value):
        self.value = value
    def impact(self):
        print('血量减少%s点' % self.value )
#减速效果
class LowerSpeedEffect(SkillEffect):
    def __init__(self,value,time):
        self.value = value
        self.time = time
    def impact(self):
        print('速度减少%s点，持续时间%s秒' % (self.value,self.time))
#降低防御力
class LowerDeffenceEffect(SkillEffect):
    def __init__(self,value,time):
        self.value = value
        self.time = time
    def impact(self):
        print('防御力减少%s点，持续时间%s秒' % (self.value,self.time))

#-------------------------------------------------------------------
class SkillDeployer:
    '''技能释放器'''
    def __init__(self, name=None):
        self.name = name
        # 保存配置文件内容
        self.__load_config_file = self.__load_config_file()
        # 保存创建好的效果对象
        self.__creat_skill_obj = self.__creat_skill_obj()

    # 读配置文件
    def __load_config_file(self):
        return {
            '剑开天门':['DamageEffect(90)','LowerDeffenceEffect(20,2)'],
            '两袖青蛇':['DamageEffect(50)','LowerSpeedEffect(15,2)']
        }

    # 创建对象
    def __creat_skill_obj(self):
        skill_obj_list = self.__load_config_file[self.name]
        return [eval(item) for item in skill_obj_list]

    # 调用方法
    def genernate_skill(self):
        print('释放技能！',self.name)
        for item in self.__creat_skill_obj:
            item.impact()

#测试代码：
skill = SkillDeployer('剑开天门')
skill.genernate_skill()
skill = SkillDeployer('两袖青蛇')
skill.genernate_skill()


