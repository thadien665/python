def response(hey_bob):

    def is_upper_question():
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."

    def not_question():
        if hey_bob.isupper():
            return "Whoa, chill out!"
        elif hey_bob.isspace() or len(hey_bob) == 0:
            return "Fine. Be that way!"
        else:
            return "Whatever."


    if "?" in hey_bob:
        index_qmark = hey_bob.index("?")
        if index_qmark == len(hey_bob) - 1:
            return is_upper_question()
        else:
            ending_string = hey_bob[index_qmark + 1:]
            if ending_string.isspace():
                return is_upper_question()
            else: #not a question
                return not_question()
    else:
        return not_question()



