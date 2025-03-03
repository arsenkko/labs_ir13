def zigzag_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1]) 

    return result

matrix = [
    [1, 2, 3, 4],
    [8, 7, 6, 5],
    [9, 10, 11, 12],
    [16, 15, 14, 13]
]

print(zigzag_traversal(matrix))

import unittest

class TestZigzagTraversal(unittest.TestCase):
    def test_rectangle_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(zigzag_traversal(matrix), expected)

if __name__ == "__main__":
    unittest.main()

matrix = [
    [1, 2, 3, 4],
    [8, 7, 6, 5],
    [9, 10, 11, 12],
    [16, 15, 14, 13]
]