def get_indices_of_item_weights(weights, length, limit):
    
    if length <= 1:
        return None
    
    # case in which weights has two numbers and they're the same
    if length == 2:
        if weights[0] == weights[1] and weights[0] + weights[1] == limit:
            return (1, 0)
    
    # convert weights to dict
    weights_dict = { n:ind for ind, n in enumerate(weights) }
    
    # loop thru weights
    for w in weights:
        # if the limit minus the current weight is in the dict,
        if (limit - w) in weights_dict:
            # get the index of the current weight,
            current_ind = weights_dict[w]
            # get the index of the limit minus 
            # the current weight,
            found_ind = weights_dict[limit-w]
            # figure out which one is the larger index,
            largest = current_ind if current_ind > found_ind else found_ind
            smallest = current_ind if current_ind < found_ind else found_ind
            return (largest, smallest)

    return None

if __name__ == "__main__":
    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2)
    
    weights_3 = [4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    print(answer_3)
    
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
    print(answer_4)