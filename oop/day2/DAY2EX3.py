# Write a Python program to sort a list of tuples using Lambda.

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=(lambda x: x[1]))
print (a)
# print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

# x_squared = list(map (lambda elem: elem ** 2, x))


# Write a Python program to square and cube every number in a given list of integers using Lambda.


num_lis=[1,2,3,4,5,6]




x_2= list(map (lambda m: m ** 2, num_lis))
print(x_2)

lam_1=lambda n: n**2

x_3=[lam_1 for var in num_lis]
print(x_3)   #zapytac sie




students= {"Asia Jasia":[1,5,3,6], "Grażyna Janusz":[4,3,6,2], "Janusz Kowal":[3,6,5,2]}

x_2= list(map (lambda m: m ** 2, num_lis))
print(x_2)



x = {max(v): v for (k,v) in students }

grade = {name: grade.sort() for (name, grade) in students.items()}

grade1=list(map(lambda items: (items[0], items[1].sort(), students.items()))

print(grade)
print(grade1)



