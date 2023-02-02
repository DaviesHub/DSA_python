def linear_search(list, target):
    '''
    Returns the index position of the target if found on the list, else it returns None
    '''

    for i in range(len(list)):
        if list[i] == target:
            return list.index(target)

    return None

def verify(index):
    '''
    Returns the result of the linear search function
    '''
    if index == None:
        print("Target not found in list")
    else:
        print(f"Target found at index {index}")

nums = [2, 44, 6, 5, 1, 10]
result = linear_search(nums, 5)
verify(result)