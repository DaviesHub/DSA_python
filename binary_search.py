def binary_search(list, target):
    '''
    Returns the index position of the target if found on a sorted list, else it returns None.
    '''

    first = 0
    last = len(list) - 1

    while first <= last:
        mid =  (first + last) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None


def verify_search(list, target):
    result = binary_search(list, target)
    if result is not None:
        return result
    else:
        return "Not Found"

nums = [2, 10, 44, 57, 62, 91, 103]

print(verify_search(nums, 91))