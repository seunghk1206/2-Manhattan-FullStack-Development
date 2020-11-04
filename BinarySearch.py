import time
start_time = time.time()
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        elif item > midpoint_value:
            begin_index = midpoint + 1
    return None
sequence_a = [each for each in range(10000)]

item_a = 9000

print(binary_search(sequence_a, item_a))

print("--- %s seconds ---" % (time.time() - start_time))