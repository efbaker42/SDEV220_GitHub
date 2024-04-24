def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6" #reproduce results from previous exercise; a positive control

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6" #try sum() with a tuple
    #got the expected error message (AssertionError: Should be 6)
    #If I change the values to sum to 6, I do get the expected "Everything passed" message

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed") #if test_sum() and test_sum_tuple() are true, print "Everything passed"