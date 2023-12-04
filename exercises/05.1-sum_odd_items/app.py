arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

def sum_odds(items):
    total_odd_numbers = 0
    for i in arr:
        if (i % 2) != 0:
            total_odd_numbers += i
    return total_odd_numbers
print(sum_odds(arr))
            
            

#Your code go here:
