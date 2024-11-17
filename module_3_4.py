def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        lower_oth_words = word.lower()
        if lower_oth_words in root_word:
            same_words.append(word)
        elif root_word in lower_oth_words:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
