my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

def calculate_average(lst):
    values = 0

    for x in lst:
        values += x
    avg = values / len(lst)
    return avg
print(calculate_average(my_list))
    