# A naive Bloom Filter implementation
import math
import unittest
import mmh3
import random
from bitarray import bitarray

class BloomFilter:
    def __init__(self, prob_fp, size):
        self.prob_fp = prob_fp
        self.size = self.get_size(self.prob_fp, size)
        self.hash_count = self.get_hash_count(self.size, size)
        self.bit_array = bitarray(self.size)

    def get_size(self, p, n):
        return int(-(n*math.log(p))/(math.log(2)**2))

    def get_hash_count(self, m, n):
        return int((m/n)*math.log(2))

    def add(self, item):
        digests = []
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
            self.bit_array[digest] = True

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p, n = .05, 20
        cls.bloomFilter = BloomFilter(p, n)

    def test_case1(self):
        self.assertEqual(self.bloomFilter.hash_count, 4)

    def test_case2(self):
        # words to be added
        word_present = ['abound','abounds','abundance','abundant','accessable',
'bloom','blossom','bolster','bonny','bonus','bonuses', 'coherent', 'cohesive', 'colorful', 'comely', 'comfort', 'gems', 'generosity', 'generous','generously','genial']

        # word not added
        word_absent = ['bluff','cheater','hate','war','humanity', 'racism','hurt','nuke','gloomy','facebook', 'geeksforgeeks','twitter']

        for word in word_present:
            self.bloomFilter.add(word)

        random.shuffle(word_present)
        random.shuffle(word_absent)
        testSet = word_present[:10] + word_absent[:10]

        for word in testSet:
            if self.bloomFilter.check(word):
                if word in word_absent:
                    print ("'{}' is false positive".format(word))
                else:
                    print ("'{}' is probably present".format(word))
            else:
                print("'{}' is definitely not present".format(word))


if __name__ == '__main__':
    unittest.main()
