"""
消除类游戏是深受大众欢迎的一种游戏，游戏在一个包含有n行m列的游戏棋盘上进行，棋盘的每一行每一列的方格上
放着一个有颜色的棋子，当一行或一列上有连续三个或更多的相同颜色的棋子时，这些棋子都被消除。当有多处可以
被消除时，这些地方的棋子将同时被消除。

现在给定一个n行m列的棋盘，棋盘中的每一个方格上有一个棋子（用数字1-9表示各种颜色的棋子），请给出经过消除后的棋盘。

请注意：一个棋子可能在某一行和某一列同时被消除。

【输入形式】

从标准输入读取数据，第一行包含两个整数n和m，分别表示棋盘的行数和列数（
行数和列数都大于等于3，小于等于9），以一个空格分隔这两个整数。

接下来输入n行，每行m个整数，用一个空格分隔各个整数，这些整数分别表示
每一个方格中棋子的颜色（大于等于1，小于等于9）。

【输出形式】

向标准输出上输出n行，每行m个整数，相邻整数之间以一个空格分隔，表示经过消除后的棋盘。
如果一个方格中的棋子被消除，则对应的方格输出数字0，否则输出代表原棋子颜色的整数。每行最后一个整数后也要有一个空格。

"""

n, m = [int(x) for x in input().split()]  # 将n,m 转换为 int 类型

checkerboard = []

falg_list = [[0] * m for i in range(n)]  # 创建一个n行 m列的列表,初始值为 0

for i in range(n):
    temp = input().split()
    checkerboard.append(temp)

for i in range(n):
    for j in range(m):
        # 检查 每一列 是否有可以消除的，有的话，就设置 falg_list[i][j] 的值为 1
        if i + 1 < n and i + 2 < n:
            if checkerboard[i][j] == checkerboard[i + 1][j] and checkerboard[i][j] == checkerboard[i + 2][j]:
                falg_list[i][j] = 1
                falg_list[i + 1][j] = 1
                falg_list[i + 2][j] = 1

        # 检查 每一行 是否有可以消除的，有的话，就设置 falg_list[i][j] 的值为 1
        if j + 1 < m and j + 2 < m:
            if checkerboard[i][j] == checkerboard[i][j + 1] and checkerboard[i][j] == checkerboard[i][j + 2]:
                falg_list[i][j] = 1
                falg_list[i][j + 1] = 1
                falg_list[i][j + 2] = 1

# 打印消除后的棋盘
for i in range(n):
    for j in range(m):
        # falg_list[i][j] 的值为 1 ，说明棋盘中的数字已被消除
        if falg_list[i][j] == 1:
            checkerboard[i][j] = 0
        print(checkerboard[i][j], end=' ')
    print()
