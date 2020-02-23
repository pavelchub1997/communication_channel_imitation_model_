import numpy as np
import os, gc

from functions_for_the_course import *

def main():

    n, k = map(int, input('Введите параметры кода(n, k): ').split(' '))
    pol = Reading_from_File_for_Polinom('polinom.txt', n, k)
    file = Reading_from_File('Input_text.txt')
    list_1 = Blocking(file, k)
    f = open('Results of the course.txt', 'w', encoding='UTF-8')
    f.write('Размер входного файла: \n')
    statinfo = os.stat('Input_text.txt')
    f.write(str(statinfo.st_size) + ' Байт' + '\n')
    f.write('\nПараметры кода(n, k): \n')
    f.write('(' + str(n) + ',' + str(k) + ')' + '\n')
    f.write('\nПолином в векторной форме имеет следующий вид: \n')
    f.write(str(pol) + '\n')
    G = Built_Matrix_G(pol, n, k)
    f.write('\nПорождающая матрица: \n')
    for i in G:
        f.write(str(i) + '\n')
    print('\nПорождающая матрица: ')
    print(G)
    I_T = Table_info_words(k)
    C_T = Code_Table_Words(I_T, G)
    print('\nТаблица информационных и кодовых слов: ')
    for i in range(len(I_T)):
        print('\t', I_T[i], '\t\t\t', C_T[i])
    f.write('\nТаблица информационных и кодовых слов: \n')
    for i in range(len(I_T)):
        f.write('\t' + str(I_T[i]) + '\t\t' + str(C_T[i]) + '\n')
    buff_list_1 = []
    for i in range(len(list_1)):
        buff_list_1.append(C_T[GetIndex(list_1[i])])
    print('\nПользователь, введите следующую вероятность: ')
    P_User_stir = float(input('Стирания: '))
    P_User_good = 1 - P_User_stir
    print('3) хорошей передачи: ', P_User_good)
    f.write('\nВведенные пользователем вероятности: \n')
    f.write('1)Стирания: ' + str(P_User_stir) + '\n')
    f.close()
    buff_list = []
    res = []
    for i in range(len(buff_list_1)):
        buff_list.append(Interference_Detection(buff_list_1[i], n, P_User_stir, P_User_good))
        res.append(MinHDist(buff_list[i], I_T, C_T))
    result = []
    for i in range(len(res)):
        for j in range(len(res[0])):
            result += str(res[i][j])
    for i in range(len(result)):
        result[i] = int(result[i])
    result = result[:-GetIndex(result[-k:])-k]
    Output_Text = ''
    for i in range(0, len(result), 8):
        Output_Text += (chr(GetIndex(result[i:i+8])))
    print(Output_Text)
main()