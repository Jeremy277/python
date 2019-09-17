#将tkinter的全部内容引入到该程序中
from tkinter import *
#创建根窗体 不需要在类名 Tk前加模块名
root = Tk()
#根窗体标题
root.title('simple GUI')
#设置窗体大小 以字符'x'隔开 单位像素
root.geometry('200x200')
#在根窗体上创建一个框架,用来承载其他小部件
#必须将小部件的容器(master,用于承载这个小部件的东西)传给构造器
#这里将root传给这个框架的构造器,于是新框架被放到root窗体
app = Frame(root)
#grid()是所有小部件都有的方法,它关联一个布局控制器
app.grid()
#在框架中创建一个标签
lb1 = Label(app,text = '我是标签!')
#调用grid()方法
lb1.grid()
#1.在框架中创建一个按钮
bttn1 = Button(app,text = '无用按钮')
bttn1.grid()
#2.创建app框架中的第二个按钮
bttn2 = Button(app)
bttn2.grid()
#在小部件被创建出来后,仍可以对其进行修改configure()
bttn2.configure(text = '我也是')
#3.创建app框架中的第三个按钮
bttn3 = Button(app)
bttn3.grid()
#使用类似于字典的方式来访问按钮的'text'选项,该选项的名字就是键(字符串形式)
bttn3['text'] = '这里也是'
#启动事件循环
root.mainloop()