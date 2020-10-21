##min max product

def min_max_product(arr):
    smallest = arr[0]
    biggest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
        elif item > biggest:
            biggest = item

    return biggest * smallest

print(min_max_product([100,24,15,4,9,61]))
