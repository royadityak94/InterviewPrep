//
// Created by adity on 3/3/2020.
//
#include "lowest_integer_array.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

std::vector<int> segregate(std::vector<int> arr, int n){
    int j = 0;
    for (int i=0; i<n;i++){
        if (arr[i] < 0){
            swap(&arr[i], &arr[j]);
            j += 1;
        }
    }
    return arr;
}

int return_smallest_integer_naive(std::vector<int> arr){
    int smallest_unseen = 1;
    sort(arr.begin(), arr.end());

    for (int i = 0; i<arr.size(); i++){
        if (arr[i] == smallest_unseen)
            smallest_unseen += 1;
        else if (arr[i] > smallest_unseen)
            return smallest_unseen;
    }
    return smallest_unseen;
}

int return_smallest_integer_hashmap(std::vector<int> arr){
    std::map<int, int> keys;
    int largest = 0;
    for (int i=0; i<arr.size(); ++i){
        if (arr[i] > 0){
            largest = std::max(largest, arr[i]);
            keys[arr[i]] = 1;
        }
    }
    for (int i=1; i<arr.size(); ++i)
        if (keys.find(i) == keys.end())
            return i;
    return largest + 1;
}

int return_smallest_integer_efficient(std::vector<int> arr){
    int n = arr.size();
    arr = segregate(arr, n);
    if (arr.back() <= 0)
        return 1;
    for (int i=0; i<n; ++i)
        if ((std::abs(arr[i] - 1) < n) && (arr[std::abs(arr[i]) - 1] > 0))
        arr[std::abs(arr[i]) - 1] = -arr[std::abs(arr[i]) - 1];

    for (int i=0; i<n; ++i){
        if (arr[i] > 0)
            return (i+1);
    }
    return (n+1);
}

int main1(){
    // Test Case - 1:
    std::vector<int> arr1 = {1, 3, 6, 4, 1, 2};
    std::vector<int> arr2 = {-1, -3};
    std::vector<int> arr3 = {1, 2, 3};

    if (return_smallest_integer_efficient(arr1) != return_smallest_integer_naive(arr1) &&
            return_smallest_integer_hashmap(arr1) != return_smallest_integer_naive(arr1))
        std::cout << "Test Case - 1 failed. " << std::endl;
    // Test Case - 2:

    else if (return_smallest_integer_efficient(arr2) != return_smallest_integer_naive(arr2) &&
        return_smallest_integer_hashmap(arr2) != return_smallest_integer_naive(arr2))
        std::cout << "Test Case - 2 failed. " << std::endl;
    // Test Case - 3:
    else if (return_smallest_integer_efficient(arr3) != return_smallest_integer_naive(arr3) &&
        return_smallest_integer_hashmap(arr3) != return_smallest_integer_naive(arr3)) {
        std::cout << "Test Case - 3 failed. " << std::endl;
        std::cout << return_smallest_integer_efficient(arr3) << " | " <<
          return_smallest_integer_naive(arr3) << " | " <<
          return_smallest_integer_hashmap(arr3) << " | " << std::endl;
    }
    else {
        std::cout << "All tests have passed!" << std::endl;
    }

}