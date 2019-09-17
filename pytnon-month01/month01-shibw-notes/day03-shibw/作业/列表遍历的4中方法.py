list = ['html', 'js', 'css', 'python']

# 方法1
print ('遍历列表方法1：')
for i in list:
    print ("序号：%s   值：%s" % (list.index(i) + 1, i))

print ('\n遍历列表方法2：')
# # 方法2
# for i in range(len(list)):
#     print ("序号：%s   值：%s" % (i + 1, list[i]))
#
# # 方法3
print ('\n遍历列表方法3：')
for i, val in enumerate(list):
    print (("序号：%s   值：%s" % (i + 1, val)))
# 方法3 enumerate()方法，通过查看help()函数来查看
# enumerate()函数的第二个参数只是改变了序号的起始值，并没有改变其他
print ('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
for i, val in enumerate(list, 2):
    print ("序号：%s   值：%s" % (i + 1, val))