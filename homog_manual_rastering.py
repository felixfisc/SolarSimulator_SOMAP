#for GCODE
import math
import time
from serial import Serial

#for Keithley
import pyvisa #keithley interaction
import numpy as np #data handling
import pandas as pd #data handling
#import pyvisa #keithley interaction
from time import perf_counter #time counter
from datetime import datetime
from datetime import date
import os
from operator import itemgetter

from utils_solarsim import PlotlyMakeHeatmap as PMH

rm = pyvisa.ResourceManager()
rm.list_resources() # list devices connected to the computer right now

#########################################################################
Keithley = rm.open_resource('GPIB0::23::INSTR') # <----- KEITHLEY ADDRESS
#########################################################################


def meas(voltage, x_pos, y_pos, tic): #keithley measuring
    x = x_pos*10 # in mm
    y = y_pos*10    
    print("tanking measurement for x = " + str(x) +" and  y = " + str(y))
    Keithley.write(":SYST:BEEP   2000, 0.10")                                                          #play beep 2000Hz for 0.1sec
    Keithley.write(":SOUR:VOLT:LEV ", str(voltage))                                                     #str(X) X for voltage applied

    result = Keithley.query(":READ?") #Trigger sweep, request data
    yvalues = Keithley.query_ascii_values(":FETC?")
    toc = perf_counter()   
    t = 0                                                                                               #get actual time in s
    t = toc - tic                                                                                       #calc elapsed time
    res = {'Time [s]': t, 'x [mm]': x, 'y [mm]': y, 'Voltage [V]': voltage, 'Current [A]': yvalues}     #build format how its saved

    return res               


def main(x_counts, y_counts, h_mm):

############## User Input Variables ##########################################################

    voltage = 0                     # we measure I_sc = Short circut current at 0V

############# intern data handling #########################################################

    current = {'Time [s]': [], 'x [mm]': [], 'y [mm]': [], 'Voltage [V]': [], 'Current [A]': []}
    CURRENT = pd.DataFrame(data=current)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    size_info = '_' + str(x_counts) + 'x' + str(y_counts) + '_h' + str(h_mm)  # info about sample size and number of gridpoints 

    dir = "Homogenety_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + size_info + '_HoMea.csv'
    name_pdf = dir + now_time  + size_info + '_HoMea.pdf'

##############  Setup Keithley  ###########################################################

    Keithley.write("*RST") #Restore GPIB default conditions
    Keithley.timeout = 999000
   
    Keithley.write(":SENS:FUNC:CONC OFF") 
    Keithley.write(":SOUR:FUNC VOLT") #
    Keithley.write(":SOUR:VOLT:MODE FIXED")
    Keithley.write(":SOUR:VOLT:RANG 20")
    Keithley.write(":SOUR:VOLT:LEV ", str(0)) 
    Keithley.write(":SENS:CURR:PROT 1")
    Keithley.write(":SENS:FUNC 'CURR'")
    Keithley.write(":SENS:CURR:RANG:AUTO ON")
    Keithley.write(":FORM:ELEM CURR")
    #Keithley.write(":SYST:BEEP:STAT 1")
    Keithley.write(":OUTP ON")                                                              #switch keithley ON

############## Rastering and triggering the measurement #####################################

    print("Starting homogeneity rastering")
    print("Put sample on position x = 0, y = 0, [cm]")

    tic = perf_counter()

    x = 0
    y = 0
    while y < y_counts:
        while x < x_counts:
            print("Place sample to (", x, ",", y,")")
            input("Press Enter to continue...")

            #take measurement
            res = meas(voltage, x, y, tic)
            RES = pd.DataFrame(data=res)                                            #build dataframe
            CURRENT = pd.concat([CURRENT, RES], axis = 0).reset_index(drop=True)    #save in file
            CURRENT.to_csv (name_csv, index = None, header=True, sep='\t')          #save in file with name_csv

            x+=1

        y +=1
        x = 0
        print("Next row\n")


######################  Shutdown  ##########################################################

    Keithley.write(":OUTP OFF")                                                     #switch keithley OFF
    CURRENT.to_csv (name_csv, index = None, header=True, sep='\t')
    print("measurement over\n")

    PMH.make_Heatmap(PMH.manipulate_data_NonUni_ratio(PMH.load_file_csv(name_csv, '\t')), name_pdf)




