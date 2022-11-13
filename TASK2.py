def get_count_char(str_):
    dct = dict()
    lst = list()
    for i in str_.lower():
        if i.isalpha():
            lst.append(i)
            dct[i] = lst.count(i)
    return dct


def percent_to_all(dictionary: dict):
    sum_of_all = sum(dictionary.values())
    new_dictionary = dict()
    for k, v in dictionary.items():
        new_dictionary[k] = round((v / sum_of_all * 100), 2)
    return new_dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent_to_all(get_count_char(main_str)))
