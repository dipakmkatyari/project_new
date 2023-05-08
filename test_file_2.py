class Test_1:
    def test_div(self):
        a=10
        b=20
        c=a/b
        if c==0.6:
            print("test cases passed")
            assert True
        else:
            print("test cases failed")
            assert False