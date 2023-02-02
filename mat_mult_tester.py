from mat_mult import mat_mult


class TestMat:

    def test_not_empty(self):
        assert mat_mult([], []) == 254

    def test_wrong_type(self):
        assert mat_mult(2, 3) == 253
        assert mat_mult(2, [3]) == 253
        assert mat_mult('c', [[2, 3]]) == 253

    def test_presence_of_internal_lists(self):
        assert mat_mult([2], [2, 3]) == 252
        assert mat_mult([[2]], [2, 3]) == 252
        assert mat_mult([2], [[2, 3]]) == 252

    def test_mat1rows_equal_mat2cols(self):
        assert mat_mult([[2, 3]], [[3]]) == 255
        assert mat_mult([[2, 3]], [[3, 4], [5, 6], [7, 8]]) == 255

    def test_matrix_uniform_list_size(self):
        assert mat_mult([[1, 2, 3], [4, 5]], [[1, 2], [3, 4], [5, 6]]) == 106
        assert mat_mult([[1, 2, 3], [4, 5, 6]], [
                        [1, 2], [3, 4], [5, 6, 7]]) == 107

    def test_shell(self):
        assert mat_mult([[0]], [[0]]) == [[0]]

    def test_multiplication(self):
        assert mat_mult([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]) == [
            [22, 28], [49, 64]]
