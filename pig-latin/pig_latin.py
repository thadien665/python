def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    list_of_words = text.split(" ")
    final_result = ""
    for text in list_of_words:
        if text[0] in vowels or text[0:2] == "xr" or text[0:2] == "yt":
            final_result += text + "ay "
        else:
            if "y" in text and any(letter in text[:text.find("y")] for letter in vowels) == False and len(text[:text.find("y")]) != 0:
                part_to_move = text[:text.find("y")]
                final_result += text[text.find("y"):] + part_to_move + "ay "
            elif "qu" in text and any(letter in text[:text.find("qu")] for letter in vowels) == False:
                part_to_move = text[:text.find("qu")]
                final_result += text[text.find("qu")+2:] + part_to_move + "quay "
            else:
                index = 0
                while text[index] not in vowels:
                    index += 1
                part_to_move = text[:index]
                final_result += text[index:] + part_to_move + "ay "
    return final_result.strip()