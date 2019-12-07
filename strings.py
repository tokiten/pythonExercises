print("#next we test the strings#")
message='"Hello Tokiten,Welcome to Python world!"'
print(message)
message="'Let's start our journey, god bless you.'"
print(message)
print("\n\n")


print("#next we test the functions :title,upper,lower#")
name=("tokiten chan")
print(name.title())
print(name.upper())
print(name.lower())
print("\n\n")

print('#next we test the "strings combination"#')
firstName='jacky'
lastName='chan'
fullName=firstName+' '+lastName
print(fullName.title())
print("\n\n")

print('#next we test the "addBlank" use "\t(tab)" and "\n(enter)"#')
print("languages I planned to learn:\n\tC\n\tPython\n\tC++\n\tC#\n\tJava")

print('#next we test "deleteBlank" via the functions: lstrip(), restrip(), strip()#')
a=" python "
print('next we print a\n')
print(a)
print('next we print the results of upper three funtions\n')
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print('next we print a again to check if it is " python "\n')
print(a)
print('next we really delete the needless "space"before and after "python"\n')
print('we check strip()')
a=" python "
print(a)
a=a.strip()
print(a)
print('we check lstrip()')
a=" python "
print(a)
a=a.lstrip()
print(a)
print('we check rstrip()')
a=" python "
print(a)
a=a.rstrip()
print(a)
