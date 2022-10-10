def is_sorted(L):

    """ Reutrn a boolean donting whether L is sorted"""
    n = len(L)
    return not any(L[i] <= L[i+1] for i in range(n-1))
    """
    for i in range(n-1):
        if L[i] < L[i+1]:
            print(f"i={i}\tL[i]=[l{i}]")
    """
    return all(L[i] <= L[i+1] for i in range(n-1))


def bubble_sort(L):
    """Uses bubble sort to (inefficently) sort L"""
    n = len(L)                              #?
    for i in range(n):                      #?
        for j in range(n-1):                
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

if __name__ == '__main__':
    n= 500
    L = [i for i in range(n)]
    assert is_sorted(L)
    L[-1] = -1
    assert not is_sorted(L)

    bubble_sort(L)


    #More arithmic, then it would take logn times to be able to sort 
    #as you increase the number of trials, the time keeps on going down, and the fit of the line of the curve of being able to measure a sorting alogorthm gets closer to the line of best fit
    #it gets a better average 



#N^2 100 items --> 100,000 times longer 
#big-O get rid of unimportant terms and to focus on the most important 
#function f(n) is O(n) for sufficantyl large n, 
#cg(n) >= f(n), n>n(subsript0
# 
#ranking big O
#picture on phone

#log2(8) =3 , can also express as a different base for example,4, then you can do log4(8)/log4(2) (3/2)/(1/2) 3 


