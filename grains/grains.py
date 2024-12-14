def square(number):
    if number <=0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    else:
        return 2**(number - 1)



def total():
    summ = 0
    for i in range(1, 65):
        summ += square(i)
    return summ

