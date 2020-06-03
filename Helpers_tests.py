import unittest
from Helpers import assign_initial_values
from Helpers import return_array_of_values_from_dict
from Helpers import append_x_coordinate_list


class Helpers_tests(unittest.TestCase):
    
    def test_assign_initial_values(self):
        initial_s = 10
        initial_d = 14
        initial_i = 12
        initial_t = 21912
        w, x, y, z = assign_initial_values(initial_s, initial_d, initial_i, initial_t) 
        self.assertEqual(21912, z)
        
    def test_return_array_of_values_from_dict(self):
        test_dictionary = {'Test Key' : 1, 'Another Test Key' : 3, 'Last test key' : 10}
        return_array = return_array_of_values_from_dict(test_dictionary)
        expected_array = [1, 3, 10]
        for i in range(len(return_array)):
            self.assertEqual(expected_array[i], return_array[i])
        
    def test_append_x_coordinate_list(self):
        x_test_value = 5
        list_brs_test_values = [10, 20, 40, 10, 10]
        expected_coordinate_list = [5, 5, 5, 5, 5]
        actual_coordinate_list = append_x_coordinate_list(x_test_value, list_brs_test_values)
        for i in range(len(expected_coordinate_list)):
            self.assertEqual(expected_coordinate_list[i], actual_coordinate_list[i])
        
if __name__ == '__main__':
    unittest.main()        
