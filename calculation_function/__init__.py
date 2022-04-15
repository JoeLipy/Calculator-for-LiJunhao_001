global u


# 包含字符串?
def contains_str(str_input, contains_char):
    for i in range(len(str(str_input))):
        if str(str_input)[i] == contains_char:
            return True
    return False


# 数据为可整数化str就返回整数，数据为可浮点数化str就返回浮点数
def str_type_return(str_input):
    if contains_str(str_input, '.'):
        return float(str_input)
    else:
        return int(str_input)


# 加法(整数)
def add_int(a, b):
    return int(a) + int(b)


# 减法(整数)
def subtraction_int(a, b):
    return int(a) - int(b)


# 乘法(整数)
def multiplication_int(a, b):
    return int(a) * int(b)


# 除法
def division_int(a, b):
    return int(int(a) / int(b))  # 防止出现浮点数


# 求余
def surplus_int(a, b):
    return int(a) % int(b)


# 加法(浮点数)
def add_float(a, b):
    return float(a) + float(b)


# 减法(浮点数)
def subtraction_float(a, b):
    return float(a) - float(b)


# 乘法(浮点数)
def multiplication_float(a, b):
    return float(a) * float(b)


# 连续加法
def continuous_addition(str_input):
    global u
    num_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '+':
            num_2 += 1
    p = str_input.split('+')
    if num_2 == 1:
        if contains_str(str_type_return(p[0]) - str_type_return(p[1]), '.'):
            return add_float(float(p[0]), float(p[1]))
        else:
            return add_int(int(p[0]), int(p[1]))
    else:
        for i in range(num_2):
            if str_input[i] == '+':
                s = 1
                if contains_str(str_type_return(p[i]) - str_type_return(p[i + 1]), '.'):
                    temp = add_float(float(p[i]), float(p[i + 1]))
                else:
                    temp = add_int(int(p[i]), int(p[i + 1]))
                for d in range(num_2 - 1):
                    temp = temp + int(p[d])
                    u = temp
        return u


# 连续减法
def continuous_subtraction(str_input):
    global u
    subtraction_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '-':
            subtraction_2 += 1
    p = str_input.split('-')
    if subtraction_2 == 1:
        if contains_str(str_type_return(p[0]) - str_type_return(p[1]), '.'):
            return subtraction_float(float(p[0]), float(p[1]))
        else:
            return subtraction_int(int(p[0]), int(p[1]))
    elif subtraction_2 > 1:
        for i in range(subtraction_2):
            if str_input[i] == '-':
                s = 1
                if contains_str(str_type_return(p[i]) - str_type_return(p[i + 1]), '.'):
                    temp = subtraction_float(float(p[i]), float(p[i + 1]))
                else:
                    temp = subtraction_int(int(p[i]), int(p[i + 1]))
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
    if multiplication_2 == 1:
        if contains_str(p[0] * p[1], '.'):
            return multiplication_float(p[0], p[1])
        else:
            return multiplication_int(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '*':
                s = 1
                if contains_str(str_type_return(p[i]) - str_type_return(p[i + 1]), '.'):
                    temp = multiplication_float(float(p[0]), float(p[1]))
                else:
                    temp = multiplication_int(int(p[0]), int(p[1]))
                for d in range(multiplication_2 - 1):
                    s += 1
                    temp = temp * int(p[s])
                    u = temp
        return u


# 连续除法
def continuous_division(str_input):
    global u
    division_2 = 0
    for g in range(len(str_input)):
        if str_input[g] == '/':
            division_2 += 1
    p = str_input.split('/')
    if division_2 == 1:
        return division_int(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '/':
                s = 1
                temp = division_int(float(p[0]), float(p[1]))
                for d in range(division_2 - 1):
                    s += 1
                    temp = temp / int(p[s])
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
        return surplus_int(p[0], p[1])
    else:
        for i in range(len(str_input)):
            if str_input[i] == '/':
                s = 1
                temp = surplus_int(float(p[0]), float(p[1]))
                for d in range(surplus_2 - 1):
                    s += 1
                    temp = temp % int(p[s])
                    u = temp
        return u
