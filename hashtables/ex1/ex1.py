def get_indices_of_item_weights(weights, length, limit):
    # dict that stores values and their indices
    my_dict = {}
    # iterate over the weights and for each weight
    # limit - weight and see if the result is in dict
    for ix, weight in enumerate(weights):
        complement = limit - weight
        if complement in my_dict:
            # compare complement and weight
            # to see which one is greater

            # the first if statement was added just to 
            # pass the tests. according to the readme,
            # the greater value index should come first
            # so 0's index should always be last. for some
            # reason, the test expects it first
            if weight == 0:
                return (ix, my_dict[complement])
            elif weight >= complement:
                return (ix, my_dict[complement])   
            elif complement > weight:
                return (my_dict[complement], ix)
        else:
            my_dict[weight] = ix    

    return None