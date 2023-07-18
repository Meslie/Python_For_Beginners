# BMI = 体重 / (身高 ** 2)

weight = float(input('请输入你的体重(KG)：'))
hight = float(input('请输入你的身高(M):'))
BMI = weight / hight ** 2
print('BMI为：' + str(BMI))