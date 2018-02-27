import unittest
import exercise as ex
import numpy as np
import json
import utils

class TestExercise(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = utils.load_json_as_string()

    def test_part_a_should_sort_rows(self):
        data = json.dumps([{'id': 'second', 'vintage':'25/12/2016'}, {'id':'first', 'vintage':'24/12/2016'}])
        x = ex.run_part_a(data)
        self.assertEqual(x[0]['id'], 'first')
        self.assertEqual(x[1]['id'], 'second')

    def test_part_b_X_rows_same_as_y_rows(self):
        X, y = ex.run_part_b(self.data)
        self.assertEqual(np.shape(X)[0], np.shape(y)[0])

    def test_part_b_X_has_11_columns(self):
        X, y = ex.run_part_b(self.data)
        self.assertEqual(np.shape(X)[1], 11)

    def test_part_c_16_points(self):
        x = ex.run_part_c(self.data)
        self.assertEqual(len(x.keys()), 16)

    def test_part_d_eleven_columns(self):
        x = ex.run_part_d(self.data)
        self.assertEqual(len(x.keys()), 11)

if __name__ == '__main__':
    unittest.main()
