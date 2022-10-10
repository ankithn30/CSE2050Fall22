#create functions with the running times, O(n), O(n), O(n^2)
import time 
from functions import car, calculate,tester, built_in
def time_f(func,*arg,n_trials=20):
    '''Tests what you give it in values, with the paramaters'''
    best = float('inf')
    #start time
    start = time.time()
    #checking trials
    for n in range(n_trials):
        func(*arg)
    #end time
    end = time.time()
    if (end - start) < best:
        best = (end - start)
    return best

#test cases for each of the built in functions, 
L = [i for i in range(10000)]
S = {i for i in range(10000)}
#number part for the tuple
T = {i for i in range(10000)}
#letter part for the tuple
U = {'a','b','c','d','e'}
#final created tuple variable, which will be used
P = (T,U)
Str = "ajkdkifhns"

#the test cases for the built in-s
l1 = time_f(built_in,L,-5000)
s1 = time_f(built_in,S,1000005)
#Tuple
t1 = time_f(built_in,P,(150000,'z'))
z1 = time_f(built_in,Str,'zhjkjfjfjbfjksdflj')

#shows the timings from the creatred threee functions which virtualize O(n),O(n^2),O(1)
print("=" * 50)
print(f"{'n':8}{'t_const (ms)':16}{'t_lin (ms)':15}{'t_quad (ms)':32}")
print("=" * 50)
for n in [2, 4, 6, 8, 10,12,14,16,18,20]:
    print(f"{n:<4}\t{1000*time_f(calculate, 5, n_trials=n):<10.3g}\t{1000*time_f(tester, [1,2,3,4], n_trials=n):<10.3g}\t{1000*time_f(car, ['Honda', 'Lamborghini', 'Ford', 'Mercedes'], [2018, 2019, 2020, 2021], n_trials=n):<10.3g}\t")
print("-" * 50)


#table for to find a value with pythons built-ins
print("=" * 75)
print(f"{'Contains (times in ms)':>40}")
print("=" * 75)
print(f"{'n':>0}{'t_list':>12}{'t_tup':>15}{'t_str':>17}{'t_set':>15}")
print("=" * 75)
for n in [100, 200, 300, 400, 500, 600,700,800,900,1000]:
    print(f"{n:<4}\t{1000*time_f(built_in,L,l1, n_trials=n):<10.3g}\t{1000*time_f(built_in,P ,s1, n_trials=n):<10.3g}\t{1000*time_f(built_in,Str,z1, n_trials=n):<10.3g}\t{1000*time_f(built_in,S,t1, n_trials=n):<10.3g}\t")
