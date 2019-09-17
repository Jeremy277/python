from project.student_system_model.bll import StudentManagerController
from project.student_system_model.model import StudentModel


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