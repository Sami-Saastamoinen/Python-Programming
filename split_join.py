def my_split(sentence, separator):
    words = []
    temp_string = ""
    for i in sentence:
        if i != separator:
            temp_string += i
        elif i == separator:
            words.append(temp_string)
            temp_string = ""
    words.append(temp_string)

    return words


def my_join(words, separator):
    sentence = ""
    for i in words[:-1]:
        sentence += i + separator
    sentence += words[-1]

    return sentence


def main():
    sentence = str(input("Write a sentence:"))
    print(my_join(my_split(sentence, ' '), ','))
    print(my_join(my_split(sentence, ' '), '\n'))


if __name__ == "__main__":
    main()
