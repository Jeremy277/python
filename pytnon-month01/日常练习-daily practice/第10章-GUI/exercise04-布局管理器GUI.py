#使用Text（多行文本）和Entry(单行文本)小部件以及Grid布局管理器
from tkinter import *
#基于Frame的Application类
class Aplication(Frame):
    def __init__(self,master):
        super(Aplication,self).__init__(master)
        self.grid()
        self.create_widgets()
    #创建小部件
    def create_widgets(self):
        self.inst_lb1 = Label(self,text='输入正确密码就可以得到答案了')
        #Grid布局管理器指定这个标签的具体位置
        self.inst_lb1.grid(row =0,column = 0,columnspan = 2,sticky = W)
        #row column定义对象在容器中的具体位置,将容器想象为单元格。
        #columnspan 参数用于横跨多列防止小部件
        #rowspan 参数用于横跨多行防止小部件
        #sticky用于调整小部件在这个单元格中的位置 N S E W
        #创建表示密码的标签
        self.pw_lb1 = Label(self,text='password:')
        self.pw_lb1.grid(row=1,column=0,sticky=W)
        #创建用于接受密码的Entry小部件 单行文本框
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1,column = 1,sticky = W)
        #创建提交按钮  绑定到reveal()方法
        self.submit_bttn =Button(self,text='submit',command=self.reveal)
        self.submit_bttn.grid(row=2,column=0,sticky=W)
        #创建Text小部件
        #wrap决定文本的换行方式，WORD在文本框右边缘时自动换行
        # CHAR只将下一个字符放到下一行,NONE不换行
        self.secret_txt = Text(self,width=35,height=5,wrap=WORD)
        self.secret_txt.grid(row =3,column = 0,columnspan = 2,sticky = W)

    def reveal(self):
        #判断密码是否正确
        #调用Entry小部件的get()方法得到文本,#下述方法entry和text都有
        contents=self.pw_ent.get()
        if contents == 'secret':
            message = '这里有可以让你长生的秘诀，万古长青'
        else:
            message = '密码错误，你离长生的秘密还差的很远'
        #将其插入到text小部件，首先删除text小部件的所有文本
        self.secret_txt.delete(0.0,END)
        #表示从第0行第0列开始删除文本一直到文本末尾
        #insert接收插入位置和字符串
        self.secret_txt.insert(0.0,message)



#程序主体
root = Tk()
root.title('GUI')
root.geometry('300x150')

app = Aplication(root)

root.mainloop()



