def intersection(arrays):
    # a dictionary of element frequencies
    my_dict = {}
    # iterate over the array of arrays
    # for each array, add each of its elements
    # to the dictionary
    for arr in arrays:
        for each in arr:
            if each in my_dict:
                my_dict[each] += 1
            else:
                my_dict[each] = 1    
    # at the end, check to see which numbers
    # in the dictionary have the frequency that
    # equals the length of the outer array
    all_sorted = sorted(my_dict.items(), key=lambda pair: pair[1], reverse=True)
    results = []
    # while loop setup
    # length of outer array to make sure we don't go over the index
    length = len(arrays)
    # length of all_sorted to make sure we don't go over the index
    sorted_length = len(all_sorted)
    # flag to exit the loop when it starts iterating over pairs
    # that occur at frequencies we don't care about
    keep_going = True
    ix = 0
    while ix < length and ix < sorted_length and keep_going:
        if all_sorted[ix][1] == length:
            results.append(all_sorted[ix][0])
            ix += 1
        else:
            keep_going = False    
    
    return results



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
