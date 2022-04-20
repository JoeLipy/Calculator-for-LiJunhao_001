from calculation_function import *

k = 0
print('welcome to jtr calculator')
print('maker:LiJunhao_001')
# Repeat query and output
while True:
    formula = input('formula:')
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
