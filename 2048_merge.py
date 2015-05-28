"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result_list = []
    nonzero_list = []
    #Start with a result list that contains the same number 
    #of 0's as the length of the line argument
    for i in range(len(line)):
        result_list.append(0)
    #Iterate over the line input looking for non-zero entries. 
    #For each non-zero entry, put the value into the next available 
    #entry of the result list (starting at position 0)
    for i in range(len(line)):
        if line[i] != 0:
            nonzero_list.append(line[i])
    for i in range(len(nonzero_list)):
        result_list[i] = nonzero_list[i]        
    return result_list
print merge([2,0,2,2])
