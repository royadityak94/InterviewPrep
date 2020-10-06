# Implemented algorithm: Fisher-Yates Shuffle (or, Knuth Shuffle)
import random

def get_randomized_shuffle(arr, seed=42):
    random.seed(seed)

    for idx in range(len(arr)):
        random_idx = random.randint(idx, len(arr)-1)
        if random_idx != idx:
            arr[idx], arr[random_idx] = arr[random_idx], arr[idx]
    return arr


def main():
    print (list(range(4, 23)))
    print ("Random Shuffle: ", get_randomized_shuffle(list(range(4, 23))))

main()
