#chapter 3 lists


#BICYCLE.PY
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#visit the elements of the list
print(bicycles[0].title())
print(bicycles[1].upper())
#use i(i<0) as the index to visit the last element of the list when you don't know the length of the list
print(bicycles[-1].title())
print(bicycles[3].upper())
print(bicycles[-2].title())
print(bicycles[2].upper())
#exercise 3-1,3-2,3-3
members=['tokiten','xu zhong','yunpeng wu','yijie zhu']
message='the members of my dormitory 7B226 are: '+members[0]+','+members[1]+','+members[2]+','+members[3]+','
print(message)

print('\tgood afternoon'+members[0]+'\n','\tgood afternoon'+members[1]+'\n','\tgood afternoon'+members[2]+'\n','\tgood afternoon'+members[3]+'\n')


#MOTORCYCLE.PY
#change the element of the list
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
#add the element of the list
motorcycles.append('ducati')
print(motorcycles)
#add elements to a blank list
courses=[]
courses.append('Advanced Mathematics')
courses.append('Linear Algebra')
courses.append('Advanced Algebra')
courses.append('Discrete Mathematics')
print(courses)
#insert element to the blank
courses.insert(2,'Computer Sciencs')
print(courses)
#use del to delete an element from the list
del courses[2]
print(courses)
print('################')
#use pop
print(courses)
poppedCourse=courses.pop(1)
print(courses)
print('The first course I have had in Soochow University is '+poppedCourse)
#use remove
print('########################')
courses=[]
courses.append('Advanced Mathematics')
courses.append('Linear Algebra')
courses.append('Advanced Algebra')
courses.append('Discrete Mathematics')
print(courses)
courses.insert(2,'Computer Science')
CScourse=courses[2]
courses.remove('Computer Science')
print(CScourse+' is not belong to Mathematics')
#CARS.PY
print('####################################')
cars=['bmw','audi','toyota','subaru']
print(cars)
#a-z
cars.sort()
print(cars)
#z-a
cars.sort(reverse=True)
print(cars)
#use sorted
print('######################')
cars=['bmw','audi','toyota','subaru']
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list:')
print(cars)
print('\nHere is the reverse-sorted list:')
print(sorted(cars,reverse=True))
print('\nHere is the original list:')
print(cars)
#reverse
print('#')
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
#len
carsLength=len(cars)
print(carsLength)
#exercise 3-8,3-9,3-10
print('#')
destination=[]
destination.append('Cheng Du')
destination.append('Nepal')
destination.append('Niagara Falls')
destination.append('toronto')
destination.append('kyoto')
destination.append('harbin')
print(destination)
print(sorted(destination))
print(destination)
print(sorted(destination,reverse=True))
print(destination)
destination.reverse()
print(destination)
destination.reverse()
print(destination)
destination.sort()
print(destination)
destination.sort(reverse=True)
print(destination)
length=len(destination)
print(length)
print('#')
