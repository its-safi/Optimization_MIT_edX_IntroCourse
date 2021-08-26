
def solveit(test):

    i=0
    while True:
        if test(i)==True:
            return i
            break
        elif test(-i) ==True:
            return -i
        i=i+1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15

print(solveit(f))