mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
def print_types(mix):
    for i in range(len(mix)):
        print(type(mix[i]))
print_types(mix)