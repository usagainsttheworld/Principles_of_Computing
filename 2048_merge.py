"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    slide_list = []
    merged_list = []
    result_list =[]
    merge = False 
    
    #Iterate over the line input looking for non-zero entries. 
    #For each non-zero entry, put the value into the next available 
    #entry of the slide_list (starting at position 0), add 0 in the end to match the length of line
    for number in line:
        if number != 0:
            slide_list.append(number)
    while len(slide_list) != len(line):
        slide_list.append(0)
    print 'non-zero slide to left', slide_list
    
    #Iterate over the slide_list and create merged_list 
    #in which pairs of tiles in the slide_list are replaced with 
    #a tile of twice the value and a zero tile.
    for i in range(len(slide_list)-1):
        if slide_list[i] == slide_list[i+1] and merge == False:
            merged_list.append(slide_list[i]*2)
            merged_list.append(0)
            print 'just add pair', merged_list
            merge = True          
        elif slide_list[i] != slide_list[i+1] and merge == False:
            merged_list.append(slide_list[i])
            print 'add non match', merged_list
        else:
            merge = False
    #deal with last element in the list
    if slide_list[-1] != 0 and merge == False:
        merged_list.append(slide_list[-1])
        print 'just add last element', merged_list
    
    #slide the non-zero to the left
    for number in merged_list:
        if number != 0:
            result_list.append(number)
    while len(result_list) != len(line):
        result_list.append(0)
        print 'merged non-zero slide to left', result_list
    return result_list

print merge([0,2])
