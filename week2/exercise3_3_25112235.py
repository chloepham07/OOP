#Exercise 3.3
#1. Write a function that draws a grid like the following:
# + - - - - + - - - - + 
# |         |         |
# |         |         | 
# |         |         |
# |         |         |
# + - - - - + - - - - + 
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - + 
#2. Write a function that draws a similar grid with four rows and four columns.

for i in range (2):
    print (('+ '+'- '*4)*2+'+ ')
    for i in range(4):
        print (('| '+' '*8)*2+'| ')
print (('+ '+'- '*4)*2+'+ ')

def grid(a):
    for i in range (a):
        print (('+ '+'- '*4)*a+'+ ')
        for i in range(4):
            print (('| '+' '*8)*a+'| ')
    print (('+ '+'- '*4)*a+'+ ')
a=int(input('2.Enter a:'))
grid(a)
