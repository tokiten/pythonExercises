#chapter4#
#exercise 4-1
animal=['lion','crocodile','dragon']
for amazingAnimal in animal:
    print('\tA '+amazingAnimal+' would surely make you amazed')
print('All of these animals are amazing')
#use range
for value1 in range(1,11):
    print('\t#'+str(value1)+'#')
print('All of value1 have been printed\n')
for value2 in range(2,10):
    print(value2)
print('All of value2 have been printed')
numbers=list(range(1,11,2))
volume=[]
for number in numbers:
    number=number**3
    volume.append(number)
print(numbers)
print(volume)
#use min,max,sum
print('#')
print(volume)
disposeResults=[]
disposeResults.append(min(volume))
disposeResults.append(max(volume))
disposeResults.append(sum(volume))
print(disposeResults)

squares=[value**2 for value in range(1,11)]
print(squares)
trial=[value**(1/2) for value in volume]
print(trial)

#exercise 4-3
twentyNums=[]
for number in range(1,21):
    print(number)
print('#')

#exercise 4-4,4-5
nums4=[]
for number4 in range(1,1000001):
    nums4.append(number4)
print(min(nums4),max(nums4))
print(sum(nums4))
print('#')

#exercise 4-6
nums5=[]
for number5 in range(1,21,2):
    nums5.append(number5)
print(nums5)

#exercise 4-7
nums6=[]
for number6 in range(3,31,3):
    nums6.append(number6)
print(nums6)

#exercise 4-8
nums7=[]
for number7 in range(1,11):
    number7=number7**3
    nums7.append(number7)
print(nums7)

#exercise 4-9
nums8=[number8**3 for number8 in range(1,11)]
print(nums8)

print(nums8[2:7])
print(nums8[-8:-3])
print(nums8[:-3])
print(nums8[6:])
print(nums8[-3:])
print(nums8[:6])
for number8 in nums8[:5]:
    print(number8)

#exercise 4-12
myFavouriteCartoons=['weathering with me','darling in the franxx','sword art online']
friendFavouriteCartoons=myFavouriteCartoons[:]
friendFavouriteCartoons.append('fate grander order')
myFavouriteCartoons.append('fate/zero')
print("#\n")
for myCartoons in myFavouriteCartoons:
    print("\tmy favourite cartoons are: "+myCartoons.title())
print('\n')
for friendCartoons in friendFavouriteCartoons:
    print("\tmy firend's favourite cartoons are: "+friendCartoons.title())
print('\n')
print('#')

#tuple
menu=('noodles','cake','dumpling','moon cake','rice')
print(menu)
for food in menu:
    print(food.title())
menu=('null')
print(menu)