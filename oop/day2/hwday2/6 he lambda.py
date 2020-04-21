#6. Write a Python program to square and cube
# every number in a given list
# of integers using Lambda. Go to the editor
#Click me to see the sample solution


items = [1, 2, 3, 4, 5]

squared = list (map(lambda x: x**2, items))

print(squared)


#13 Write a Python program to count the even, odd numbers in
#a given array of integers using Lambda. Go to the editor
#Click me to see the sample solution


items = [3,3,3,3,8,8,8,9,13,26,19,38]


even= list(filter(lambda x: x%2==0,  items))
odd= list(filter(lambda x: x%2!=0,  items))

print(f"number of even numbers is: {len(even)} and odd numbers is: {len(odd)}")


#17. Write a Python program to find numbers divisible by
#nineteen or thirteen from a list of numbers using Lambda. Go to the editor
#Click me to see the sample solution




number_19 = list(filter(lambda x: x%19==0 or x%13==0, items))

print(number_19)

#18. Write a Python program to find palindromes in a given list of strings using Lambda

items= ["assa","kaja","kajak","lool"]

palindr=list(filter(lambda word: word==word[::-1], items))

print(palindr)




