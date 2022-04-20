from calculation_function import *

k = 0
print('欢迎使用jtr计算器')
print('制作者:LiJunhao_001')
# 重复执行询问和输出
while True:
    formula = input('算式:')
    for y in range(len(formula)):
        if formula[y] == '+':
            print(formula, '=', continuous_addition(formula))
            break
        elif formula[y] == '-':
            print(formula, '=', continuous_subtraction(formula))
            break
        elif formula[y] == '*':
            print(formula, '=', continuous_multiplication(formula))
            break
        elif formula[y] == '/':
            print(formula, '=', int(continuous_division(formula)), '......', int(continuous_surplus(formula)))
            break
