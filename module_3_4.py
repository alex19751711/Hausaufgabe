def single_root_words (root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].lower().find(root_word.lower()) != -1 or root_word.lower().find(other_words[i].lower()) != -1:
            same_words.append(other_words[i])
            continue
    return same_words


result1 = single_root_words('riCH', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('disableMENT', 'Able', 'Mable', 'disabLE', 'bagel')
print(result1)
print(result2)
