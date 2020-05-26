#coding=utf-8
'''
《Python零基础入门10天搞定》https://chuanke.baidu.com/v4500746-178215-927115.html
这个是Python3版的
'''

number = 50
# 答案是50

flag = True
# 循环是否结束的标志

while flag:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        flag = False
        # 循环结束
    elif guess > number:
        print('No, it is a little higher than the correct number')
    else:
        print('No, it is a little lower than the correct number')
else:
    print('The while loop is over.')

print('Done')