from sstack import SStack

st = SStack()

while True:
    exp = input('请输入逆波兰表达式：')
    tmp = exp.split(' ')
    for i in tmp:
        if i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.pop())#查看栈顶元素
        else:
            st.push(int(i))













