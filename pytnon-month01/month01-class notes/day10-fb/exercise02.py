#创建Studen类
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def print_self(self):
        print('%s的年龄是%s,成绩为%s.' %
              (self.name,self.age,self.score))

list_2 = [Student('小一',14,59),
          Student('小二',15,69),
          Student('小三',16,99)]
print(list_2)

#定义一个函数 查找小二同学的成绩
def find_1(name):
    for item in list_2:
        if item.name == name:
            return item

stu_1 = find_1('小二')
print(stu_1.name,stu_1.score)
stu_1 = find_1('小四')
#stu_1 = None
#None.score
if stu_1:#因此要做一下判断
    print(stu_1.score)#AttributeError:
# 'NoneType' object has no attribute 'name'

#定义函数查找年龄在30岁以下:
def age_30():
    list_3 = []
    for item in list_2:
        if item.age < 30:
            # list_3.append([item.name,item.age,item.score])
            list_3.append(item)
    return list_3

list_3 = age_30()
for item in list_3:
    print('小于30岁的学生:',item.name)

#删除所有不及格学生,通过索引从后往前删,因为列表内预留内存空间
# 会自动进位,容易出错
def delete_nopass():
    for i in range((len(list_2)-1),-1,-1):
        if list_2[i].score < 60:
            del list_2[i]
    return list_2

list_4 = delete_nopass()
for item in list_4:
    print(item.name,end=' ')



