from itertools import count


def single_root_words (root_words, *other_words):
    same_words = []
    for i in range (len(other_words)) :
        if len (root_words) > len (other_words[i]):
            if root_words.lower().count(other_words[i].lower())!=0:
                same_words.append(other_words[i])
        elif len (root_words) < len (other_words[i]):
            if root_words.upper() in other_words[i].upper():
                same_words.append(other_words[i])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)