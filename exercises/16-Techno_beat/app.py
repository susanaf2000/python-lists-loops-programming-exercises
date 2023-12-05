def lyrics_generator(lst):
    new_list = []
    count = 0

    for i in lst:
        if i == 0:
            new_list.append("Boom")
        elif i == 1:
            new_list.append("Drop the base")
            count +=1
            if count == 3:
                new_list.append("!!!Break the base!!!")
                count = 0
    return " ".join(new_list)

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))