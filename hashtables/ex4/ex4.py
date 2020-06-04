def has_negatives(a):
    # store the numbers that have negatives
    result = []
    # turn the list into a dictionary
    # for fast lookup
    num_dict = {num:True for num in a}
    # loop thru input a,
    for num in a:
        # if the number is not negative,
        # and the inverse of that number exists
        # in the dict,
        if num > 0 and (num*-1) in num_dict:
            # add the num to the results
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
