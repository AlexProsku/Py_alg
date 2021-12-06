"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""

from collections import Counter


def hafman(string):
    if len(string) == 0:
        return f'Передана пустая строка'
    cnt_un_chr = []
    for i in Counter(string).items():
        cnt_un_chr.append([i[1], i[0]])
    cnt_un_chr = sorted(cnt_un_chr)
    if len(cnt_un_chr) == 1:
        return '0'
    while len(cnt_un_chr) > 1:
        position = cnt_un_chr[0][0] + cnt_un_chr[1][0]
        spam = [position, [cnt_un_chr[0][1], cnt_un_chr[1][1]]]
        cnt_un_chr = cnt_un_chr[2:]
        if len(cnt_un_chr) == 0:
            cnt_un_chr = [spam]
        elif position <= cnt_un_chr[0][0]:
            cnt_un_chr = [spam] + cnt_un_chr
        else:
            for i in range(len(cnt_un_chr)):
                if position <= cnt_un_chr[i][0] and i < len(cnt_un_chr):
                    cnt_un_chr = cnt_un_chr[:i] + [spam] + cnt_un_chr[i:]
                    break
                elif i == len(cnt_un_chr) - 1:
                    cnt_un_chr.append(spam)
    cnt_un_chr = cnt_un_chr[0][1]
    haf_code = [['0', cnt_un_chr[0]], ['1', cnt_un_chr[1]]]
    list_type = True
    while list_type:
        tmp_list = []
        list_type = False
        for elements in haf_code:
            if type(elements[1]) == list:
                for idx, el in enumerate(elements[1]):
                    tmp_list += [[elements[0] + str(idx), el]]
                    if type(el) == list:
                        list_type = True
            else:
                tmp_list += [elements]
        haf_code = tmp_list

    haf_decode_dict = {}
    for i in haf_code:
        haf_decode_dict[i[1]] = i[0]

    str_decode = ''
    for char in string:
        str_decode += haf_decode_dict.get(char) + ' '

    return str_decode


a = 'beep boop beer!'
print(hafman(a))
