#学生信息管理系统:
# 数据模型类：StudentModel
# 		数据：编号 id,姓名 name,年龄 age,成绩 score
class StudentModel:
    def __init__(self,name,age,score,id = 0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id
# 	逻辑控制类：StudentManagerController
# 		数据：学生列表 __stu_list
# 		(#私有属性,提供只读)
# 		行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，
# 		修改学生update_student，根据成绩排序order_by_score。
class StudentManagerController:
    __stu_id = 1000
    def __init__(self): #函数中不需要定义行参
        self.__stu_list = []  #赋值空列表

    @property
    def stu_list(self):
        return self.__stu_list
    def add_student(self,stu):
        StudentManagerController.__stu_id += 1
        stu.id = StudentManagerController.__stu_id
        self.__stu_list.append(stu)
    def remove_student(self,id):
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
    def update_student(self,stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i],self.__stu_list[j] = self.__stu_list[j],self.__stu_list[i]

# 	界面视图类：StudentManagerView
# 		数据：逻辑控制对象__manager
# 		行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
# 输入学生__input_students，输出学生__output_students，
# 删除学生__delete_student，修改学生信息__modify_student
class StudentManagerView():
    def __init__(self):
        self.__manager = StudentManagerController()
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
    def main(self):
        choice = None
        while choice != 0:
            self.__display_menu()
            choice = input('请输入选项:')
            if choice == '0':
                print('谢谢使用,退出!')
                break
            elif choice == '1':
                self.__input_students()
            elif choice == '2':
                self.__output_students()
            elif choice == '3':
                self.__delete_student()
            elif choice == '4':
                self.__modify_student()
            elif choice == '5':
                self.__sort_by_score()
            else:
                print('请重新输入选项!')
    def __input_students(self):
        name = input('请输入学生姓名:')
        age = int(input('请输入学生年龄:'))
        score = int(input('请输入学生成绩:'))
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)
        print('添加学生信息成功!')
    def __output_students(self):
        print('学生信息:')
        for item in self.__manager.stu_list:
            print(item.id,item.name,item.age,item.score)
    def __delete_student(self):
        stu_id = int(input('请输入学生编号:'))
        if self.__manager.remove_student(stu_id):
            print('删除学生信息成功!')
        else:
            print('删除学生信息失败!')
    def __modify_student(self):
        id = int(input('请输入需要修改的学生ID:'))
        name = input('请输入修改后学生姓名:')
        age = int(input('请输入修改后学生年龄:'))
        score = int(input('请输入修改后学生成绩:'))
        stu = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu):
            print('修改学生信息成功!')
        else:
            print('修改学生信息失败!')
    def __sort_by_score(self):
        self.__manager.order_by_score()
        print('排序成功!')

view = StudentManagerView()
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
# # #manger.stu_list列表 保存学生对象
# # print(manger.stu_list[1].name)
# # #测试删除学员
# manger.remove_student(1004)
# for item in manger.stu_list:
#     print('删除后:',item.id,item.name)
# # #测试修改学员
# manger.update_student(StudentModel('娘子',19,80,1001))
# for item in manger.stu_list:
#     print('修改后:',item.id,item.name,item.age,item.score)
# # #测试按成绩排序
# manger.order_by_score()
# for item in manger.stu_list:
#     print('按分数升序排列:',item.id,item.name,item.age,item.score)