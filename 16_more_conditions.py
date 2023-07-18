# BMI = 体重 / (身高 ** 2)

weight = float(input('请输入你的体重(KG)：'))
hight = float(input('请输入你的身高(M):'))
BMI = weight / hight ** 2
print('BMI为：' + str(BMI))

# 肥胖 BMI > 30
# 偏胖 30 >= BMI > 25
# 正常 25 >= BMI > 18.5
# 偏廋 18.5 >= BMI
if BMI > 30:
    print('肥胖！')
elif 30 >= BMI and BMI > 25:
    print('偏胖')
elif 25 >= BMI > 18.5:
    print('正常')
elif 18.5 >= BMI:
    print('偏廋')