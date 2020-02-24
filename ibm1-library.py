pairs = [
    (["das", "Haus"], ["the", "house"]),
    (["das", "Buch"], ["the", "book"]),
    (["ein", "Buch"], ["a", "book"]),
]

t = {}

# -- Initialize t(e|f)
for pair in pairs:
    sentence_f = pair[0]
    sentence_e = pair[1]
    for word_f in sentence_f:
        for word_e in sentence_e:
            t[word_f + "|" + word_e] = 0.25

# -- Converge for i iterations
for i in range(10):
    total_f = {}
    count_ef = {}

    # -- Initialize t
    for pair in pairs:
        sentence_f = pair[0]
        sentence_e = pair[1]
        for word_e in sentence_f:
            total_f[word_e] = 0
            for word_f in sentence_e:
                count_ef[word_e + "|" + word_f] = 0

    for pair in pairs:
        sentence_f = pair[0]
        sentence_e = pair[1]
        s_totals = {}
        i = 0

        # -- Normalize
        for word_f in sentence_f:
            i += 1
            for word_e in sentence_e:
                if word_e not in s_totals.keys():
                    s_totals[word_e] = 0
                s_totals[word_e] += t[word_f + "|" + word_e]

        # -- Collect counts
        for word_f in sentence_f:
            for word_e in sentence_e:
                id = word_f + "|" + word_e
                if id not in count_ef.keys():
                    count_ef[id] = 0
                count_ef[id] += t[id] / s_totals[word_e]
                if word_f not in total_f.keys():
                    total_f[id] = 0
                total_f[word_f] += t[id] / s_totals[word_e]

    # -- Estimate probabilities
    foreign_words = []
    english_words = []
    for pair in pairs:
        foreign_words += pair[0]
        english_words += pair[1]
    list(set(t))

    foreign_words = list(set(foreign_words))
    english_words = list(set(english_words))

    for foreign_word in foreign_words:
        for english_word in english_words:
            id = foreign_word + "|" + english_word
            if id in t.keys() and total_f[foreign_word] != 0:
                t[id] = count_ef[id] / total_f[foreign_word]

print("T: " + str(t))
