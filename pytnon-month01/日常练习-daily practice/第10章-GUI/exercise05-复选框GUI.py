#复选框允许用户从一组选项中选取任意数量的的选项
from tkinter import *
#基于Frame的Application类
class Aplication(Frame):
    def __init__(self,master):
        super(Aplication,self).__init__(master)
        self.grid()
        self.create_widgets()
    #创建小部件
    def create_widgets(self):
       #创建描述标签 在tkinter中所有GUI元素都通过容器跟程序保持联系
        #如果不需要直接访问某个小部件,就不需要将其赋值给变量
        Label(self,text = '请输入你喜欢的电影种类')\
            .grid(row = 0,column = 0,sticky=W)
        #创建操作说明标签
        Label(self,text = '请选择:').grid(row = 1,column = 0,sticky=W)
        #创建复选框   BooleanVar类
        #任何复选框都要有一个特殊对象与之关联,以便自动反应该复选框的状态
        #1.创建喜剧复选框
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
            text = 'comedy',
            variable = self.likes_comedy,
            command = self.update_text#绑定
        ).grid(row = 2,column = 0,sticky = W)
       # 2.创建戏剧复选框
        self.likes_drama = BooleanVar()
        Checkbutton(self,
            text='drama',
            variable=self.likes_drama,
            command=self.update_text
            ).grid(row=3, column=0, sticky=W)
       # 3.创建浪漫复选框
        self.likes_romance= BooleanVar()
        Checkbutton(self,
            text='romance',
            variable=self.likes_romance,
            command=self.update_text
            ).grid(row=4, column=0, sticky=W)
        #创建文本框
        self.result_text = Text(self,width=40,height = 5,wrap=WORD)
        self.result_text.grid(row=5,column=0,columnspan=3)
    #根据复选框选取状态更新文本内容
    def update_text(self):
        likes = ''
        if self.likes_comedy.get():
            likes += '你喜欢喜剧电影'
        if self.likes_drama.get():
            likes += '你喜欢戏剧电影'
        if self.likes_romance.get():
            likes += '你喜欢浪漫电影'

        self.result_text.delete(0.0,END)
        self.result_text.insert(0.0,likes)



#程序主体
root = Tk()
root.title('GUI')
# root.geometry('300x150')

app = Aplication(root)

root.mainloop()



