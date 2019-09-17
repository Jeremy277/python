from tkinter import *
#基于Frame的Application类
class Aplication(Frame):
    # def __init__(self,master):
    def __init__(self,master=None):
        # super(Aplication,self).__init__()
        super().__init__(master)
        # 调用超类的构造器，使Application对象能得到超类中已经实现的方法
        # 注意 这里传入的参数是当前Application的对象容器root 之后调用这个对象
        # 的create_widget()方法
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.bttn1 = Button(self,text = '无用按钮')
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = '我也是')

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3['text'] = '这里也是'

# root = Tk()
# root.title('GUI')
# # root.geometry('200x85')
#
app = Aplication()
app.master.title='GUI'

app.mainloop()



