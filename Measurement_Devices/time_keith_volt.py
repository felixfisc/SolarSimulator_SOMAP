#for GCODE
import math
import time


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

import matplotlib.pyplot as plt

from utils_solarsim import PlotlyMakeHeatmap as PMH

rm = pyvisa.ResourceManager()
rm.list_resources() # list devices connected to the computer right now

#########################################################################
Keithley = rm.open_resource('GPIB0::23::INSTR') # <----- KEITHLEY ADDRESS
#########################################################################


def meas(curr, tic): #keithley measuring
   
    #Keithley.write(":SYST:BEEP   2000, 0.10")                                                          #play beep 2000Hz for 0.1sec
    Keithley.write(":SOUR:CURR:LEV ", str(curr))                                                     #str(X) X for curr applied

    result = Keithley.query(":READ?") #Trigger sweep, request data
    yvalues = Keithley.query_ascii_values(":FETC?")
    toc = perf_counter()                                                                                        #calc elapsed time
    res = {'Time [s]': toc - tic, 'Voltage [V]': yvalues, 'Current [A]': curr}     #build format how its saved

    return res               


print("Enter 'main(t_interval, t_period)'")
def main(t_interval, t_period):

############## User Input Variables ##########################################################

    curr = 0                     # we measure I_sc = Short circut voltage at 0V

############# intern data handling #########################################################

    voltage = {'Time [s]': [], 'Voltage [V]': [], 'Current [A]': []}
    VOLTAGE = pd.DataFrame(data=voltage)

##############  Output file Data   ###########################################################
    
    now_day = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day)
    now_time =  str(datetime.today().hour) + '-' + str(datetime.today().minute) + '-' + str(datetime.today().second) 
    time_info = "_for_" + str(t_period) + "every" + str(t_interval)

    dir = "Temporal_Measurements/" + now_day +'/'  # directory where output files are saved at
    if not os.path.exists(dir):
        os.makedirs(dir)

    name_csv = dir + now_time  + time_info + '_TempMea.csv'
    name_pdf = dir + now_time  + time_info + '_TempMea.pdf'

##############  Setup Keithley  ###########################################################

    Keithley.write("*RST") #Restore GPIB default conditions
    Keithley.timeout = 999000
   
    Keithley.write(":SENS:FUNC:CONC OFF") 
    Keithley.write(":SOUR:FUNC CURR") #
    Keithley.write(":SOUR:CURR:MODE FIXED")
    Keithley.write(":SENS:FUNC 'VOLT'")
    Keithley.write(":SOUR:CURR:RANG MIN")
    Keithley.write(":SOUR:CURR:LEV ", str(0)) 
    Keithley.write(":SENS:VOLT:PROT 25")
    Keithley.write(":SENS:VOLT:RANG:AUTO ON")
    Keithley.write(":FORM:ELEM VOLT")
    #Keithley.write(":SYST:BEEP:STAT 1")
    Keithley.write(":OUTP ON")                                                              #switch keithley ON

############## Rastering and triggering the measurement #####################################

    print("Starting temporal measurement")
    print("Taking measurement every " + str(t_interval) + " seconds for " + str(t_period) + " seconds.")

    tic = perf_counter()

    t = 0
    i = 0
    while t <= t_period:

        print("taking measurement for t = " + str(t))
        #take measurement
        res = meas(curr, tic)
        RES = pd.DataFrame(data=res, index = [i])                                            #build dataframe
        VOLTAGE = pd.concat([VOLTAGE, RES], axis = 0).reset_index(drop=True)    #save in file
        VOLTAGE.to_csv (name_csv, index = None, header=True, sep='\t')          #save in file with name_csv

        time.sleep(t_interval-0.1)
        t += t_interval
        i += 1



######################  Shutdown  ##########################################################

    Keithley.write(":OUTP OFF")                                                     #switch keithley OFF
    VOLTAGE.to_csv (name_csv, index = None, header=True, sep='\t')

    print("measurement over\n")

    plt.plot(VOLTAGE['Time [s]'], VOLTAGE['Voltage [V]']) 
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    plt.savefig(name_pdf)
    #plt.grid(True)
    #plt.legend() 
    plt.show()



