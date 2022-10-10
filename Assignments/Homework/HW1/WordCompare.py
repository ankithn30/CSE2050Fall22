#setting up function, "word_compare", should comapare the two words that are imported into it 
def word_compare(w1, w2="steal"):
    #checking if either w1 or w2 is an int
    check_int = isinstance(w1, int)
    check_int2 = isinstance(w2,int)
    #implementing if either are True
    if check_int or check_int2 == True:
        return "Those aren't strings!"
    #if not an int
    else:
        #compares the length between both strings
        #we are working with an if within an if where it checks if both words have the same length and 
        #also include the same letters when "sorted()", then it prompts through the if/else statment 
        if len(w1) == len(w2):
            #implementing sorted() to check if both strings have identical letters
            new_w1 = sorted(w1)
            new_w2 = sorted(w2)
            #if both strings are the same, and include the same letters 
            if new_w1 == new_w2:
                return "Anagram"
            #if they dont include the same letters
            elif new_w1 != new_w2:
                return(w1,w2)
        #if both lengths are different, both are simply returned 
        else:
            return w1,w2
            