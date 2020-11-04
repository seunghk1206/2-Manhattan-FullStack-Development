import time
start_time = time.time()
def Nnary_search(sequence, item, N):
    begin_index = 0
    end_index = len(sequence)-1
    while begin_index <= end_index:
        Npoint = begin_index + (end_index - begin_index) // N
        Npoint_value = sequence[Npoint]
        if Npoint_value == item:
            return Npoint
        elif item < Npoint_value:
            end_index = Npoint - 1
        elif item > Npoint_value:
            begin_index = Npoint + 1
    return None
sequence_a = [each for each in range(10000)]

item_a = 9000

print(Nnary_search(sequence_a, item_a, 9000))#N<length of sequence_a

print("--- %s seconds ---" % (time.time() - start_time))