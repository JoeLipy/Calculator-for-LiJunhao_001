# 加法
def add(a, b):
    return int(a) + int(b)


# 减法
def subtraction(a, b):
    return int(a) - int(b)


# 除法
def division(a, b):
    return int(int(a) / int(b))  # 防止出现浮点数


# 求余
def surplus(a, b):
    return int(a) % int(b)


# 乘法
def multiplication(a, b):
    return int(a) * int(b)


# 连续加法
def continuous_addition(str_input):
    global u
    num_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '+':
            num_2 += 1
    p = str_input.split('+')
    print(p)
    if num_2 == 1:
        return add(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '+':
                p = str_input.split('+')
                s = 1
                temp = add(float(p[0]), float(p[1]))
                for d in range(num_2 - 1):
                    s += 1
                    temp = temp + int(p[s])
                    if d > 1:
                        u = add(temp, u)
                    else:
                        u = temp
        return u


# 连续减法
def continuous_subtraction(str_input):
    global u
    subtraction_2 = 0
    for f in range(len(str_input)):
        if str_input[f] == '-':
            subtraction_2 += 1
        p = str_input.split('-')
        print(p)
        if subtraction_2 == 1:
            return subtraction(p[0], p[1])
        else:
            for i in range(len(str_input)):
                if str_input[i] == '-':
                    p = str_input.split('-')
                    s = 1
                    temp = subtraction(float(p[0]), float(p[1]))
                    for d in range(subtraction_2 - 1):
                        s += 1
                        temp = temp - int(p[s])
                        if d > 1:
                            u = subtraction(temp, u)
                        else:
                            u = temp
            return u


# 连续乘法
def continuous_multiplication(str_input):
    global u
    multiplication_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '*':
            multiplication_2 += 1
    p = str_input.split('*')
    print(p, multiplication_2)
    if multiplication_2 == 1:
        return multiplication(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '*':
                s = 1
                temp = multiplication(float(p[0]), float(p[1]))
                for d in range(multiplication_2):
                    s += 1
                    print(s)
                    temp = temp * int(p[s])
                    if d > 1:
                        u = multiplication(temp, u)
                    else:
                        u = temp
            break
        return 0


# 连续除法
def continuous_division(str_input):
    global u
    division_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '/':
            division_2 += 1
    p = str_input.split('/')
    print(p)
    if division_2 == 1:
        return division(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '/':
                s = 1
                temp = division(float(p[0]), float(p[1]))
                for d in range(division_2 - 1):
                    s += 1
                    temp = temp / int(p[s])
                    if d > 1:
                        u = division(temp, u)
                    else:
                        u = temp
        return u


# 连续求余
def continuous_surplus(str_input):
    global u
    surplus_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '/':
            surplus_2 += 1
    p = str_input.split('/')
    if surplus_2 == 1:
        return surplus(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '/':
                s = 1
                temp = surplus(float(p[0]), float(p[1]))
                for d in range(surplus_2 - 1):
                    s += 1
                    temp = temp % int(p[s])
                    if d > 1:
                        u = surplus(temp, u)
                    else:
                        u = temp
            break
    return u


k = 0
print('欢迎使用jtr计算器')
print('制作者:Lijunhao_001')
# 重复执行询问和输出
while True:
    formula = input('算式:')
    for y in range(len(formula)):
        if formula[y] == '+':
            u = continuous_addition(formula)
            print(formula, '=', u)
            break
        elif formula[y] == '-':
            u = continuous_subtraction(formula)
            print(formula, '=', u)
            break
        elif formula[y] == '*':
            u = continuous_multiplication(formula)
            print(formula, '=', u)
            break
        elif formula[y] == '/':
            u = int(continuous_division(formula))
            t = int(continuous_surplus(formula))
            print(formula, '=', u, '......', t)
            break
    u = []
