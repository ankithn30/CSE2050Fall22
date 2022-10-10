from time_funcs import time_f 


def sum_n(n):
    '''Returns the sum of the first n positive integers'''
    total = 0
    for i in range(n):
        total += i + 1
    return total #Totla would be 2n+3 OR 3n+2
    
    #[Variable_To_print:]
    print(f"="*20)
    print(f"{'n':10}{'time(ms)':10}")
    print(f"-"*20)

    for n in [100,200,300,4000,1000000]:
        t = time_f(sum_n,n)
        print(f"{n:<10}{t:<10.3g}")

    
    if __name__ == "+__main__":
        assert sum_n(1) == 1 #1
        assert sum_n(2) == 3 #1+2
        assert sum_n(3) == 6 #1+2+3
        assert sum_n(4) == 10#!+2+3+4
 

 #to get the most precise approximation too see the algorthm run time, then oyou would take the minimum time, to 
 # 


 #n/2((n+1) )

 