''' Hashset implementation in Python
'''
import math
import mmh3

class HashSet: 
    def __init__(self, element_counts=1e4): 
        self.brackets = int(math.sqrt(element_counts))
        self.hashset = [[] for _ in range(self.brackets)]
    
    def add(self, element): 
        current_bracket = mmh3.hash(element) % self.brackets
        if element not in self.hashset[current_bracket]: 
            self.hashset[current_bracket].append(element)
    
    def remove(self, element):
        current_bracket = mmh3.hash(element) % self.brackets
        if element in self.hashset[current_bracket]: 
            self.hashset[current_bracket].remove(element)
        print (f'Element {element} not in the set!')
    
    def contains(self, element):
        current_bracket = mmh3.hash(element) % self.brackets 
        if element in self.hashset[current_bracket]:
            return True
        return False

def main(): 
    # Initialize a Bloom Filter
    hashset = HashSet()

    # Elements to be added to Bloom Filter 
    add_following_elements = tuple(['New York', 'Houston', 'California', 'San Francisco', 'Denver', 'Atlanta'])

    # Elements in delete list
    delete_elements = tuple(['Houston', 'California', 'Denver'])

    # Add the elements to the bloom filter 
    for element in add_following_elements: 
        hashset.add(element)

    # # Delete the element 
    # for element in delete_elements: 
    #     hashset.remove(element)

    # Elements not in Bloom Filter
    elements_never_added = tuple(['New Delhi', 'Dhaka', 'London', 'Beijing', 'Berlin'])

    # Create a combined tuple 
    combined_tuples = add_following_elements + elements_never_added 

    correct_assignment = false_positive_rate = false_negative_rate = 0

    for element in combined_tuples: 
        is_in_bloom = hashset.contains(element)
        if is_in_bloom: 
            if element in add_following_elements:
                correct_assignment += 1
            else: 
                false_positive_rate += 1
        else: 
            if element in elements_never_added:
                correct_assignment += 1
            else: 
                false_positive_rate += 1
            
        print (f'Element {element} is in hashset {is_in_bloom}')

    print ("Success Rate: %f" % (correct_assignment/len(combined_tuples)))
    print ("False Positive Rate: %f" % (false_positive_rate/len(combined_tuples)))
    print ("False Negative Rate: %f" % (false_negative_rate/len(combined_tuples)))


if __name__ == '__main__': 
    main()