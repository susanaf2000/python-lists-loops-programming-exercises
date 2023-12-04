theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def wiki_woko(x):
return "wiki" if x == 1 else "woko"

new_list = list(map(lambda x: wiki_woko(x), theBools))
print(new_list)
    


