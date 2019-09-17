from tkinter import *
#基于Frame的Application类
class Aplication(Frame):
    def __init__(self,master):
        super(Aplication,self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()
    #创建小部件
    def create_widgets(self):
        self.bttn = Button(self)
        # self.bttn.configure(text = 'Total Click:0')
        self.bttn['text' ]= 'Total Click:0'
        #绑定能够事件计数器 设置command
        self.bttn['command'] = self.update_count
        self.bttn.grid()
    #创建事件计数器
    def update_count(self):
        self.bttn_clicks += 1
        # self.bttn.configure(text = 'Total Click:'+str(self.bttn_clicks))
        self.bttn['text'] = 'Total Click:'+str(self.bttn_clicks)
#程序主体
root = Tk()
root.title('GUI')
root.geometry('200x85')

app = Aplication(root)

root.mainloop()



