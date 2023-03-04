def merge_sort(items):
    """
        Sorts a list in ascending order
        Returns a new sorted list with
        
        Divide: Find the midpoint of a list and divide into sublists
        Conquer: Recursively sort the sublists created using previous step
        Combine: Merge the sorted sublists created in previous step
    """
    print("main func starts")
    if len(items) <= 1:
        print(len(items))
        return items
    
    left_half, right_half = split(items)

    print("lefthalf", left_half)
    print("righthalf", right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    print("left ", left)
    print("right ", right)
    print("main func ends")
    return merge(left, right)


def split(items):
    """
        Divide the unsorted list at midpoint into sublists
        Returns two sublists - left and right

        Takes O(logn) time
    """

    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]

    return left, right

def merge(left, right):
    """
        Merges two lists, sorting them in the process
        Retuns a new merged list
    """
    print("\nmerge starts")
    item_storage = []
    i = 0 # index of left list
    j = 0 # index of right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            item_storage.append(left[i])
            i += 1
        else:
            item_storage.append(right[j])
            j += 1

    while i < len(left):
        item_storage.append(left[i])
        i += 1

    while j < len(right):
        item_storage.append(right[j])
        j += 1
    print("\nmerge ends")
    return item_storage



test_list = [54, 19, 27, 33]
l = merge_sort(test_list)
print(l)

def verify_sorted(list):
    if len(list) == 0 or len(list) == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

        
print(verify_sorted(merge_sort(test_list)))
    
