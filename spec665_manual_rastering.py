# -*- coding: utf-8 -*-
#for GCODE
import math
import time


import numpy as np #data handling
import pandas as pd #data handling

from time import perf_counter #time counter
from datetime import datetime
from datetime import date
import os
from operator import itemgetter

from ctypes import *
from psychopy.hardware.pr import PR655
from psychopy import logging

#logging.console.setLevel(logging.ERROR)  # error messages only
#logging.console.setLevel(logging.INFO)  # will give more info
#logging.console.setLevel(logging.DEBUG)  # log all communications

from utils_solarsim import integrateBetween
from utils_solarsim import PlotlyMakeHeatmap as PMH
from utils_solarsim import load_file_csv

#########################################################################
myPR655 = PR655("COM4") # spectrometer camera
#########################################################################


def safe_meas( num_retries = 30 ):
    for attempt_no in range(num_retries):
        try:
            return myPR655.getSpectrum()
        except IndexError as error:
            if attempt_no < (num_retries - 1):
                print("Error: IndexError, trying again; Attempt no " + str(attempt_no+1) + " of " + str(num_retries))
            else:
                raise error    


def meas(x_pos, y_pos, tic): #spectrometer measuring
    x = x_pos*10 # in mm
    y = y_pos*10
    print("tanking measurement for x = " + str(x) +" and  y = " + str(y))

    spectrum = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM = pd.DataFrame(data=spectrum)

    #start scan
    wavelengths, data_array= safe_meas()

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
    """
    calibration_file_name = "Spectrometer_Measurements/Thorspec_calibration_factors.csv"
    calibration_file = load_file_csv(calibration_file_name, seperator=';')

    spectrum_cal = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM_CAL = pd.DataFrame(data=spectrum_cal)

    for i in range(SPECTRUM['Intensity [A.U.]'].__len__()):
        temp = {'Wavelength [nm]': SPECTRUM['Wavelength [nm]'][i], 
                'Intensity [A.U.]': SPECTRUM['Intensity [A.U.]'][i]*calibration_file["f_thor"][i]}
        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRUM_CAL = pd.concat([SPECTRUM_CAL, TEMP], axis = 0).reset_index(drop=True)
    SPECTRUM_CAL.to_csv("2_0a_cal.csv", index = None, header = True, sep = '\t')
    """
    ####### integrate spectrum ###########################################
    res_400_500 = integrateBetween(SPECTRUM, 'Wavelength [nm]', 'Intensity [A.U.]', 400,500)
    res_500_600 = integrateBetween(SPECTRUM, 'Wavelength [nm]', 'Intensity [A.U.]', 500,600)
    res_600_700 = integrateBetween(SPECTRUM, 'Wavelength [nm]', 'Intensity [A.U.]', 600,700)
    res_700_800 = integrateBetween(SPECTRUM, 'Wavelength [nm]', 'Intensity [A.U.]', 700,780)



    res_integrated = {'Time [s]' : [t,t,t,t],
                        'x [mm]' : [x,x,x,x],
                        'y [mm]' : [y,y,y,y],
                        'Wavelength Intervall [nm]': ["400-500", "500-600", "600-700", "700-800"], 
                        'Integrated Intensity [A.U.]': [res_400_500, res_500_600, res_600_700, res_700_800]}

    return res_integrated 


def main(x_counts, y_counts, h_mm):
############# intern data handling #########################################################
    
    spectrum_integrated = {'Time [s]': [], 'x [mm]': [], 'y [mm]': [], 'Wavelength Intervall [nm]': [], 'Integrated Intensity [A.U.]': []}
    SPECTRUM_INTEGRATED = pd.DataFrame(data=spectrum_integrated)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    size_info = '_' + str(x_counts) + 'x' + str(y_counts) + '_h' + str(h_mm)   # info about sample size and number of gridpoints 

    dir = "Spectrometer_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + size_info + '_665Mea.csv'
    name_pdf = dir + now_time  + size_info + '_665Mea.pdf'



############## Rastering and triggering the measurement #####################################

    print("Starting 665 rastering\n")
    print("Make sure tripod is in the SpectraScan PR665 position and ND filter is on")
    print("Make sure PR665 is plugged into correct COM port and turned on")
    print("Put sample on position x = 0, y = 0, [cm]")

    tic = perf_counter()


    x = 0
    y = 0
    while y < y_counts:
        while x < x_counts:
            print("Place sample to (", x, ",", y,")")
            input("Press Enter to continue...")

            #take measurement
            res_integrated = meas(x, y, tic)
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
