people = ['Ebuka', 'Israel', 'Emmanuel', 'Mark']

#Indexing of list
ebuka = people[0]
print(ebuka)

#Changeable
people[3] = 'John'
# people[4] = 'Angel' #list assignment index out of range

print(people)
string = 'Jet brain'
print(len(people))
print(string[-1])
print(people[-1])
print(people[1:3])
print(people[2:])
print(people[-4:])

#Adding to list item
people.append('Iris')
people.append('Ebuka')
print(people)

people.insert(1, 'Idris')
print(people)

#Removing item from list
people.remove('John')
print(people)

people.pop(-2)
print(people)
del people[0]
print(people)
#people.clear()
#print(people)

#Sorting list
people.sort()
print(people)
people.sort(reverse=True)
print(people)

#Copying of list
people2 = people.copy()
people3 = list(people)
people3 = people[:]
print(people2)
print(people3)
people.clear()
print(people2)

#Joining of List
print('Fruits'.center(40, '*'))

fruits1 = ['Banana', 'Grape']
fruits2 = ['Orange', 'Apple']

fruits = fruits1 + fruits2
print(fruits)