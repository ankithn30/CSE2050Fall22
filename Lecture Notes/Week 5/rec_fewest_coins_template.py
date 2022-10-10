from typing import Counter


def rec_fewest_coins(coin_value_list, amt_in_cents):
    global counter
    counter +=1 
    #assume we have pennies 
    min_coins = amt_in_cents
    #Define the recursive base case: we need 1 coin
    if amt_in_cents in coin_value_list:
        return 1 
    # memoization - we've already solved this subproblem

    #Recursively search for a minimum number of coins
        # Build a list of valid coins
        #goes through eveo ry valid step and then make a recursive call to that step
    #explore every possible path

    
        # Iterate over each coin
            # Recursively call function on next smaller amount
            # Update our minimum if we have done better
   
    for coin in coin_value_list:
        if coin < amt_in_cents:
            temp_min = 1 + rec_fewest_coins(coin_value_list, amt_in_cents)
            #checkin the return value 
            if temp_min < min_coins:
                min_coins = temp_min


    solved[amt_in_cents] = min_coins
    # return min_coins
    return min_coins
    # Return min_coins


################################### Quiz ###################################
# Will this give the correct answer (fewest coins) for any amount and      #
# any list of coins?                                                       #
#    1) yes                                                                #
#    2) no                                                                 #
############################################################################
    
    
if __name__ == '__main__':
    counter = 0
    print(rec_fewest_coins([1,21,25], 63))
    print(f"counter = {counter}")


    counter = 0
    solved = dict()
    print(rec_fewest_coins([1,5,21,25], 63, dict()))
    print(f"coutner = {counter}")
    #make a dictionary every time 

    print(solved)

L = []
for key in solved:
    L.append(key)
L.sort()
print(L)