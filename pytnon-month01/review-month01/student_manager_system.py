'''
    学生信息管理系统
'''
class StudentModel:
    def __init__(self,name,age,score,id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

class StudentController:
    __stu_id = 1000
    def __init__(self):
        self.__stu_list = []
    @property
    def stu_list(self):
        return self.__stu_list
    def add_student(self,stu):
        StudentController.__stu_id += 1
        stu.id = StudentController.__stu_id
        self.__stu_list.append(stu)
    def del_student(self,id):
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
    def sort_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[j].score:
                    self.__stu_list[i],self.__stu_list[j] = self.__stu_list[j],self.__stu_list[i]
class StudentControllerView:
    def __init__(self):
        self.manage = StudentController()
    def __display_menu(self):
        print('''
        学生信息管理系统 v1.1
        0)显示学生信息
        1)添加学生信息
        2)删除学生信息
        3)修改学生信息
        4)排序学生信息
        q)退出系统
        ''')
    def main(self):
        self.__display_menu()
        choice = None
        while choice != 'q':
            choice = input('请输入选项：')
            if choice == 'q':
                print('谢谢使用！')
                break
            elif choice == '0':
                self.__input_stu()
            elif choice == '1':
                self.__add_student()
            elif choice == '2':
                self.__del_stu()
            elif choice == '3':
                self.__update_stu()
            elif choice == '4':
                self.__sort_by_score()
            else:
                print('请输入正确选项！')
    def __add_student(self):
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        stu = StudentModel(name,age,score)
        self.manage.add_student(stu)
        print('添加学生信息成功！')
    def __input_stu(self):
        for item in self.manage.stu_list:
            print(item.id,item.name,item.age,item.score)
    def __del_stu(self):
        id = int(input('请输入需要删除的学生编号：'))
        if self.manage.del_student(id):
            print('删除学生信息成功！')
        else:
            print('请输入正确学生编号！')
    def __update_stu(self):
        id = int(input('请输入需要修改 的学生编号：'))
        name = input('请输入需要修改的学生姓名：')
        age = int(input('请输入需要修改的学生年龄：'))
        score = int(input('请输入需要修改的学生成绩：'))
        stu = StudentModel(name,age,score,id)
        if self.manage.update_student(stu):
            print('更新学生信息成功')
        else:
            print('请输入正确学生编号！')
    def __sort_by_score(self):
        self.manage.sort_by_score()
        print('排序成功')

if __name__ == '__main__':
    view = StudentControllerView()
    view.main()
    # s01 = StudentModel('张三',16,78)
    # s02 = StudentModel('李四',15,68)
    # s03 = StudentModel('王五',17,88)
    # manage = StudentController()
    # manage.add_student(s01)
    # manage.add_student(s02)
    # manage.add_student(s03)
    # # for item in manage.stu_list:
    # #     print(item.id,item.name,item.age,item.score)
    # manage.del_student(1002)
    # # for item in manage.stu_list:
    # #     print(item.id,item.name,item.age,item.score)
    # manage.add_student(s02)
    # s03 = StudentModel('娘子',18,99,1004)
    # manage.update_student(s03)
    # # for item in manage.stu_list:
    # #     print(item.id,item.name,item.age,item.score)
    # manage.sort_by_score()
    # # for item in manage.stu_list:
    # #     print(item.id,item.name,item.age,item.score)



