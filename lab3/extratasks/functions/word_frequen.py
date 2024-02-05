def word_frequen(string):
    words_list = string.split()
    words_dict = {}

    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict
print(word_frequen("Hello my frieds!How are you today?"))