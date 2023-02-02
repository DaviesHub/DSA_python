def binary_search(list, target):
    '''
    Returns the index position of the target if found on a sorted list, else it returns None.
    '''

    # Find middle of the list and compare to target position
    if len(list) % 2 == 0:
        i = (len(list)/2) + 1
    else:
        i = ((len(list)/2) + 1)/2