from mypackage import mymodule

def test_top_n():
    "This is to test if our function works"
    assert mymodule.top_n([14,8,7,19,34],3) == [34,19,14],'incorrect'
    assert mymodule.top_n([18,86,90],2) == [90,86],'incorrect'
    assert mymodule.top_n([70,13,6,8,11],3) == [70,13,11],'incorrect'