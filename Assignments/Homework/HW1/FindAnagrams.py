#Implementing the function "word_compare" from the file "WordCompare"
from WordCompare import word_compare

#creating a check in words 
def find_anagrams(words):
    s = "" 
    #loops through the words in the list,  
    for w1 in words:
        #setting up a list to add all of the words into 
        l  = []
        #checks for the second "pair" in the words, ex. 1-2,1-3 etc
        for w2 in words:
            #
            if w1 != w2:
            #using the function "word_compare" from the 
            #other file to check if both words are anagrams 
            #Checks whether or not each pair of words is an anagram.
                if word_compare(w1,w2) == "Anagram":
                #adding, the words, that are the same as each other into the list "l"
                    l.append(w2)
        s += w1 +": " + str(l) + '\n'
    #Returns the final "word" and wehther or not it has an anagram pair 
    return s[:-1]
#part4 assert 
#word list
words = ["dusty","study","ton","chin","inch","not","to","how","they","make","mayor","any"]
#expected list from the function above
expected_result = "dusty: ['study']\nstudy: ['dusty']\nton: ['not']\nchin: ['inch']\ninch: ['chin']\nnot: ['ton']\nto: []\nhow: []\nthey: []\nmake: []\nmayor: []\nany: []"
#This is to test to see when running the file, that it will output exactly what is written in the expected_result variable
#It puts words through the function and then it will check and see, if it matches then the program should run without any errors
assert find_anagrams(words) == expected_result


#test
assert 5>3
assert not 3>5