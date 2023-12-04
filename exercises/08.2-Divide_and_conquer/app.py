list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:

def merge_two_list(numbers):
    odd_list = []
    even_list = []

    for numb in numbers:
        if numb % 2 == 0:
            even_list.append(numb)
        else:
            odd_list.append(numb)
    
    merged_list = [odd_list, even_list]
    return merged_list

print(merge_two_list(list_of_numbers))

