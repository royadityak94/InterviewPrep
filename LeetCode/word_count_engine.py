'''Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.
Order: sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence.
Punctuations: The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

input:  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
output: [["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"]]
'''
import re
from collections import OrderedDict

# O(n + m) time | O(m) space, n: word count, m: total keys
def word_count_engine(document):
    mapper = OrderedDict()
    maxFrequency = float('-inf')
    for word in document.split():
        word_lower = re.sub(r'[^\w\s]', '', word.lower())
        mapper[word_lower] = 1 + mapper.get(word_lower, 0)
        maxFrequency = max(maxFrequency, mapper[word_lower])

    # in O(nlogn + n) time | O(n) space - just, sample!!
    # frequencies = []
    # for key, value in sorted(mapper.items(), key=lambda item: item[1], reverse=True):
    #     frequencies += [key, str(value)],
    # Place words (as list) based on index (= frequencies)
    counterList = [None] * (maxFrequency+1)

    for word in mapper.keys():
        _count = mapper[word]
        currentList = counterList[_count]
        if currentList is None:
            currentList = []
        currentList += word,
        counterList[_count] = currentList

    frequencies = []
    # Iterate backways, and add the frequencies to the final list (except those that are None)
    for idx in range(len(counterList))[::-1]:
        present_list = counterList[idx]
        if present_list is None:
            continue
        for item in present_list:
            frequencies += [item, str(idx)],
    return frequencies

if __name__ == '__main__':
    document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    expected_op = [["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"]]
    assert word_count_engine(document) == expected_op
