"""
Student code for Word Wrangler game
"""
import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    nodup_list = []
    for dummy_element in list1:
        if dummy_element not in nodup_list:
            nodup_list.append(dummy_element)    
    return nodup_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersect_list = []
    for dummy_element in list1:
        if dummy_element in list2:
            intersect_list.append(dummy_element)
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    merge_list = []
    idx_i = 0
    idx_j = 0
    while idx_i < len(list1) and idx_j < len(list2):
        if list1[idx_i] <= list2[idx_j]:
            merge_list.append(list1[idx_i])
            idx_i += 1
        elif list1[idx_i] >list2[idx_j] :
            merge_list.append(list2[idx_j])
            idx_j += 1  
    if idx_i == len(list1):
        while idx_j < len(list2):
            merge_list.append(list2[idx_j])
            idx_j += 1 
    elif idx_j == len(list2):
        while idx_i < len(list1):
            merge_list.append(list1[idx_i])
            idx_i += 1
    return merge_list
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        listb4 = list1[:len(list1)/2]
        listaf= list1[len(list1)/2:]
        listb4 = merge_sort(listb4)
        listaf = merge_sort(listaf)
        return merge(listb4, listaf)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 1 or len(word) ==0:
        return [word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        new_string_list = []
        all_strings = []
        new_string_list.append(first)
        for each_string in rest_strings:
            for dummy_idx in range(len(each_string)+1):
                if dummy_idx == 0:
                    new_string = first + rest
                else:
                    new_string = rest[:dummy_idx] + first + rest[dummy_idx:]
                new_string_list.append(new_string)
        all_strings = rest_strings + new_string_list 
        return all_strings
            
  

    #Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
list1 = [3,6,8]
list2 = [1,6,9]
list3 = [3,6,8,1,6,2,9,11]
#print intersect(list1,list2)
#print merge(list1,list2)
#print merge_sort(list3)
print gen_all_strings("aab")


