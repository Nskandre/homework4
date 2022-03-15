def fizz_buzz(start, stop):
    '''Sums the numbers of range that are divisible on 3 and 5

    :param start: int, required
    :param stop: int, required
    :return: sums the numbers of range from start till stop 
    that are divisible on 3 and 5
    '''
    result_fizz_buzz = 0
    for i in range(start, stop+1):
        if i % 3 == 0 and i % 5 == 0:
            result_fizz_buzz += i
    return result_fizz_buzz


# print(fizz_buzz(1000, 20000))


def plural_form(num, word1 = '', word2 = '', word3 = ''):
    '''Returns correct word for number

    :param num: int, required
    :param word1:
    :param word2:
    :param word3:
    :return: one of the words that correct for num
    '''
    list1 = list(range(10))
    result_plural_form = ''
    if str(num)[-1] == '0' or len(str(num)) == 2 or str(num)[-1] in '56789':
        result_plural_form = word3
    elif str(num)[-1] == '1':
        result_plural_form = word1
    else:
        result_plural_form = word2
    
    return result_plural_form

print(12, plural_form(12, 'студент', 'студента', 'студентов'))