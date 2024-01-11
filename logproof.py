#logarithmical proof that the result from
# x € (0,1)
# x*log2(x) + (1-x)*log2(1-x)
# will always be >= -1
from math import log2

def operation(x):
    y= ( (x * log2(x)) + ((1-x) * log2(1-x)) )
    return y
    
def func():
    b=[]
    b += [i/10 for i in range(1,10)]
    [print(i) for i in b]  #prints out 0.1,0.2 ... 0.9
    c=[]
    c += ["{:.2f}".format(operation(elem)) for elem in b]
    return c
    #c is
    #['-0.47', '-0.72', '-0.88', '-0.97', '-1.00', '-0.97', '-0.88', '-0.72', '-0.47']
