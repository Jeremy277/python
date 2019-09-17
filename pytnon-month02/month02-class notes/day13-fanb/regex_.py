'''
    regex
'''

import re

s = 'Alex:1994,Sunny:1996'
pattern = r'(\w+):(\d+)'
# pattern = '\w+:\d+'

#re模块调用
l = re.findall(pattern,s)
print(l)

#正则对象调用
regex = re.compile(pattern)
l = regex.findall(s,0,10)
print(l)

#打印内容：
# [('Alex', '1994'), ('Sunny', '1996')]
# [('Alex', '1994')]

# ['Alex:1994', 'Sunny:1996']
# ['Alex:1994']


#正则表达式内容切割字符串
l = re.split(r',',s)
print(l)  #['Alex:1994', 'Sunny:1996']

#替换目标
l = re.sub(r':','--',s) #Alex--1994,Sunny--1996
print(l)
l = re.subn(r':','--',s,4) #('Alex--1994,Sunny--1996', 2)
print(l)