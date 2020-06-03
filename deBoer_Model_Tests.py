import unittest
from deBoer_Model_Implementation import generate_gaussian_noise_ki
from deBoer_Model_Implementation import calculate_pulse_pressure
from deBoer_Model_Implementation import calculate_diastolic_pressure
from deBoer_Model_Implementation import calculate_systolic_pressure
from deBoer_Model_Implementation import calculate_effective_systolic_pressure
from deBoer_Model_Implementation import calculate_weighted_sum_previous_systolic_values
from deBoer_Model_Implementation import calculate_RR_interval
from deBoer_Model_Implementation import calculate_arterial_time_constant

import numpy as np


class Model_Tests(unittest.TestCase):   
            
    def test_generate_gaussian_noise(self):
        random_generated_sample = generate_gaussian_noise_ki()
        self.assertIsNotNone(random_generated_sample)

        
    def test_calculate_pulse_pressure(self):
        previous_i_value = 10
        gaussian_noise_sample_value = 5
        respiration_value = 3
        expected_pulse_pressure_value = 0.016 * previous_i_value + gaussian_noise_sample_value + respiration_value
        actual_pulse_pressure_value = calculate_pulse_pressure(previous_i_value, gaussian_noise_sample_value, respiration_value)
        self.assertEqual(expected_pulse_pressure_value, actual_pulse_pressure_value)
        
    def test_calculate_diastolic_pressure(self):
        meanD_test_value = 23
        meanT_test_value = 32
        meanI_test_value = 10
        meanS_test_value = 18
        I_test_value, T_test_value, S_test_value = 2, 1, 0
        diastolic_pressure_returned_value = calculate_diastolic_pressure(meanD_test_value, meanT_test_value, meanI_test_value, meanS_test_value, I_test_value, T_test_value, S_test_value)
        self.assertEqual(0, diastolic_pressure_returned_value)
    
    def test_calculate_systolic_pressure(self):
        diastolic_pressure_test_value = 271
        pulse_pressure_test_value = 3918
        expected_systolic_pressure_value = diastolic_pressure_test_value + pulse_pressure_test_value
        actual_systolic_pressure_value = calculate_systolic_pressure(diastolic_pressure_test_value, pulse_pressure_test_value)
        self.assertEqual(expected_systolic_pressure_value, actual_systolic_pressure_value)
        
    def test_calculate_effective_systolic_pressure(self):       
        systolic_pressure_test_value = 271
        expected_effective_sp_value = 18 * np.arctan(systolic_pressure_test_value / 18)
        actual_effective_sp_value = calculate_effective_systolic_pressure(systolic_pressure_test_value)
        self.assertEqual(expected_effective_sp_value, actual_effective_sp_value)           
        
    def test_calculate_weighted_sum_previous_systolic_values(self):
        ak_test_value = [0, 3, 4, 2]
        current_iteration_test_value = 3
        s_dash_list_test_value = [1, 2, 3]
        expected_weighted_sum = 18
        actual_weighted_sum = calculate_weighted_sum_previous_systolic_values(ak_test_value, current_iteration_test_value, s_dash_list_test_value)
        self.assertEqual(expected_weighted_sum, actual_weighted_sum)
    
    def test_calculate_RR_interval(self):
        ak_test_value = [0, 3, 4, 2]
        current_iteration_test_value = 3
        s_dash_list_test_value = [1, 2, 3]
        gaussian_noise_test_value = 18.3
        expected_RR_interval_value = 36.3
        actual_RR_interval_value = calculate_RR_interval(ak_test_value, current_iteration_test_value, gaussian_noise_test_value, s_dash_list_test_value)
        self.assertEqual(expected_RR_interval_value, actual_RR_interval_value)
        
    def test_calculate_arterial_time_constant(self):
        ak_test_value = [1, 2, 3]
        s_dash_list_test_value = [5, 2, 7]
        expected_arterial_time_constant = -50
        actual_arterial_time_constant = calculate_arterial_time_constant(ak_test_value, 1, s_dash_list_test_value)
        self.assertEqual( expected_arterial_time_constant, actual_arterial_time_constant)
        
    
        
        
        
if __name__ == '__main__':
    unittest.main()