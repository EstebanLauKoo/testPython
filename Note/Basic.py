'''
    this is just a note
'''
import math
import re


''' Setting a variable '''
job = 'hello'
''' Printing Hello World'''
print('hello world')
''' Printing variable 'job' '''
print(job)
''' Printing a concatenation of Hello Nick'''
print("Hello, " + "Nick")
''' Splitting a string according to :'''
print("Hello:Nick".split(":"))
''' concatenating a string plus splitting a string according to ':' and calling the index 1 in the array'''
print("My Name is " + "Bob:Ethan:Travis".split(":")[1])


''' Boolean Operators '''
''' Boolean must be capitalized and not in string quotations'''
print(True)
''' comparison must be == '''
''' = just sets a value'''
print(5 == 5)
''' test for truth according to system'''
print(5 == 4)
''' == can be called as 'is' '''
print(5 is 5)
''' test for false'''
print(5 is 4)
''' test if what you says is true (in this case its not)'''
print(5 is not 5)
''' can also test for type and strings'''
print("this" is "this")
''' what about one quotation vs double'''
print("this" is 'this')

''' Lists (arrays) '''
''' define arrays by []'''
namesArray = ["Hello my name is ", "Bob", "Tristan", "Ian"]
''' set a variable as two strings'''
nameValue = namesArray[0] + namesArray[1]
print(nameValue)
''' Wanted to test for what king of type the variable is'''
print(type(nameValue))

''' Dictionaries '''
''' Create Dictionaries {}'''
''' We don't wrap code blocks in {}'''
''' Think of this like an object'''
''' You can also set integers and booleans it doesnt have to be just str'''
nickPerson = {"name": "Nick", "age": 32, "hobby": "code", "dead": False}
''' to call just put var["attributeName"]'''
print(nickPerson["age"])
print(type(nickPerson["age"]))
print(nickPerson["dead"])

''' Variables'''
''' Variables in python can be very dynamic'''
''' Python is not a type language'''
Esteban = {"name": "Esteban", "age": 25, "hobby": "code", "dead": True}
print("hello my name is " + Esteban["name"])

''' Built-in functions'''
''' Traditional call on command'''
''' converts this to string'''
print(str(34))
''' converts string to int'''
print(float("5.6"))
''' len calculates digits, letters, or # of items '''
print(len(nickPerson))
numberArray = [32, 42, 235, 23, 29, 26, 35, 98]
''' sorted will shift the array around '''
print(sorted(numberArray))
''' sorting letters will prioritize capitalized letters then lowercase prioritizes numbers as string'''
letterArray= ["B", "T", "N", "a", "d", "b", "t", "Z", "2"]
print(sorted(letterArray))

''' user-defined functions '''
''' pep guidelines (python guidelines)'''
''' skip 2 lines at the top of the page for imports and notes'''
''' CamelCase is used for class names'''
''' functions are inclined to be done in snakecase (my_function)'''
''' pass parameters by ()'''


def reiterate(data):
    print(data)


''' to call a function type the name and the parameters'''
reiterate(Esteban)

''' arguments'''
''' to make things dynamic use arguments'''


def is_he_dead(person):
    if person["dead"] is True:
        print("RIP")
    else:
        print("well im still alive, why?")


is_he_dead(Esteban)

my_name_is="my name is"
and_im="and I'm"
''' Default Arguments'''


def print_something(name, age):
    print(my_name_is, name, and_im, age)


''' by putting , instead of + we can skip issues with int vs string'''
print_something("Esteban", 25)

''' giving default values'''


def print_something_2(name="Someone", age="Unknown"):
    print(my_name_is, name, and_im, age)


print_something_2()

''' Key word arguments'''
''' None is considered boolean (null)'''


def print_something_3(name="Someone", age="Unknown"):
    print(my_name_is, name, and_im, age)


''' 
by specifying keyword arguments it helps you place things in different orders
and also helping you categorize values
'''
print_something_2(age=30, name="Bryan")

'''
    Infinite arguments
'''


''' * tells you that its going to be array'''
peopleList = ["Erin", "Bob", "Steve", "Phung", "Bryan"]


''' For an array with data don't put the asterisk, for an object with multiple information*'''


def print_people(people):
    for person in people:
        print("this person", person)


print_people(peopleList)


''' More dynamic programming'''


def do_math(num1, num2):
    return num1 + num2


math1 = do_math(4, 6)
math2 = do_math(12,36)

print(math1 + math2)


''' if, else, else if conditionals'''
''' remember Boolean can be expressed as 'is' '''

Person2 = {"name": "Esteban", "age": 25, "hobby": "code", "dead": "Maybe"}


if Person2["dead"] is True:
    print("he is dead")
elif Person2["dead"] is False:
    print("He is alive")
else:
    print("I don't know what you want from me")

''' Set up a jumbled array, sorted it, then printed it sorted'''

numberArray2 = [32, 4, 5, 645, 345, 23453, 34535, 534405, 32, 5, 9, 17]
orgArray2 = sorted(numberArray2)

for number in orgArray2:
    print(number)

''' ran a run loop with an counter'''

run = True
current = 1

while run:
    if current == 100:
        run = False

    else:
        print(current)
        current += 1

''' took the int pi converted to string, looped through it to have it print the digit and its placement 
had it break if it reached a number 7
- Couldn't figure out how to make it run with a run sequence and a for loop
- Made it work with break and continue 
'''
numberPi = str(math.pi)
print(numberPi)

digitPlacement = 1

for number in numberPi:
    if number == "7":
        print("Stopped")
        break
    elif number == ".":
        print("this is just a decimal")
        continue
    else:
        if number == "3" and digitPlacement == 1:
            print(str(number) + " in the 1's")
        else:
            print(str(number) + " in the " + str(digitPlacement) + "th place")
            digitPlacement += 1

''' importing libraries into a script (modules)'''
''' importing re (regex) '''

stringRegex = "'I AM NOT YELLING', she said. Though we knew it to not be true"
stringRegex2 = "'I AM NOT YELLING', she said. Though we knew it to not be true 2345-343234 12324"
print(stringRegex)

''' We are calling the module regex and using the sub class function'''
''' Telling it to remove all capitalized letters'''
''' learn regex it's definitely useful'''
new = re.sub('[A-Z]', '', stringRegex)
new1 = re.sub('[.,\'A-Z+" "]', '', stringRegex)
new2 = re.sub('[^0-9]', '', stringRegex2)
print(new)
print(new1)
print(new2)









