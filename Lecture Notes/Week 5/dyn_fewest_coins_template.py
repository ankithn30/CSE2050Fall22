def dyn_fewest_coins(coins, amt):
    #Generate a list of sub problems to solve
    L = [None] *  (amt+1)
    #Iterate over every amount of change up to amt_in_cents
        # Worst case: all pennies

        # Check with every coin if we can do better

    for i in range(amt+1):
        L[i] = i 
        #min_coins = i 

        for coin in coins:
            if coin <= i:
                temp_min = L[i-1] + 1
                if temp_min < L[i]:
                    L[i] = temp_min
        return L[amt]
    """
    for i in range(len(minCoins)):
        print("The minimum coins to make {} cents is {}".format(i,minCoins[i]))
    """


print(dyn_fewest_coins([1,5,10,21,25], 63))
print(dyn_fewest_coins([1,5,10,21,25,2,3,4], 64))
