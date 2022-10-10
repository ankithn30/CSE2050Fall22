x=27
def mult(p1):
    return p1*x

#print(f"name = {__name__}")
#WHen this is run, it would be "main"
#Below are the test cases 
if __name__ == 'main':
    assert mult(1) == 27
    assert mult(2) == 54
    assert mult(4) == 108
    print(f"mult(1) = {mult(1)}")
    print(f"mult(2) = {mult(2)}")

