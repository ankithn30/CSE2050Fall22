w1=2
w2="what"
check_int = isinstance(w1, int)
check_int2 = isinstance(w2,int)
if check_int or check_int2 == True:
    print("Those aren't strings!")
#elif w1 != w2:
    #print(w1,w2)
else:
    if len(w1) == len(w2):

        new_w1 = sorted(w1)
        new_w2 = sorted(w2)

        #if(new_w1 == new_w2):
            #return "Anagram";
        if new_w1 == new_w2:
            print("Anagram")
        elif new_w1 != new_w2:
            new_tuple = (w1,w2)
            print(new_tuple)

    else:
        print((w1,w2))

