import numpy as np
import matplotlib.pyplot as plt

def assign_initial_values(initial_s, initial_d, initial_i, initial_t):
    s = initial_s
    d = initial_d
    i = initial_i
    t = initial_t
    return s, d, i, t

#function used for computing b_k
def double_list_values(lst):
    return [x * 2 for x in lst]

def return_array_from_list(lst):
    return np.asarray(lst)

def create_plot_from_dictionary(calculated_values_dictionary, title, ylabel, ymin= None, ymax = None):
    time_values = list(calculated_values_dictionary.keys())
    function_values = list(calculated_values_dictionary.values())
    plot = plt.plot(time_values, function_values)
    plt.title(title)
    plt.ylim(ymin, ymax)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlabel('Time(s)')
    plt.xlim(xmin=0)
    plt.grid()
    plt.show()
    return plot

def plot_blood_pressure(systolic_pressure_dictionary, diastolic_pressure_dictionary, ylabel, title, ymin = None, ymax = None):
    systolic_pressure_time_values = list(systolic_pressure_dictionary.keys())
    systolic_pressure_calculated_values = list(systolic_pressure_dictionary.values())
    plt.plot(systolic_pressure_time_values, systolic_pressure_calculated_values, label='Systolic pressure')
    
    diastolic_pressure_time_values = list(diastolic_pressure_dictionary.keys())
    diastolic_pressure_calculated_values = list(diastolic_pressure_dictionary.values())
    plt.plot(diastolic_pressure_time_values, diastolic_pressure_calculated_values, label='Diastolic pressure')
    plt.grid()
    plt.legend(loc="upper left")
    plt.xlabel('Time(s)')
    plt.title(title)
    plt.ylim(ymin, ymax)
    plt.xlim(xmin=0)
    plt.ylabel(ylabel)
    plt.show()
    
def return_array_of_values_from_dict(dictionary):
    values = dictionary.values()
    values_as_list = list(values)
    array = np.array(values_as_list)
    return array

def compute_mean_and_std(list_brs_values):
    mean = round(np.mean(list_brs_values), 2)
    std = round(np.std(list_brs_values), 2)
    return mean, std

def append_x_coordinate_list(x_value, list_brs_values):
    x_coordinates = []
    for i in range(len(list_brs_values)):
        x_coordinates.append(x_value)
    return x_coordinates