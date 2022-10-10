import File1

File1.mult(3)
x=4
print(File1.mult(3))

#Both file1 and file2 have theie own namespaces 

#File1 has the attrributes, AND you get access to evertything in that module 
#file2 is used for testing
#File1 namespace gets pasted into file2 namesapce 

print(File1.x)

#Wriitng your own module, will look at the local directory and then the pythn direcotry, and if it cannot find it, then it will throw an error 
