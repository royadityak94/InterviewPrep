//
// Created by adity on 3/3/2020.
//
#include "longest_subarray_with_k_characters.h"
#include <iostream>

int find_max_substring_k_distinct(std::string inp_str, int max_distinct) {
    int start = 0, longest = 0;
    std::string curr_window = "";
    for (int end = 0; end < inp_str.length(); ++end) {
        curr_window += inp_str[end];
        if (curr_window.length() > max_distinct) {
            longest = std::max(longest, int(curr_window.length()));
            curr_window = std::string(&inp_str[start], &inp_str[end]);
        }
    }
    return longest;
}


int main(){
    std::string str1 = "araaaaaaci";
    std::string str2 = "alllbpppaaja";
    int distinct1 = 3, distinct2 = 3;
    //Test Case-1
    std::cout << find_max_substring_k_distinct(str1, distinct1) << std::endl;
    std::cout << find_max_substring_k_distinct(str2, distinct2) << std::endl;

}