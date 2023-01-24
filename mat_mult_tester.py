from mat_mult import *

class TestMat:
    def test_shell(self):
        assert mat_mult([[0]],[[0]]) == [[0]]

    def test_multiplication(self):
        assert mat_mult([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]]) == [[22,28],[49,64]]
