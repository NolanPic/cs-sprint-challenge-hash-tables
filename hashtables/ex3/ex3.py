# Breakdown:
# 1. Sort the array of arrays from shortest to longest
# 2. Loop thru the arrays and create a list of
# dictionaries from them
# 3. Loop thru all the values in the SHORTEST array
# 4. While looping, check each dictionary to see if it
# contains the value.
# 5. If each dictionary contains the value, add it to
# the result set

# O(n^2) I believe
def intersection(arrays):
    result = []
    
    # sort the arrays by shortest to longest
    arrays = sorted(arrays, key=len)
    # each array will become a dictionary in
    # vvv this vvv list
    dictionaries = []
    # loop thru the array of arrays
    for arr in arrays:
        # ...and convert each one to a dict,
        arr_dict = {i:True for i in arr}
        
        # ... and add that dict to a list of dictionaries
        dictionaries.append(arr_dict)
        
    # now, loop thru the values of the first (SHORTEST) array,
    for i in arrays[0]:
        value_exists_in_all = True # start as true
        # ... and then loop thru the dictionaries,
        for d in dictionaries:
            if i not in d: # <- remember, d is a dictionary repretsenting one of the lists!
                value_exists_in_all = False
        if value_exists_in_all:
            result.append(i)
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
    
