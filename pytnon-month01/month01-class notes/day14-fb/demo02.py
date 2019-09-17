class StudentModel:
    def __init__(self,name='',age =
    0,score = 0,id = 0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id
    # #对象-->字符串(格式随意)
    # def __str__(self):
    #     return '编号:%d,姓名:%s' % (self.id,self.name)
    #对象-->字符串(解释器识别 有格式要求)
    def __repr__(self):
        return 'StudentModel("%s",%d,%d,%d)' % (
            self.name,self.age,self.score,self.id
        )


s01 = StudentModel('哪吒',7,99,7)
print(s01)
# str01 = str(s01)
# print(str01)
#eval 将字符串当做代码去执行
#eval()只能执行一行表达式
# print(eval('1+2*5'))
# eval('del s01')
#exec()执行一段语句 分号;或换行符\n隔开
exec("a=11;b=20;print(a+b)")
str02='''
a=1
b=2
print(a+b)'''
exec(str02)
#克隆对象
s02 = eval(repr(s01))
print(s02)
