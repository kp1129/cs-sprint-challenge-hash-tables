def has_negatives(a):
    # dictionary to lookup values
    my_dict = {}
    # compile the dictionary:
    # iterate over the list of integers
    # if a number is negative, add it to dict

    for num in a:
        if num < 0 and num not in my_dict:
            my_dict[num] = 1

    # iterate over input and for each positive number
    # subtract it from 0 and check the dictionary
    
    result = []
    for num in a:
        if num > 0:
            complement = 0 - num
            if complement in my_dict:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
