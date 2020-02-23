import random, sys
import numpy as np

def Reading_from_File_for_Polinom(file, n, k):

    result = []
    choise = int(input('Введите число, соответствующее его степени: \n1)deq(g(x)) = 3;\n2)deq(g(x)) = 4;\n3)deq(g(x)) = 5;\n4)deq(g(x)) = 6;\n5)deq(g(x)) = 7;\n6)deq(g(x)) = 8;\nВаш выбор: '))

    f = open(file, 'r', encoding='UTF-8')
    for str_1 in f.readlines():
        str_1 = str_1.strip().split(';')
        if choise == int(str_1[0]):
            if n-k-2 == int(str_1[0]):
                str_1 = str_1[1]
                break
    f.close()

    for j in range(len(str_1)):
        if str_1[j] != ' ':
           result.append(int(str_1[j]))

    for i in range(k-1):
        result.append(0)

    return result

def Reading_from_File(file):

    f = open(file, 'r', encoding='UTF-8')
    str_1 = f.read()
    f.close()

    prev = ''

    for i in range(len(str_1)):
        temp = bin(ord(str_1[i]))[2:]
        while len(temp) % 8 != 0:
            temp = '0' + temp
        prev += temp

    return prev

def Blocking(prev, k):

    buff_list = []
    count = int(0)
    while len(prev) % k != 0:
        prev += '0'
        count += 1
    for i in range(0,len(prev),k):
        buff_list.append(prev[i:i+k])
    temp = bin(count)[2:]
    while len(temp) % k != 0:
        temp = '0' + temp
    buff_list.append(temp)
    for i in range(len(buff_list)):
        buff_list[i] = np.array(list(map(int, buff_list[i])))
    return np.array(buff_list)

def Built_Matrix_G(polinom, n, k):
    res = []
    buff_list = []

    res.append(polinom)

    for j in range(1,k):
        for i in range(n):
            buff_list.append(polinom[i])
        buff_list = buff_list[:-1]
        buff_list.insert(0, 0)
        polinom = buff_list
        res.append(buff_list)
        buff_list = []

    return np.array(res)

def MultiField(vector1, vector2):
    buff_list = []
    buff = int()
    if len(vector1) != len(vector2):
        return -1
    for i in range(len(vector1)):
        buff_list.append((vector1[i] * vector2[i]) % 2)
    for i in buff_list:
        buff += i
    return buff % 2

def Table_info_words(k):
    res = []
    a = [0 for i in range(k)]
    res.append(a[:])
    for m in range(pow(2, k) - 1):
        buff = k - 1
        while 1:
            a[buff] += 1
            if (a[buff] % 2 == 0):
                a[buff] = 0
                buff -= 1
            else: break
        res.append(a[:])
    return res

def Code_Table_Words(Inf_Tab, Gsys):
    result = []
    mass = []

    for c in range(len(Inf_Tab)):
        for j in range(len(np.transpose(Gsys))):
            mass.append(MultiField(Inf_Tab[c], np.transpose(Gsys)[j]))
        result.append(mass[:])
        mass = []

    return result

def GetIndex(list):

    length = len(list)
    result = 0
    for i in range(length):
        result += list[length-i-1] * 2 ** i
    return result

def Interference_Detection(vector, n, P_User_stir, P_User_good):

    file = open('Results of the course.txt', 'a', encoding='UTF-8')
    buff_list = []
    count_for_stir = int(0)
    print('Вероятность появления символа: ')
    for i in range(len(vector)):
        r = random.uniform(0,1)
        print('в момент времени t = ' + str(i) + ' равна: ' + str(r))
        if 0 <= r <= P_User_good:
            buff_list.append(str(vector[i]))
        else:
            buff_list.append('*')
            count_for_stir += 1
    res_stir = (count_for_stir / n) * P_User_stir
    print('Вектор, полученный из канала связи, имеет вид: ', buff_list)
    print('Реальная вероятность стирания: ' + str(res_stir))
    file.write('\nРеальная вероятность стирания: ' + str(res_stir) + '\n')
    file.write('\nВектор, полученный из канала связи, имеет вид: \n')
    file.write(str(buff_list) + '\n')
    file.close()
    return np.array(buff_list)

def MinDiff(code_vector, code_table):

    buff_list = []
    buff_count = int()
    if len(code_vector) != len(code_table[0]):
        return -1
    for i in code_table:
        for j in range(len(i)):
            if code_vector[j] != str(i[j]):
                buff_count += 1
        buff_list.append(buff_count)
        buff_count = int()
    min = buff_list[0]
    index = 0
    for i in range(len(buff_list)):
        if buff_list[i] < min:
            min = buff_list[i]
            index = i
    return index

def MinHDist(code_vector, info_table, code_table):
    file = open('Results of the course.txt', 'a', encoding='UTF-8')
    file.write('\nДекодируемый вектор: \n')
    file.write(str(info_table[MinDiff(code_vector, code_table)]) + '\n' + '______________________________________________________')
    file.close()
    decode = info_table[MinDiff(code_vector, code_table)]
    print('Декодируемый вектор: ', decode)
    return decode