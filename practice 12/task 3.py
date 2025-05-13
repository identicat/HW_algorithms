ru_en_dict = {}


with open('en-ru.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(' - ')
        en_word = parts[0].strip()
        ru_words = [word.strip() for word in parts[1].split(',')]

        for ru_word in ru_words:
            if ru_word in ru_en_dict:
                if en_word not in ru_en_dict[ru_word]:
                    ru_en_dict[ru_word].append(en_word)
            else:
                ru_en_dict[ru_word] = [en_word]


ru_words_sorted = sorted(ru_en_dict.keys())


with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for ru_word in ru_words_sorted:
        en_list = sorted(ru_en_dict[ru_word])
        f.write(f"{ru_word} – {', '.join(en_list)}\n")