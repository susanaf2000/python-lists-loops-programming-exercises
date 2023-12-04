#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:

for i in range(15 - len(my_list)): #dentro de () temos a length desejada
    n = random.randint(1, 734)
    my_list.append(n)
print(my_list)