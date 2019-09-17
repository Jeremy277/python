#单选框 只允许在一组选项中选取一个
from tkinter import *
#基于Frame的Application类  定义构造器初始化新的Application对象
class Aplication(Frame):
    def __init__(self,master):
        super(Aplication,self).__init__(master)
        self.grid()
        self.create_widgets()
    #创建小部件
    def create_widgets(self):
        Label(self,text = '请输入你喜欢的电影种类')\
            .grid(row = 0,column = 0,sticky=W)
        #创建操作说明标签
        Label(self,text = '请选择1个:').grid(row = 1,column = 0,sticky=W)
        #创建单选框
        #一组单选框只需共享一个用于说明'选中'的特殊对象
        #该对象是StringVar类
        #创建共享变量  用set()方法将其初始值设为None
        self.favorite = StringVar()
        self.favorite.set(None)
        #1.创建comedy单选框
        #当Comedy被选中时,
        # 由self.favorite所引用的StringVar存储字符串'comedy'
        Radiobutton(self,
                    text = 'Comedy',
                    variable = self.favorite,
                    value = 'comedy',
                    command = self.update_text
        ).grid(row = 2,column = 0,sticky=W)
        # 2.创建drama单选框
        Radiobutton(self,
                    text='Drama',
                    variable=self.favorite,
                    value='drama',
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)
        # 3.创建romance单选框
        Radiobutton(self,
                    text='Romance',
                    variable=self.favorite,
                    value='romance',
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)
        #创建用于显示结果的文本框
        self.result_text = Text(self,width = 40,height=5,wrap=WORD)
        self.result_text.grid(row = 5,column = 0,columnspan=3)
    def update_text(self):
        message = '你最喜欢的电影类型:'
        message += self.favorite.get()

        self.result_text.delete(0.0,END)
        self.result_text.insert(0.0,message)



#程序主体
root = Tk()
root.title('GUI')
# root.geometry('300x150')

app = Aplication(root)

root.mainloop()



