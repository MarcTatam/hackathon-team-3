##min max product
""" Hackathon - Level 1 """

def min_max_product(list):
    smallest = arr[0]
    biggest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
        elif item > biggest:
            biggest = item

    return biggest * smallest

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 200
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))
    
print(min_max_product([100,24,15,4,9,61]))
