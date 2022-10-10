#list, set and dictionaries are mutable 
#you add things to those three AND CHANGE them 
#Immutable: integer, float, boolean, tuple, string 

# you cannot add more to a tuple or a string 
#Numbers are put into the immmutable category at times when it needs 
#to process the data temporarily

# if you use the "is" command then it checks the memory to make sure that
#boths trings are equal to each other 

#Scenario is different for a string tho, it would print out "False" is two
#strings are the same and you do "str1 is str2"

#use the id() function to be able to see the allocation of memory 
#it would print out the specifc id for a specified object 
#Lists are ordered, tuples are ordered and strings are ordered

# L = ["a", "b", "c"]
 #L[0]
#'a'

#ls -a, prints out everything in the system, folders and hidden files
# cd .. is a quick shortcut back to the parent directory 

print("Hello Y'all") 

#mkdir is to CREATE A FOLDER
#touch is to create a dile in a specific directory 

#Crete a List of the first 100 positve integers 
L = []
for i in range(1, 101):       #Python ranges are half open, includes the start but not the end 
    L.append(i)
    print(L)

#Comprehension 
L = [i for i in range(1,101)]


#tuples can store multiple types of datav