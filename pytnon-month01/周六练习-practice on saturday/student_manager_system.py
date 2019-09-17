#student_manager_system
#第一步：
# 数据模型类：StudentModel
# 逻辑控制类：StudentManagerController
# 	数据：学生列表 __stu_list
# 	行为：获取列表 stu_list,
#        添加学生 add_student
#            添加id 整数 递增 类变量
class StudentModel:
    '''
    学生模型
    '''
    #id不需要传值 放在最后一位
    def __init__(self, name="", age=0, score=0,id=0):
        '''
        创建学生对象
        :param id: 编号 该学生的唯一标识
        :param name: 姓名 str
        :param age: 年龄 int
        :param score: 成绩 int
        '''
        self.id = id
        self.name = name
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
    #1.添加学生
    def add_student(self,stu):
        #为学生设置id 递增
        # StudentManagerController.__stu_id += 1
        #stu.id = StudentManagerController.__stu_id
        stu.id = self.__generate_id()
        #将学生添加到学生列表
        self.__stu_list.append(stu)
    #生成id
    def __generate_id(self):
        StudentManagerController.__stu_id += 1
        return StudentManagerController.__stu_id
    # 2.删除学生remove_student
        #根据id删除学生
        #删除后返回结果  成功True/失败False
    def remove_student(self,id):
        '''
        根据编号删除学生
        :param id: 编号
        :return: 删除的结果
        '''
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False
    #3.修改学生update_student
    # s01 = StudentModel('zs',18,50)
    # s01 = StudentModel('zs',19,40,1001)
    def update_student(self,stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False
    # 4.根据成绩排序order_by_score。
    # 你是谁  你要找谁
    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i],self.__stu_list[j] = \
                    self.__stu_list[j],self.__stu_list[i]

class StudentManagerView:
    #生成在此类下的逻辑管理器  组合
    def __init__(self):
        self.__manger = StudentManagerController()
    #1.显示菜单
    def __display_menu(self):
        print('''
    学生信息管理系统1.0
+-----------------------+
| 0)退出管理系统          |                                
| 1)添加学生信息          |              
| 2)显示学生信息          |
| 3)删除学生信息          |
| 4)修改学生信息          |
| 5)按照成绩排序          |
+-----------------------+
 ''')
    #2.选择菜单
    def __select_menu(self):
        # import sys
        option = input('请选择:')
        if option == '1':
            self.__input_students()
        elif option == '2':
            self.__output_students()
        elif option == '3':
            self.__delete_student()
        elif option == '4':
            self.__modify_student()
        elif option == '5':
            self.__output_student_by_score()
        elif option == '0':
            # print('谢谢使用,退出系统')
            # sys.exit()
            exit('谢谢使用,退出系统')
        else:
            print('请正确输入选项!')
    #3.入口逻辑
    def main(self):
        '''
        界面入口
        :return:
        '''
        while True:
            self.__display_menu()
            self.__select_menu()
    # 4.输入学生
    def __input_students(self):
        #收集学生信息 要求用户输入 姓名年龄 成绩
        #创建学生对象
        #在控制器找add_student方法
        name = input('请输入学生姓名:')
        age = int(input('请输入学生年龄:'))
        score = int(input('请输入学生成绩:'))
        stu = StudentModel(name,age,score)
        #这样写会重复生成 管理器 列表,因此在视图界面类创造一个管理器
        # manger = StudentManagerController()
        self.__manger.add_student(stu)
    #5.输出信息
    def __output_students(self):
        for item in self.__manger.stu_list:
            print(item.id, item.name, item.age, item.score)
    #6.删除学生
    def __delete_student(self):
        #需要用户输入id
        #调用管理器对象的删除学生方法
        #如果结果为True 显示删除成功
        #否则显示删除失败
        id = int(input('请输入需要删除的学生ID:'))
        if self.__manger.remove_student(id):
            print('删除成功!')
        else:
            print('删除失败!')
        print('删除后学生信息:')
        self.__output_students()
    #7.修改学生信息
    def __modify_student(self):
        #手机用户输入的信息保存到对象
        #调用管理器的修改学生方法
        id = int(input('请输入需要修改的学生ID:'))
        name = input('请输入修改后学生姓名:')
        age = int(input('请输入修改后学生年龄:'))
        score = int(input('请输入修改后学生成绩:'))
        stu = StudentModel(name, age, score,id)
        if self.__manger.update_student(stu):
            print('修改成功!')
        else:
            print('修改失败!')
        print('修改后学生信息:')
        self.__output_students()
    #8.按成绩升序排列
    def __output_student_by_score(self):
        self.__manger.order_by_score()
        print('按照成绩排序学生:')
        self.__output_students()

#2.测试界面视图
view = StudentManagerView()
# view.display_menu()
view.main()

#1.测试逻辑控制代码
#测试添加学员
# manger = StudentManagerController()
# s01 = StudentModel('许瑶',18,98)
# s02 = StudentModel('许仙',16,99)
# s03 = StudentModel('小青',15,79)
# s04 = StudentModel('姐夫',15,79)
# manger.add_student(s01)
# manger.add_student(s02)
# manger.add_student(s03)
# manger.add_student(s04)
# for item in manger.stu_list:
#     print(item.id,item.name,item.age,item.score)
# #manger.stu_list列表 保存学生对象
# # print(manger.stu_list[1].name)
# #测试删除学员
# manger.remove_student(1004)
# for item in manger.stu_list:
#     print('删除后:',item.id,item.name)
# #测试修改学员
# manger.update_student(StudentModel('娘子',19,80,1001))
# for item in manger.stu_list:
#     print('修改后:',item.id,item.name,item.age,item.score)
# #测试按成绩排序
# manger.order_by_score()
# for item in manger.stu_list:
#     print('按分数升序排列:',item.id,item.name,item.age,item.score)



