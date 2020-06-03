# Model-of-heart-rate-and-blood-pressure-variability
Implementing deBoer's model and comparing using recordings from subjects with cardiovascular diseases.

In order to run a simulation, please clone the repository on your local machine, and run the file Heart_Rate_Blood_Pressure_Variability.py
Currently, the model is set to simulate heart rate and blood pressure variability for 26 healthy average human subjects(https://iopscience.iop.org/article/10.1088/0967-3334/21/2/310/pdf?casa_token=6kDOQwFutdwAAAAA:lIdzY2vaxV9G7OzSuu6-BuE_xiK_NwTQOzSCKSNKl49aAWTb0dUjLSlfVWjT_2Z2i--67S9a). The simulation input values can be altered, by modifying the values of meanS, meanD, meanI and meanT. These values represent the normal human averages for systolic pressure, diastolic pressure, heart rate variability and arterial time constant, but can be changed depending on the subject type you would like to simulate.

The model we have implemented closely resembles deBoer’s model(https://journals.physiology.org/doi/pdf/10.1152/ajpheart.1987.253.3.H680). It is a beat-to-beat implementation of the cardiovascular system in which the current values of the features of each beat
depend on feature values from previous beats. 
