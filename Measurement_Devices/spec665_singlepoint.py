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
myPR655 = PR655("COM7") # spectrometer camera
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



def main(h_mm):
############# intern data handling #########################################################
    
    spectrum_integrated = {'Time [s]': [], 'x [mm]': [], 'y [mm]': [], 'Wavelength Intervall [nm]': [], 'Integrated Intensity [A.U.]': []}
    SPECTRUM_INTEGRATED = pd.DataFrame(data=spectrum_integrated)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    size_info = '_h' + str(h_mm)   # info about sample size and number of gridpoints 

    dir = "Spectrometer_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + size_info + '_665_1Mea.csv'
    name_pdf = dir + now_time  + size_info + '_665_1Mea.pdf'



############## Rastering and triggering the measurement #####################################

    print("Starting 665 rastering\n")
    print("Make sure tripod is in the SpectraScan PR665 position and ND filter is on")
    print("Make sure PR665 is plugged into correct COM port and turned on")
    print("Put sample on position x = 0, y = 0, [cm]")
    input("Press Enter to continue...")


    spectrum = {'Wavelength [nm]': [], 'Intensity [A.U.]': []}
    SPECTRUM = pd.DataFrame(data=spectrum)

    #start scan
    wavelengths, data_array= safe_meas()

    j = 0
    for i in wavelengths:
        res = {'Wavelength [nm]': wavelengths[j], 'Intensity [A.U.]': data_array[j]}
        RES = pd.DataFrame(data=res, index = [j])
        SPECTRUM = pd.concat([SPECTRUM,RES], axis = 0).reset_index(drop=True)
        j += 1                                                                                    

    # Step 2.0a
    SPECTRUM.to_csv(name_csv, index = None, header = True, sep = '\t')


######################  Shutdown  ##########################################################
    print("measurement over\n")

