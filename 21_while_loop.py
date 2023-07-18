print('求平均值！')

count = 0
total = 0

user_input = input('请输入数字(输入"q"，结束输入)：')
while user_input != 'q':
    total += float(user_input)
    count += 1
    user_input = input('请输入数字(输入"q"，结束输入)：')

if count > 0:
    avg = total / count
    print('总个数：' + str(count) + '平均值为：' + str(avg))
else:
    print('请输入数据！')