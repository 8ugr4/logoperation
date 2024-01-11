#logarithmical proof that the result from
# x € (0,1)
# x*log2(x) + (1-x)*log2(1-x)
# will always be >= -1
from math import log2


# print (math.log(-14))
def operation(x):
    y= ( (x * log2(x)) + ((1-x) * log2(1-x)) )
    return y
def func():
    b=[]
    b += [i/10 for i in range(1,10)]
    [print(i) for i in b]
    c=[]
    c += ["{:.2f}".format(operation(elem)) for elem in b]
    return c
    #a = [ elem*0.1 for elem in range(10) ]
def logcheck(a):
    return log2(a)
