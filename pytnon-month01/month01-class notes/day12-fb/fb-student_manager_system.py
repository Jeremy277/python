#student_manager_system
#第一步
# 数据模型类：StudentModel
# 		数据：编号 id,姓名 name,年龄 age,成绩 score
# 逻辑控制类：StudentManagerController
# 		数据：学生列表 __stu_list          (#私有属性,提供只读)
# 		行为：获取列表 stu_list
# 		     添加学生 add_student
#                   添加id 整数 递增 类变量
#            删除学生remove_student
#            修改学生update_student
#            根据成绩排序order_by_score
class StudentModel:
    '''
    学生模型
    '''
    #id 不需要传值 放到最后一位
    def __init__(self, name='', age=0, score=0,id = 0):
        '''
        创建学生对象
        :param id: 编号 该学生的唯一标示
        :param name: 姓名 str
        :param age: 年龄 int
        :param score: 成绩 int
        '''
        self.id = id
        self.name =name
        self.age = age
        self.score = score

class StudentManagerController:
    '''
    学生管理控制器 处理业务逻辑
    '''
    __stu_id = 1000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu):
        #为学生设置id 递增
        stu.id = self.__generate_id()
        #将学生添加到学生列表
        self.__stu_list.append(stu)

    def __generate_id(self):
        StudentManagerController.__stu_id += 1
        return StudentManagerController.__stu_id

    def remove_student(self,stu_id):
        #根据id删除 删除后返回结果 成功True或失败False
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        raise ValueError('删除失败,id错误')

    def update_student(self,stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        raise ValueError('未找到对应学员')




    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[j].score:
                    self.__stu_list[i],self.__stu_list[j] = \
                    self.__stu_list[j],self.__stu_list[i]



#测试添加学员
manger = StudentManagerController()
s01 = StudentModel('许瑶',18,98)
s02 = StudentModel('许仙',16,99)
s03 = StudentModel('小青',15,79)
manger.add_student(s01)
manger.add_student(s02)
manger.add_student(s03)
for item in manger.stu_list:
    print(item.id,item.name,item.age,item.score)
#manger.stu_list列表 保存学生对象
# print(manger.stu_list[1].name)
#测试删除学员
# manger.remove_student(1001)
# for item in manger.stu_list:
#     print('删除后:',item.id,item.name)
#测试修改学员
manger.update_student(StudentModel('娘子',19,80,1001))
for item in manger.stu_list:
    print('修改后:',item.id,item.name,item.age,item.score)
#测试按成绩排序
manger.order_by_score()
for item in manger.stu_list:
    print('由大到小:',item.id,item.name,item.age,item.score)



