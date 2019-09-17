import re

s = '热烈庆祝中华人民共和国建国70周年，1949-2019'
pattern = r'\d+'

#返回迭代对象
it = re.finditer(pattern,s)
for i in it:
    print(i.group())

#完全匹配
obj = re.fullmatch(r'.+',s)
print(obj.group())

#匹配开始
obj = re.match(r'\w',s)
print(obj.group())

#匹配第一处
obj = re.search(r'\d+',s)
print(obj.group())