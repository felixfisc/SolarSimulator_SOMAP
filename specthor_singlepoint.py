# -*- coding: utf-8 -*-
#for GCODE
import math
import time
from serial import Serial

import numpy as np #data handling
import pandas as pd #data handling
import matplotlib.pyplot as plt

from time import perf_counter #time counter
from datetime import datetime
from datetime import date
import os
from operator import itemgetter

from ctypes import *

from utils_solarsim import integrateBetween
from utils_solarsim import PlotlyMakeHeatmap as PMH
from utils_solarsim import load_file_csv


def main(h_mm):

############## User Input Variables ##########################################################
       
    integration_time=c_double(0.035)  #set integration time for spectrometer in seconds, ranging from 1e-5 to 6e1
    thor_to_665_factor = 0.089

############# intern data handling #########################################################
    
    spectrum_integrated = {'Time [s]': [], 'x [mm]': [], 'y [mm]': [], 'Wavelength Intervall [nm]': [], 'Integrated Intensity [A.U.]': []}
    SPECTRUM_INTEGRATED = pd.DataFrame(data=spectrum_integrated)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    size_info = '_h' + str(h_mm)  # info about sample size and number of gridpoints 

    dir = "Spectrometer_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + size_info + '_Th1Mea.csv'
    name_pdf = dir + now_time  + size_info + '_Th1Mea.pdf'

##############  Setup Spectrometer  ###########################################################

    ccs_handle=c_int(0)
    lib = cdll.LoadLibrary("C:\Program Files\IVI Foundation\VISA\Win64\Bin\TLCCS_64.dll")
    #documentation: C:\Program Files\IVI Foundation\VISA\Win64\TLCCS\Manual

    #Start Scan- Resource name will need to be adjusted
    #windows device manager -> NI-VISA USB Device -> Spectrometer -> Properties -> Details -> Device Instance ID
    lib.tlccs_init(b"USB0::0x1313::0x8087::M00290395::RAW", 1, 1, byref(ccs_handle))   

    #integration time set above
    lib.tlccs_setIntegrationTime(ccs_handle, integration_time)
                                                            #switch keithley ON

############## Rastering and triggering the measurement #####################################

    print("Starting with Thorlabs spectrometer")
    print("Make sure tripod is in the ThorSpec position and ND filter + LP780 filter are on")
    print("Make sure ThorSpec is plugged in")
    print("Put sample on position x = 0, y = 0, [cm], relative to midpoint (12,8)")
    input("Press Enter to continue...")

    spectrum = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM = pd.DataFrame(data=spectrum)

    #start scan
    lib.tlccs_startScan(ccs_handle)
    wavelengths_thor=(c_double*3648)()
    lib.tlccs_getWavelengthData(ccs_handle, 0, byref(wavelengths_thor), c_void_p(None), c_void_p(None))
    #retrieve data
    data_array_thor=(c_double*3648)()
    lib.tlccs_getScanData(ccs_handle, byref(data_array_thor))
 

    j = 0
    for i in wavelengths_thor:
        res = {'Wavelength [nm]': wavelengths_thor[j], 'Intensity [A.U.]': data_array_thor[j]}
        RES = pd.DataFrame(data=res, index = [j])
        SPECTRUM = pd.concat([SPECTRUM,RES], axis = 0).reset_index(drop=True)
        j += 1                                                             


    # Step 2.0a
    ########## calibrate spectrum with data from halogen lamp #######
    calibration_file_name = "Spectrometer_Measurements/Thorspec_calibration_factors.csv"
    calibration_file = load_file_csv(calibration_file_name, seperator='\t')

    spectrum_cal = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM_CAL = pd.DataFrame(data=spectrum_cal)

    for i in range(SPECTRUM['Intensity [A.U.]'].__len__()):
        temp = {'Wavelength [nm]': SPECTRUM['Wavelength [nm]'][i], 
                'Intensity [A.U.]': SPECTRUM['Intensity [A.U.]'][i]*calibration_file["f_thor"][i]*thor_to_665_factor}
        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRUM_CAL = pd.concat([SPECTRUM_CAL, TEMP], axis = 0).reset_index(drop=True)
    SPECTRUM_CAL.to_csv(name_csv, index = None, header = True, sep = '\t')



######################  Shutdown  ##########################################################

    print("measurement over\n")

    #close spectrometer connection
    lib.tlccs_close (ccs_handle)

    plt.plot(SPECTRUM['Wavelength [nm]'], SPECTRUM["Intensity [A.U.]"], color='g', label='raw') 
    plt.plot(SPECTRUM_CAL['Wavelength [nm]'], SPECTRUM_CAL["Intensity [A.U.]"], color='r', label='calibrated') 
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Intensity [A.U.]")
    plt.grid(True)
    plt.legend() 
    plt.show()