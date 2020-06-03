import numpy as np
import random
from Helpers import double_list_values

def generate_gaussian_noise_ki():
    mu, sigma = 0.3, 25  #mean and standard deviation
    sample = np.random.normal(mu, sigma, 1000)
    random_sample = random.choice(sample)
    return random_sample

def generate_gaussian_noise_kp():
    mu,sigma = 0.3 , 2 #mean and standard deviation
    sample = np.random.normal(mu, sigma, 1000)
    random_sample = random.choice(sample)
    return random_sample

def calculate_pulse_pressure(previous_i, gaussian_noise, respiration_value):
    ratio_of_pulse_pressure_to_previous_i = 0.016
    pulse_pressure = ratio_of_pulse_pressure_to_previous_i * previous_i + gaussian_noise + respiration_value
    return pulse_pressure

def calculate_diastolic_pressure(meanD, meanT, meanI, meanS, I, T, S):
    arterial_compliance = meanD * np.exp(meanI/meanT) / meanS
    diastolic_pressure = arterial_compliance * S * np.exp(-I/T)
    return diastolic_pressure

def calculate_systolic_pressure(d, p):     
    systolic_pressure = d + p
    return systolic_pressure

def calculate_effective_systolic_pressure(s):
    effective_systolic_pressure = 18 * np.arctan(s/18)
    return effective_systolic_pressure

def calculate_weighted_sum_previous_systolic_values(a_k, current_iteration, s_dash_list):
    sigma_constant = 0
    for i in range (0, len(a_k)):
        if i == current_iteration:
            break
        sigma_constant += a_k[i] * s_dash_list[i]
    return sigma_constant

def calculate_RR_interval(a_k, current_iteration, gaussian_noise, s_values):
    weighted_sum = calculate_weighted_sum_previous_systolic_values(a_k, current_iteration, s_values)
    RR_interval = weighted_sum + gaussian_noise
    return RR_interval

def calculate_arterial_time_constant(a_k, current_iteration, s_dash_list):
    b_k = double_list_values(a_k)
    arterial_time_constant = 0
    for i in range (1, len(b_k)):
        if i == len(s_dash_list): 
            break
        arterial_time_constant += b_k[i]* s_dash_list[i]
    return -arterial_time_constant