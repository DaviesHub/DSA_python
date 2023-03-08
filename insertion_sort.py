# INSERTION SORT ALGORITHM. RESEARCHED FROM KHAN ACADEMY
def insertion_sort(list):
    '''
        This function sorts a list in ascending order using insertion sort algorithm.
    '''

    if len(list) <= 1:
        return list
    i = 1

    for i in range(1, len(list)): # Starting from second element of list
        # Compare with values from start of list
        j = 0
        while j < i:
            if list[j] > list[i]:
                while i > j:
                    list[i-1], list[i] = list[i], list[i-1]
                    i -= 1
            else:
                j += 1

    return list

def verify_isort(list):
    '''
        This function verifies if the list is sorted using insertion sort algorithm. It returns true if the list
        is sorted and false otherwise.
    '''

    if len(list) <= 1:
        return True
    
    return list[0] < list[1] and verify_isort(list[1:])