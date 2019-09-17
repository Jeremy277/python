'''
类
'''
#类名首字母大写
class Wife:
    #数据成员:姓名 身高 体重
    def __init__(self,height,weight,name):   #双下划线
        self.height = height
        self.weight = weight
        self.name = name
    #行为成员:玩 唱
    def sing(self):
        print('%s正在唱歌' % self.name)
    def play(self,game):
        print('%s正在玩%s' % (self.name,game))

#自动调用__init__方法:位置一一对应
w01 = Wife(1.7,50,'ciic')#ciic 1.7 50
print(w01.name,end=' ')
print(w01.height,end=' ')
print(w01.weight)

w02 = Wife('jer',1.8,70)#70 jer 1.8
print(w02.name,end=' ')
print(w02.height,end=' ')
print(w02.weight,)
w01.sing()
w01.play(2048)

# # 创建对象:
# w01 = Wife()
# print(w01)
# #w01的身高 1.7
# w01.height = 1.7
# print(w01.height)
# w01.weight = 50
# print(w01.weight)
# w01.name = 'cici'
# print(w01.name)