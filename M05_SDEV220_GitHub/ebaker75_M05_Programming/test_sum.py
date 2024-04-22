def test_sum(): #define test case
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__": #while in this program, run test_sum()
    test_sum()
    print("Everything passed") #if test_sum() is true, print "Everything passed"

    #entry point is the command line