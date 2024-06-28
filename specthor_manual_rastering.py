# -*- coding: utf-8 -*-
#for GCODE
import math
import time
from serial import Serial

import numpy as np #data handling
import pandas as pd #data handling

from time import perf_counter #time counter
from datetime import datetime
from datetime import date
import os
from operator import itemgetter

from ctypes import *

from utils_solarsim import integrateBetween
from utils_solarsim import PlotlyMakeHeatmap as PMH
from utils_solarsim import load_file_csv


def meas(ccs_handle, lib, x_pos, y_pos, tic): #spectrometer measuring
    x = x_pos*10 # in mm
    y = y_pos*10
    print("tanking measurement for x = " + str(x) +" and  y = " + str(y))

    spectrum = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM = pd.DataFrame(data=spectrum)

    #start scan
    lib.tlccs_startScan(ccs_handle)
    wavelengths=(c_double*3648)()
    lib.tlccs_getWavelengthData(ccs_handle, 0, byref(wavelengths), c_void_p(None), c_void_p(None))
    #retrieve data
    data_array=(c_double*3648)()
    lib.tlccs_getScanData(ccs_handle, byref(data_array))

    toc = perf_counter()   
    t = 0                                                                                               #get actual time in s
    t = toc - tic   

    j = 0
    for i in wavelengths:
        res = {'Wavelength [nm]': wavelengths[j], 'Intensity [A.U.]': data_array[j]}
        RES = pd.DataFrame(data=res, index = [j])
        SPECTRUM = pd.concat([SPECTRUM,RES], axis = 0).reset_index(drop=True)
        j += 1                                                                                    #calc elapsed time


    # Step 2.0a
    name_2_0a_csv = "2_0a.csv"
    #SPECTRUM.to_csv(name_2_0a_csv, index = None, header = True, sep = '\t')

    ########## calibrate spectrum with data from halogen lamp #######
    calibration_file_name = "Spectrometer_Measurements/Thorspec_calibration_factors.csv"
    calibration_file = load_file_csv(calibration_file_name, seperator='\t')

    spectrum_cal = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM_CAL = pd.DataFrame(data=spectrum_cal)

    for i in range(SPECTRUM['Intensity [A.U.]'].__len__()):
        temp = {'Wavelength [nm]': SPECTRUM['Wavelength [nm]'][i], 
                'Intensity [A.U.]': SPECTRUM['Intensity [A.U.]'][i]*calibration_file["f_thor"][i]}
        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRUM_CAL = pd.concat([SPECTRUM_CAL, TEMP], axis = 0).reset_index(drop=True)
    SPECTRUM_CAL.to_csv("2_0a_cal.csv", index = None, header = True, sep = '\t')

    ####### integrate spectrum ###########################################
    res_500_600 = integrateBetween(SPECTRUM_CAL, 'Wavelength [nm]', 'Intensity [A.U.]', 500,600)
    res_600_700 = integrateBetween(SPECTRUM_CAL, 'Wavelength [nm]', 'Intensity [A.U.]', 600,700)
    res_700_800 = integrateBetween(SPECTRUM_CAL, 'Wavelength [nm]', 'Intensity [A.U.]', 700,800)
    res_800_900 = integrateBetween(SPECTRUM_CAL, 'Wavelength [nm]', 'Intensity [A.U.]', 800,900)
    res_900_1100 = integrateBetween(SPECTRUM_CAL, 'Wavelength [nm]', 'Intensity [A.U.]', 900,1100)

    res_integrated = {'Time [s]' : [t,t,t,t,t],
                        'x [mm]' : [x,x,x,x,x],
                        'y [mm]' : [y,y,y,y,y],
                        'Wavelength Intervall [nm]': ["500-600", "600-700", "700-800", "800-900", "900-1100"], 
                        'Integrated Intensity [A.U.]': [res_500_600, res_600_700, res_700_800, res_800_900, res_900_1100]}

    return res_integrated 


def main(x_counts, y_counts, h_mm):

############## User Input Variables ##########################################################
       
    integration_time=c_double(0.035)  #set integration time for spectrometer in seconds, ranging from 1e-5 to 6e1

############# intern data handling #########################################################
    
    spectrum_integrated = {'Time [s]': [], 'x [mm]': [], 'y [mm]': [], 'Wavelength Intervall [nm]': [], 'Integrated Intensity [A.U.]': []}
    SPECTRUM_INTEGRATED = pd.DataFrame(data=spectrum_integrated)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    size_info = '_' + str(x_counts) + 'x' + str(y_counts) + '_h' + str(h_mm)  # info about sample size and number of gridpoints 

    dir = "Spectrometer_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + size_info + '_ThMea.csv'
    name_pdf = dir + now_time  + size_info + '_ThMea.pdf'

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

    print("Starting Thorlabs rastering")
    print("Make sure tripod is in the ThorSpec position and ND filter + LP780 filter are on")
    print("Make sure ThorSpec is plugged in")
    print("Put sample on position x = 0, y = 0, [cm], relative to midpoint (12,8)")

    tic = perf_counter()


    x = 0
    y = 0
    while y < y_counts:
        while x < x_counts:
            print("Place sample to (", x, ",", y,")")
            input("Press Enter to continue...")

            #take measurement
            res_integrated = meas(ccs_handle, lib, x, y, tic)
            RES_INTEGRATED = pd.DataFrame(data=res_integrated)                                            #build dataframe
            SPECTRUM_INTEGRATED = pd.concat([SPECTRUM_INTEGRATED, RES_INTEGRATED], axis = 0).reset_index(drop=True)    #save in file
            SPECTRUM_INTEGRATED.to_csv (name_csv, index = None, header=True, sep='\t')          #save in file with name_csv

            x+=1

        y +=1
        x = 0
        print("Next row\n")

######################  Shutdown  ##########################################################

    SPECTRUM_INTEGRATED.to_csv (name_csv, index = None, header=True, sep='\t')
    print("measurement over\n")

    #PMH.make_Heatmap(PMH.manipulate_data_NonUni_ratio(PMH.load_file_csv(name_csv, '\t')), name_pdf)

    #close spectrometer connection
    lib.tlccs_close (ccs_handle)