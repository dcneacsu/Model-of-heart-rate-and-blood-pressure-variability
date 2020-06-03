import math
import numpy as np
from Helpers import assign_initial_values
from Helpers import create_plot_from_dictionary
from Helpers import plot_blood_pressure
from deBoer_Model_Implementation import generate_gaussian_noise_ki
from deBoer_Model_Implementation import generate_gaussian_noise_kp
from deBoer_Model_Implementation import calculate_pulse_pressure
from deBoer_Model_Implementation import calculate_diastolic_pressure
from deBoer_Model_Implementation import calculate_systolic_pressure
from deBoer_Model_Implementation import calculate_effective_systolic_pressure
from deBoer_Model_Implementation import calculate_RR_interval
from deBoer_Model_Implementation import calculate_arterial_time_constant
from Frequency_domain_analysis import frequency_domain_representation
from Frequency_domain_analysis import plot_spectral_density
                      
def run_simulation(number_of_beats, meanS, meanD, meanI, meanT, initial_s, initial_d, initial_i, initial_t, a_k):
    arterial_time_constant_list = []
    RR_interval_dictionary = {}
    systolic_pressure_dictionary = {}
    diastolic_pressure_dictionary = {}
    
    rr_dictionary = {}
    s_dictionary = {}  #stores the s = S - meanS values for frequency plotting
    s, d, i, t = assign_initial_values(initial_s, initial_d, initial_i, initial_t) #initial values for s(n), d(n), i(n), t(n)
    S, D, I, T = assign_initial_values(meanS, meanD, meanI, meanT) #initial S(n) D(n), I(n), T(n) values
    s_dash = initial_s
    respiration = 0
    frequency = 0.25
    s_dash_list = []
    time = 0 #start_time
    for beat in range(1, number_of_beats):
        gaussian_noise_pulse_pressure = generate_gaussian_noise_kp()  
        gaussian_noise_RR_interval = generate_gaussian_noise_ki()
        respiration = np.sin((2* math.pi * frequency * time) / 1000)
        
        p = calculate_pulse_pressure(initial_i, gaussian_noise_pulse_pressure, respiration) # p(n)
        
        D = calculate_diastolic_pressure(meanD, meanT, meanI, meanS, I, T, S) # D(n)
        diastolic_pressure_dictionary.update({beat : D}) #adding D(n) value to the dictionary along with the beat number to which it corresponds
        d = D - meanD    
        
        s = calculate_systolic_pressure(d, p)
        s_dictionary.update({beat : s}) # adding the new s(n) value to the dictionary along with the beat number to which it corresponds
        s_dash = calculate_effective_systolic_pressure(s)
        s_dash_list.append(s_dash) # adding s'(n) to the list of values which will be used in calculating i(n)
        
        S = s + meanS
        systolic_pressure_dictionary.update({beat : S}) #updating dictionary with beat and value pair
        
        i = calculate_RR_interval(a_k, beat, gaussian_noise_RR_interval, s_dash_list) # i(n)
        rr_dictionary.update({beat : i})
        I = i + meanI # I(n)
        time = time + I
        RR_interval_dictionary.update({beat : I})
        
        t = calculate_arterial_time_constant(a_k, beat, s_dash_list) #t(n)
        T = t + meanT #T(n)
        arterial_time_constant_list.append(T)
    
    #Generating the time-domain and frequency-domain plots
    create_plot_from_dictionary(RR_interval_dictionary, 'Heart rate variability', 'RR Interval(ms)', 400, 1200)
    plot_blood_pressure(systolic_pressure_dictionary, diastolic_pressure_dictionary, 'BP(mmHg)', 'Blood pressure', 0, 200, )
    I_lf, I_hf = frequency_domain_representation(RR_interval_dictionary, 'Power spectra RR interval','RR Power ($ms^{2}/Hz$)') #This plot uses r(n) values simulated as those extract the mean values from the RR interval;
    S_lf, S_hf = frequency_domain_representation(systolic_pressure_dictionary, 'Power spectra SP', 'S Power ($ms^{2}/Hz$)') #This plot uses s(n) values due to the same reason as above
    Brs_lf =  math.sqrt(I_lf/S_lf)
    Brs_hf = math.sqrt(I_hf/S_hf)
    Brs = (Brs_lf + Brs_hf)/2
    plot_spectral_density(RR_interval_dictionary, systolic_pressure_dictionary)
    return I_lf, I_hf, Brs    

def main():
    a_k = [9,0,1,2,3,2,1]
    meanS = 120 #mean Systolic Pressure value
    meanD =  75 #mean Diastolic Pressure value
    meanI = 800 #mean RR interval value
    meanT = 1425 #mean arterial time constant values
    list_I_hf = [] #storing high-freq range rr interval results
    list_I_lf = [] #storing low-freq range rr interval results
    list_Baroreflex_sensitivity = []#computer baroreflex value results
    total_number_of_subjects = 26
    for i in range(total_number_of_subjects):       #for loop running for the total number of subjects to be examined
        I_lf, I_hf, Brs = run_simulation(150, meanS, meanD, meanI, meanT, 0, 0, 0, 0, a_k)
        list_I_hf.append(I_hf)
        list_I_lf.append(I_lf)
        list_Baroreflex_sensitivity.append(Brs)       
    
main()