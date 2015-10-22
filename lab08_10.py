# lab08_10.py: Tenth lab problem
# October 15, 2015

# COMPLETE THIS FUNCTION
def into(n, c):
    """Returns: The number of times that c divides n,
    
    Example: into(5,3) = 0 because 3 does not divide 5.
    Example: into(3*3*3*3*7,3) = 4.
    
    Parameter n: The number to be divided
    Precondition: n >= 1 is an int
    
    Parameter c: The number to divide by
    Precondition: c > 1 is an int"""
    if(n==1):
        return 0
    
    if(n%c==0):
        return 1+into(n/c,c)
    return 0



# TEST THE FUNCTION
# USE PRINT INSTEAD OF ASSERT_EQUALS FOR THE TUTOR
print 'Testing into'
print 'Test 1 works: '+str(0 == into(5,3))
print 'Test 2 works: '+str(1 == into(6,3))
print 'Test 3 works: '+str(4 == into(3*3*3*3*7,3))
print 'Test 4 works: '+str(1 == into(3*3*3*3*7,7))
print 'Test 5 works: '+str(0 == into(3*3*3*3*7,5))