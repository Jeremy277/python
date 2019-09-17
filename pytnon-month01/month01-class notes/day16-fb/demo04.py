#分苹果
def div_apple(apple_count):
    person_count = int(input('请输入人数:'))
    res = apple_count/person_count
    print('每个人%.2f个苹果' % res)
#ZeroDivisionError   ValueError
if __name__ == '__main__':
    try:
        div_apple(10)
    except ValueError:
        print('人数必须为整数')
    except ZeroDivisionError :
        print('人数不能为0')
    except KeyboardInterrupt :
        print('用户中断输入')
    except Exception :
        print('未知错误')
    else:
        print('无异常发生')
    finally:
        print('程序结束')


