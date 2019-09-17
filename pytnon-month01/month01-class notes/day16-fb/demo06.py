#自定义异常类
class AgeError(Exception):
    def __init__(self,message,code,id):
        #错误信息
        self.message = message
        self.code = code
        self.id = id
