# lab08_9.py: Ninth lab problem
# October 15, 2015

# COMPLETE THIS FUNCTION
def number2(n):
    """Returns: the number of 2's in the digits of n.
    
    Example: number2(0) = 0
    Example: number2(2) = 1
    Example: number2(234252) = 3
    
    Parameter n: The number to check
    Precondition: n >= 0 is an int."""
    if(n==0):
        return 0
    
    if(n%10==2):
        return 1+number2(n/10)
    
    print "hhh..."
    
    return number2(n/10)


# TEST THE FUNCTION
# USE PRINT INSTEAD OF ASSERT_EQUALS FOR THE TUTOR
print 'Testing number2'
print 'Test 1 works: '+str(0 == number2(0))
print 'Test 2 works: '+str(1 == number2(2))
print 'Test 3 works: '+str(2 == number2(22))
print 'Test 4 works: '+str(2 == number2(212))
print 'Test 5 works: '+str(3 == number2(234252))
