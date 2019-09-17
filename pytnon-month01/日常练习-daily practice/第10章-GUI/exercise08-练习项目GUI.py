#mad lib 在用户帮助下编写故事程序 需要用户提供人名 名词 动词
from tkinter import *
#基于Frame的Application类  定义构造器初始化新的Application对象
class Aplication(Frame):
    def __init__(self,master=None):
        # super(Aplication,self).__init__(master)
        super().__init__(master)
        # self.master = master#AttributeError: 'Aplication' object has no attribute 'tk'
        # super().__init__()
        self.grid()
        self.create_widgets()
    #创建小部件
    def create_widgets(self):
        Label(self,text='请输入故事的基本要素.').\
            grid(row=0,column=0,columnspan=2,sticky=W)
        #创建 人名 名词 动词 的标签和文本框
        Label(self, text='人名:'). \
            grid(row=1, column=0,sticky=W)
        self.person_txt = Entry(self)
        self.person_txt.grid(row=1, column=1,sticky=W)
        Label(self, text='名词:'). \
            grid(row=2, column=0,sticky=W)
        self.noun_txt = Entry(self)
        self.noun_txt.grid(row=2, column=1, sticky=W)
        Label(self, text='动词:'). \
            grid(row=3, column=0,sticky=W)
        self.verb_txt = Entry(self)
        self.verb_txt.grid(row=3, column=1, sticky=W)
        #创建用于形容词的复选框
        Label(self, text='形容词:'). \
            grid(row=4, column=0, sticky=W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = '渴望的',
                    variable = self.is_itchy,
                    ).grid(row=4, column=1, sticky=W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text='快乐的',
                    variable=self.is_joyous,
                    ).grid(row=4, column=2, sticky=W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text='激动的',
                    variable=self.is_electric,
                    ).grid(row=4, column=3, sticky=W)
        #创建用于身体部位的标签 变量以及单选框
        Label(self,text = '身体部分:').grid(row=5, column=0, sticky=W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ['肚脐','大脚趾','太阳穴']
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part).grid(row=5, column=column, sticky=W)
            column += 1
        #创建提交按钮
        Button(self,text = '单击生成故事',command = self.tell_story).\
            grid(row=6, column=0, sticky=W)
        #创建用于显示结果的文本框
        self.story_txt = Text(self,width=75,height=10,wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=3)

    def tell_story(self):
        person = self.person_txt.get()
        noun = self.noun_txt.get()
        verb = self.verb_txt.get()
        adjectives = ''
        if self.is_itchy.get():
            adjectives += '渴望的'
        if self.is_joyous.get():
            adjectives += '快乐的'
        if self.is_electric.get():
            adjectives += '激动的'
        body_part = self.body_part.get()

        #创建故事
        story = '有一个著名的探险者'
        story += person
        story += '.最近他在极地地区发现了一座只存在与神话中的城市'
        story += noun.title()
        story += '根据神话所述'
        story += noun
        story += '这个城市是由一个'
        story += adjectives
        story += '勇者建立的,他'
        story += verb
        story += '存在于城市周边的恶魔.'
        story += person
        story += '指着自己的'
        story += body_part
        story += ',决定一定发掘出勇者与恶魔最后的故事.'
        #显示故事
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

#程序主体
root = Tk()
root.title('GUI')
root.geometry('700x480')
app = Aplication(root)
root.mainloop()

#另一种:主程序
# app = Aplication()
# app.master.title='GUI'
#
# app.mainloop()


