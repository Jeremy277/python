"""
  天龙八部 技能系统
"""

class ImpactEffect:
  """
    影响效果
  """

  def impact(self):
    """
      影响效果,由技能释放器调用,由具体效果类实现.
    :return:
    """
    raise NotImplementedError()


class DamageEffect(ImpactEffect):
  """
    伤害生命效果
    可以被所有需要伤害生命的技能使用
  """

  def __init__(self, value):
    self.value = value

  def impact(self):
    print("伤害你的%d生命" % self.value)


class LowerMoveSpeed(ImpactEffect):
  """
    降低移动速度效果
  """

  def __init__(self, speed, time):
    self.speed = speed
    self.time = time

  def impact(self):
    print("降低速度为%d,持续时间%d." % (self.speed, self.time))


class SkillDeployer:
  """
    技能释放器
  """

  def __init__(self, name):
    self.name = name
    self.__list_impact = self.__config_skill()

  def __config_skill(self):
    """
      配置技能
    """
    # 配置文件中,记录的信息.
    dict_skill_config_info = {
      "金刚伏魔": ["DamageEffect(100)"],
      "降龙十八掌": ["LowerMoveSpeed(50,60)", "DamageEffect(100)"]
    }
    # 根据键(技能名称)从字典中获取值(str列表)
    list_skill_info = dict_skill_config_info[self.name]
    # 根据字符串列表,创建影响效果对象的列表.
    # "DamageEffect(100)" -->DamageEffect的对象
    list_skill_instance = []
    for item in list_skill_info:
      list_skill_instance.append(eval(item))
    # 返回技能列表
    return list_skill_instance
    # 建议使用列表推导式
    # return [eval(item) for item in list_skill_info]

  def generate_skill(self):
    """
      生成(释放)技能
    :return:
    """
    print(self.name, "技能释放啦")
    # 遍历影响效果列表,执行每个效果.
    for item in self.__list_impact:
      item.impact()


# 测试
# 创建技能(确定技能名称,加载技能效果)
xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()

jgfm = SkillDeployer("金刚伏魔")
jgfm.generate_skill()
