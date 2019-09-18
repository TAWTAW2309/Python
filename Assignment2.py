list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def sum_element(list):
    high_element = 0

    for x in list:
        high_element = max(sum(x), high_element)
        return high_element

print(sum_element(list))

