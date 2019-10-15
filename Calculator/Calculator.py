'''
imports regex so that we can make sure eval function doesn't destroy us
'''
import re

print("Our Calculator")

''' sets the initial value to 0 and the run to true '''
initial = 0
run = True

''' performMath function is built'''
def performMath():
    ''' makes ure that the run and previous variables are accesible in the scope '''
    global run, initial
    counter = 0
    ''' first condition involves the initial moment of run'''
    if counter == 0:
        equation = input("Enter Equation: ")
        counter = 1
    else:
        equation = input(str(initial))

    if equation == 'quit':
        counter = 0
        run = False
        print("Goodbye")
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if initial == 0:
            initial = eval(equation)

        else:
            initial = eval(str(initial) + equation)
            counter = 1
            print(counter)


while run:
    performMath()