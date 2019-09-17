# from usl import *
# import student_system_model.usl as u
# from student_system_model import usl
# from student_system_model.usl import StudentManagerView
#路径必须为主目录 否则会报错
from project.student_system_model.usl import StudentManagerView

view = StudentManagerView()
# view.display_menu()
view.main()