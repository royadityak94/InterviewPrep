'''Module to develop and implement a bloom filter implementation
'''
import mmh3
from bitarray import bitarray
import math

class BloomFilter: 
    def __init__(self, expected_elements=1e4, false_positive_rate=.1):
        # Initialize Bit array
        self.bitarray_size = self.get_size_of_bitarray(expected_elements, false_positive_rate)
        self.bitarray = bitarray(self.bitarray_size)
        self.bitarray.setall(0)

        # Get the count of hash functions 
        self.hash_count = self.get_count_of_hashes(expected_elements, false_positive_rate)

    @classmethod
    def get_count_of_hashes(self, expected_elements, false_positive_rate):
        '''
            Expected hash count (k) = (expected_elements/false_positive_rate) * log (2)
        '''
        expected_hash_functions = (expected_elements / false_positive_rate) * math.log(2)
        return int(expected_hash_functions)

    @classmethod
    def get_size_of_bitarray(self, expected_elements, false_positive_rate):
        '''
            Bitarray Size (m) = (- expected_elements * log(false_positive_rate)) / (log(2)^2)
        '''
        denominator = math.pow(math.log(2), 2)
        bitarray_size = (-expected_elements * math.log(false_positive_rate)) / denominator
        return int(bitarray_size)

    def add(self, element):
        for _seed in range(self.hash_count): 
            bit = mmh3.hash(element, _seed) % self.bitarray_size
            self.bitarray[bit] = 1
    
    def contains(self, element): 
        for _seed in range(self.hash_count): 
            bit = mmh3.hash(element, _seed) % self.bitarray_size
            if not self.bitarray[bit]: 
                return False 
        return True


def main(): 
    # Initialize a Bloom Filter
    bloom_filter = BloomFilter()

    # Elements to be added to Bloom Filter 
    add_following_elements = tuple(['New York', 'Houston', 'California', 'San Francisco', 'Denver', 'Atlanta'])

    # Add the elements to the bloom filter 
    for element in add_following_elements: 
        bloom_filter.add(element)

    # Elements not in Bloom Filter
    elements_never_added = tuple(['New Delhi', 'Dhaka', 'London', 'Beijing', 'Berlin'])

    # Create a combined tuple 
    combined_tuples = add_following_elements + elements_never_added 

    correct_assignment = false_positive_rate = false_negative_rate = 0

    for element in combined_tuples: 
        is_in_bloom = bloom_filter.contains(element)
        if is_in_bloom: 
            if element in add_following_elements:
                correct_assignment += 1
            else: 
                false_positive_rate += 1
        else: 
            if element in add_following_elements:
                false_negative += 1
            else: 
                correct_assignment += 1
            
        print (f'Element {element} is in bloom {is_in_bloom}')

    print ("Success Rate: %f" % (correct_assignment/len(combined_tuples)))
    print ("False Positive Rate: %f" % (false_positive_rate/len(combined_tuples)))
    print ("False Negative Rate: %f" % (false_negative_rate/len(combined_tuples)))


if __name__ == '__main__': 
    main()