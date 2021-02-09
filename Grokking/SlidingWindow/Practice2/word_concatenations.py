# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.


def find_word_concatenation(string, substrings):
    counter = {}
    for substring in substrings:
        if substring not in counter:
            counter[substring] = 0
        counter[substring] += 1


    matched_idxes = []
    words = len(substrings)
    word_length = len(substrings[0])

    for i in range(len(string) - (words * word_length) + 1):
        words_seen = {}
        for j in range(words):
            next_word_idx = i + (j * word_length)
            next_word = string[next_word_idx:next_word_idx + word_length]
            if next_word not in counter:
                break
            if next_word not in words_seen:
                words_seen[next_word] = 0
            words_seen[next_word] += 1

            if words_seen[next_word] > counter.get(next_word, 0):
                break

            if j + 1 == words:
                matched_idxes += i,

    return matched_idxes





if __name__ == '__main__':
    print (find_word_concatenation('catfoxcat', ["cat", "fox"])) #[0, 3]
    print (find_word_concatenation('catcatfoxfox', ["cat", "fox"])) #[3]
