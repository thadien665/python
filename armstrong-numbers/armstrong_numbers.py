def is_armstrong_number(number):
    # number_as_string = str(number)
    exp = len(str(number))
    summ = 0
    for sign in str(number):
        summ += int(sign)**exp
    return summ == number
