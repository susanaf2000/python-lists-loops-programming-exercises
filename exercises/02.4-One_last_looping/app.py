names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

names[1] = 'Steven'
names[10] = 'Pepe'
names[0] = names[2] + names[4]

for i in range(len(names) -1, -1, -1): # if we use "for i in names" it will not give the loop that we want
    print(names[i])