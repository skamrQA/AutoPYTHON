import math
def squar(a): 
    sq = a * a
    if sq % a > 0:
        decimal = math.ceil(a)
        print(decimal)
    else:
        print(sq)
squar(5.5)