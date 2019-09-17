import pygame
import sys
from pygame.locals import *

# 初始化Pygame
pygame.init()

size = width, hight = 600, 400
speed = [-2, 1]
bg = (255, 200, 255)  # RGB颜色

# clock = pygame.time.Clock()
# 创建指定大写的窗口
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption('不知火舞')

# 加载图片
turtle = pygame.image.load('nebula.jpg')
# 获得图像的位置矩形
position = turtle.get_rect()
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > hight:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 双缓冲
    # 更新图像
    screen.blit(turtle, position)  # bilt方法将一个图像覆盖到另一个图象上
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)

    # clock.tick(200)

# 什么是surface对象？
# pygame 用来表示图像的对象