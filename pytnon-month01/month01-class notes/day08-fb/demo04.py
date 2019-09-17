
# a = 100

def change():
    # a = 10
    def inner_fun():
        # a =1
        print(a)
    inner_fun()
    print(a)
# print(a)

change()