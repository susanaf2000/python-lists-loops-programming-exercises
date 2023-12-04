my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(lst):
    max_value = 0

    for x in lst:
        if max_value < x:
            max_value = x #we update max_value to the current value
        else:
            continue

    return max_value

print(maxInteger(my_list))

