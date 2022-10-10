#Recursion, greedy algorthms, memoization



from lzma import FILTER_LZMA2


def a():
    return b
def b():
    return c
def c():
    return 1
a()


def sum_k(k): #O(n) #recurions can be done in one or two lines and interative takes 5-6
#Base case 
    if k == 1: return 1 

    return k + sum_k(k-1)

sum_k(5)

assert sum_k(1) == 1
assert sum_k(2) == 3
assert sum_k(3) == 6
assert sum_k(4) == 10
assert sum_k(5) == 15

#iternative verison


def sum_k_iter(k): #O(n) #this is quicker BUT take MORE memory, Iternative solutions are often better
    total =0
    for i in range(k):
        k+= (i+1)

    return total 

sum_k(5)



#lab and homework use recursion


#fib (km) 0,1,1,2,3,5,8,13,21
#miles             3,5,8,13
#golden ration,1mile to km, 1.618 

#fi(n)/fib(n-1) -> golden raito ~1.6
counter = 0
def fib(k):

    if solved is None:
        solved = set()
    global counter 
    counter +=1 
    #takes 15 calls to get fib(5)
    if k in [0,1]: return k
    if (k-1) in solved:
        f1 = solved[k-1]
    else:
        f1 = fib(k-1)

    if (k-2) in solved:
        f2 = solved[k-2] #doing this abvoids infinite loops and this memoization --> keep track of solved problems 
    else:
        f1 = fib(k-2)
    solved[k] = f1+f2
    return solved[k]
fib(40)
print(counter)
# assert fib(0) == 0
# assert fib(1) ==1 
# assert fib(2) ==1
# assert fib(5) ==5  


#with the recurive calls you get about 2^n 