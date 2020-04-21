from functools import reduce

temperatury = [10, 13, 14, 15, 10]

acc = 1
for x in temperatury:
    acc = acc * x
print(acc)

def multiply(elem1, elem2):
    return elem1 * elem2

acc2 = reduce(lambda  elem1, elem2: elem1*elem2, temperatury)
print (acc2)
# [10, 13, 14, 15, 10]
# [130, 14, 15, 10]
# [1820, 15, 10]
# [27 300‬,10]

def a (arg1, arg2):
    with open(arg1, 'w') as f:
        f.write(arg2)
    return (arg1, arg2)
a('plik.txt',"Nasz plik")
a('plik1.txt',"Nasz plik")

acc3 = (reduce(lambda elem1, elem2: elem1+elem2, temperatury))/len(temperatury)

print(acc3)

