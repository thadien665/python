def steps(number):
    steps = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            steps += 1
        else:
            number = 3 * number + 1
            steps += 1

    return steps