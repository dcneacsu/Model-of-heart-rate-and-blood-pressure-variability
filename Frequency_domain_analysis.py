import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from Helpers import return_array_of_values_from_dict
from Helpers import append_x_coordinate_list
from Helpers import compute_mean_and_std

def frequency_domain_representation(calculated_values_dictionary, title, ylabel):        
    values = calculated_values_dictionary.values() #the values in the dictionary will represent the function values for each beat
    list_values = list(values)
    array = np.array(list_values) # converting to an array to apply fourier transform
    array = signal.detrend(array)
    f_spectral_density, Pxx = signal.welch(array, fs = 1, window='barthann', nfft=None, detrend='constant')
    freq_vals_dict = generate_frequency_values_dictionary(f_spectral_density, Pxx)
    I_lf, I_hf = calc_I_lf_I_hf(freq_vals_dict)
    plt.plot(f_spectral_density, Pxx)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel('Frequency(Hz)')
    plt.grid()
    plt.show()
    return I_lf, I_hf

def generate_frequency_values_dictionary(f, Pxx):
    index = 0
    frequency_values_dictionary = {}
    for frequency_value in f:
        frequency_values_dictionary.update({frequency_value : Pxx[index]})
        index+=1
    return frequency_values_dictionary

def calc_I_lf_I_hf(freq_dict):
    I_lf_vals = []
    I_hf_vals = []
    for key in freq_dict:
        if (key>0.05 and key <0.15):
            I_lf_vals.append(freq_dict[key])
        elif(key>=0.15 and key<0.35):
            I_hf_vals.append(freq_dict[key])
    meanI_lf = np.mean(I_lf_vals)
    meanI_hf = np.mean(I_hf_vals)
    return meanI_lf, meanI_hf

def plot_spectral_density(calculated_values_dict_first_signal, calculated_values_dict_second_signal):
    first_signal = return_array_of_values_from_dict(calculated_values_dict_first_signal)
    second_signal = return_array_of_values_from_dict(calculated_values_dict_second_signal)    
    f, Pxy = signal.csd(first_signal, second_signal, fs=1.0)
    plt.plot(f, Pxy)
    plt.title('Cross Spectral Density')  
    plt.grid()
    plt.show()
    
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5*fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order = order)
    y = signal.lfilter(b, a, data)
    return y

def generate_baroreflex_sensitivty_plot(subject_group1, subject_group2, subject_group3):    
    x_coordinates_group1 = append_x_coordinate_list(0, subject_group1)
    x_coordinates_group2 = append_x_coordinate_list(1, subject_group2)
    x_coordinates_group3 = append_x_coordinate_list(2, subject_group3)
    mean_group1, std_group1 = compute_mean_and_std(subject_group1)
    mean_group2, std_group2 = compute_mean_and_std(subject_group2)
    mean_group3, std_group3 = compute_mean_and_std(subject_group3)
    plt.legend()
    plt.plot(x_coordinates_group1, subject_group1, 'bo', label = f'Mean: {mean_group1} Std: {std_group1}')
    plt.plot(x_coordinates_group2, subject_group2, 'ro',label = f'Mean: {mean_group2} Std: {std_group2}')
    plt.plot(x_coordinates_group3, subject_group3, 'yo',label = f'Mean: {mean_group3} Std: {std_group3}')
    plt.grid()
    plt.legend(loc="upper left")
    plt.ylim(3, 20)
    plt.title('Baroreflex sensitivity values')
    plt.xticks(np.arange(3), ('Healthy Sedentary Elderly', 'Endurance Trained Elderly', 'Healthy Sedentary Young'))
    plt.show()