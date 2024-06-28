import pandas as pd

from utils_solarsim import load_file_csv

warning_printed = False

def convert_thor_to_pr665(thor_value):
    global warning_printed
    if warning_printed == False:
        print("WARNING: The measurement devices are not calibrated properly!")
        warning_printed = True
    #pr665_value = thor_value * 0.45 #value from Halogen side maximum @35ms from 04.06.2024    
    pr665_value = thor_value * 0.25 #value from Halogen main maximum @35ms from 04.06.2024    
    #pr665_value = thor_value * 0.089 #value from 08.05.2024
    """This value was obtained for a single measurement of a Red LED both with thor and PR665.
    The distance from LED to both devices was the same. Measurement was perfomed 
    in the actual solar simulator housing with all components attached, with diffusor glass and ND filter. 
    The measurement XY position was the same for both devices.
    Integration time for thor was 0.3s"""    
    #0.05 #value from 20.03.2024
    """This value was obtained for a single measurement of a Red LED both with thor and PR665. 
    The distance from LED to device each device sensor was different, 
    but the mounting height (max possible mounting height on Ender3) remained the same.
    The measurement was taken at a local maximum I(x,y).
    This is the ratio of the local maximum values.""" 
    return pr665_value


def round_value(value):
    return round(value, 6)


def calc_mis_ch(DATA, i):
    # i = 0 : 400 - 500 nm
    # i = 1 : 500 - 600 nm
    # i = 2 : 600 - 700 nm
    # i = 3 : 700 - 800 nm
    # i = 4 : 800 - 900 nm
    # i = 5 : 900 - 1100 nm
    spectral_mis_ch = {'x [mm]': [],
                      'y [mm]': [],
                      'Wavelength Intervall [nm]': [],
                      'Mismatch': []}
    SPECTRAL_MIS_CH = pd.DataFrame(data=spectral_mis_ch)

    for j in range(DATA['y [mm]'].__len__()):
        if i == 0: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '400-500',
                    'Mismatch': DATA['Mismatch 400-500 nm'][j]}
        elif i == 1: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '500-600',
                    'Mismatch': DATA['Mismatch 500-600 nm'][j]}            
        elif i == 2: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '600-700',
                    'Mismatch': DATA['Mismatch 600-700 nm'][j]}       
        elif i == 3: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '700-800',
                    'Mismatch': DATA['Mismatch 700-800 nm'][j]}       
        elif i == 4: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '800-900',
                    'Mismatch': DATA['Mismatch 800-900 nm'][j]}       
        elif i == 5: 
            temp = {'x [mm]': DATA['x [mm]'][j],
                    'y [mm]': DATA['y [mm]'][j],
                    'Wavelength Intervall [nm]': '900-1100',
                    'Mismatch': DATA['Mismatch 900-1100 nm'][j]}       

        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRAL_MIS_CH = pd.concat([SPECTRAL_MIS_CH, TEMP], axis = 0).reset_index(drop=True)
        
    return SPECTRAL_MIS_CH


def main():
    ## spectral mismatch reference values from IEC 60904-3 ##
    ref_ratio_400_500 = 18.4
    ref_ratio_500_600 = 19.9
    ref_ratio_600_700 = 18.4
    ref_ratio_700_800 = 14.9
    ref_ratio_800_900 = 12.5
    ref_ratio_900_1100 = 15.9

    ################## import data #########################
    dir = "Spectrometer_Measurements/" + "2024-6-5/"
    filename_thor = dir + "13-31-44_9x9_h25_ThMea" + ".csv"
    filename_665 = dir + "12-52-14_9x9_h25_665Mea" + ".csv"
    filename_out = "13-31-44_9x9_h25"
    data_thor = load_file_csv(filename_thor, '\t')
    data_665 = load_file_csv(filename_665, '\t')

    #warning_printed = False

    ################### merge data ##########################
    spectrum_complete = {'x [mm]': [],
                         'y [mm]': [],
                         'Integrated Intensity 400-500 nm [A.U.]': [],
                         'Integrated Intensity 500-600 nm [A.U.]': [],
                         'Integrated Intensity 600-700 nm [A.U.]': [],
                         'Integrated Intensity 700-800 nm [A.U.]': [],
                         'Integrated Intensity 800-900 nm [A.U.]': [],
                         'Integrated Intensity 900-1100 nm [A.U.]': []}
    SPECTRUM_COMPLETE = pd.DataFrame(data=spectrum_complete)

    print(data_665['y [mm]'].__len__())
    print(data_thor['y [mm]'].__len__())

    j = 0
    for i in range(int(data_665["y [mm]"].__len__()/4)):
        ####### get data from PR665, 400-500 nm, 500-600 nm, 600-700 nm 700-800 nm ###########
        ####### then get data from spectrometer, 800-900 nm, 900-1100 nm ## skip the first 3 values for each point (LP Filter > 780 nm)
            temp = {'x [mm]': data_665['x [mm]'][4*i],
                    'y [mm]': data_665['y [mm]'][4*i],
                    'Integrated Intensity 400-500 nm [A.U.]': data_665['Integrated Intensity [A.U.]'][4*i],
                    'Integrated Intensity 500-600 nm [A.U.]': data_665['Integrated Intensity [A.U.]'][4*i+1],
                    'Integrated Intensity 600-700 nm [A.U.]': data_665['Integrated Intensity [A.U.]'][4*i+2],
                    'Integrated Intensity 700-800 nm [A.U.]': data_665['Integrated Intensity [A.U.]'][4*i+3],
                    'Integrated Intensity 800-900 nm [A.U.]': convert_thor_to_pr665(data_thor['Integrated Intensity [A.U.]'][5*i+3]),  
                    'Integrated Intensity 900-1100 nm [A.U.]': convert_thor_to_pr665(data_thor['Integrated Intensity [A.U.]'][5*i+4])}
            TEMP = pd.DataFrame(data=temp, index = [0])
            SPECTRUM_COMPLETE = pd.concat([SPECTRUM_COMPLETE, TEMP], axis = 0).reset_index(drop=True)

    SPECTRUM_COMPLETE.to_csv(dir + filename_out + "_SpCom.csv", sep= '\t')

    #### calculate the sum of intensity [A.U] for each point ####
    ###### calculate the ratio of intensity for each point ######
    spectral_ratio = {'x [mm]': [],
                      'y [mm]': [],
                      'Ratio 400-500 nm [%]': [],
                      'Ratio 500-600 nm [%]': [],
                      'Ratio 600-700 nm [%]': [],
                      'Ratio 700-800 nm [%]': [],
                      'Ratio 800-900 nm [%]': [],
                      'Ratio 900-1100 nm [%]': []}
    SPECTRAL_RATIO = pd.DataFrame(data=spectral_ratio)

    for i in range(SPECTRUM_COMPLETE['y [mm]'].__len__()):
        sum = 0
        sum += SPECTRUM_COMPLETE['Integrated Intensity 400-500 nm [A.U.]'][i] 
        sum += SPECTRUM_COMPLETE['Integrated Intensity 500-600 nm [A.U.]'][i] 
        sum += SPECTRUM_COMPLETE['Integrated Intensity 600-700 nm [A.U.]'][i] 
        sum += SPECTRUM_COMPLETE['Integrated Intensity 700-800 nm [A.U.]'][i] 
        sum += SPECTRUM_COMPLETE['Integrated Intensity 800-900 nm [A.U.]'][i]
        sum += SPECTRUM_COMPLETE['Integrated Intensity 900-1100 nm [A.U.]'][i]
        
        temp = {'x [mm]': SPECTRUM_COMPLETE['x [mm]'][i],
                'y [mm]': SPECTRUM_COMPLETE['y [mm]'][i],
                'Ratio 400-500 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 400-500 nm [A.U.]'][i]*100 /sum,
                'Ratio 500-600 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 500-600 nm [A.U.]'][i]*100 /sum,
                'Ratio 600-700 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 600-700 nm [A.U.]'][i]*100 /sum,
                'Ratio 700-800 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 700-800 nm [A.U.]'][i]*100 /sum,
                'Ratio 800-900 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 800-900 nm [A.U.]'][i]*100 /sum,
                'Ratio 900-1100 nm [%]': SPECTRUM_COMPLETE['Integrated Intensity 900-1100 nm [A.U.]'][i]*100 /sum}
        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRAL_RATIO = pd.concat([SPECTRAL_RATIO, TEMP], axis = 0).reset_index(drop=True)
    # Breakout point für spectral ratio
    SPECTRAL_RATIO.to_csv(dir + filename_out + "_SpRat.csv", sep='\t')
    
    ###### calculate spectral mismatch for each point ######
    spectral_mis = {'x [mm]': [],
                    'y [mm]': [],
                    'Mismatch 400-500 nm': [],
                    'Mismatch 500-600 nm': [],
                    'Mismatch 600-700 nm': [],
                    'Mismatch 700-800 nm': [],
                    'Mismatch 800-900 nm': [],
                    'Mismatch 900-1100 nm': []}
    SPECTRAL_MIS = pd.DataFrame(data=spectral_mis)

    for i in range(SPECTRAL_RATIO['y [mm]'].__len__()):
        temp = {'x [mm]': SPECTRAL_RATIO['x [mm]'][i],
                'y [mm]': SPECTRAL_RATIO['y [mm]'][i],
                'Mismatch 400-500 nm': round_value(SPECTRAL_RATIO['Ratio 400-500 nm [%]'][i]/ref_ratio_400_500),
                'Mismatch 500-600 nm': round_value(SPECTRAL_RATIO['Ratio 500-600 nm [%]'][i]/ref_ratio_500_600),
                'Mismatch 600-700 nm': round_value(SPECTRAL_RATIO['Ratio 600-700 nm [%]'][i]/ref_ratio_600_700),
                'Mismatch 700-800 nm': round_value(SPECTRAL_RATIO['Ratio 700-800 nm [%]'][i]/ref_ratio_700_800),
                'Mismatch 800-900 nm': round_value(SPECTRAL_RATIO['Ratio 800-900 nm [%]'][i]/ref_ratio_800_900),
                'Mismatch 900-1100 nm': round_value(SPECTRAL_RATIO['Ratio 900-1100 nm [%]'][i]/ref_ratio_900_1100)}
        TEMP = pd.DataFrame(data=temp, index = [0])
        SPECTRAL_MIS = pd.concat([SPECTRAL_MIS, TEMP], axis = 0).reset_index(drop=True)

    SPECTRAL_MIS.to_csv(dir + filename_out + "_SpMis.csv", sep='\t')

    ############ single channel spectral mismatch ###########
    SPECTRAL_MIS45 = calc_mis_ch(SPECTRAL_MIS, 0)
    SPECTRAL_MIS45.to_csv(dir + filename_out + "_45Mis.csv", sep='\t')    
    SPECTRAL_MIS56 = calc_mis_ch(SPECTRAL_MIS, 1)
    SPECTRAL_MIS56.to_csv(dir + filename_out + "_56Mis.csv", sep='\t')
    SPECTRAL_MIS67 = calc_mis_ch(SPECTRAL_MIS, 2)
    SPECTRAL_MIS67.to_csv(dir + filename_out + "_67Mis.csv", sep='\t')
    SPECTRAL_MIS78 = calc_mis_ch(SPECTRAL_MIS, 3)
    SPECTRAL_MIS78.to_csv(dir + filename_out + "_78Mis.csv", sep='\t')
    SPECTRAL_MIS89 = calc_mis_ch(SPECTRAL_MIS, 4)
    SPECTRAL_MIS89.to_csv(dir + filename_out + "_89Mis.csv", sep='\t')
    SPECTRAL_MIS911 = calc_mis_ch(SPECTRAL_MIS, 5)
    SPECTRAL_MIS911.to_csv(dir + filename_out + "_911Mis.csv", sep='\t')

    ############ max spectral mismatch for each point ########
    max_spectral_mis = {'x [mm]': [None]*(SPECTRAL_MIS['y [mm]'].__len__()),
                        'y [mm]': [None]*(SPECTRAL_MIS['y [mm]'].__len__()),
                        'Wavelength Intervall [nm]': [None]*(SPECTRAL_MIS['y [mm]'].__len__()),
                        'Mismatch': [1]*(SPECTRAL_MIS['y [mm]'].__len__())} #make array of only 1 with lenght of SPECTRAL_MIS

    #print(MAX_SPECTRAL_MIS)

    for i in range(SPECTRAL_MIS['y [mm]'].__len__()):
        max_spectral_mis['x [mm]'][i] = SPECTRAL_MIS['x [mm]'][i]
        max_spectral_mis['y [mm]'][i] = SPECTRAL_MIS['y [mm]'][i]

        if abs(SPECTRAL_MIS['Mismatch 400-500 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '400-500'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 400-500 nm'][i]
        if abs(SPECTRAL_MIS['Mismatch 500-600 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '500-600'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 500-600 nm'][i]
        if abs(SPECTRAL_MIS['Mismatch 600-700 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '600-700'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 600-700 nm'][i]
        if abs(SPECTRAL_MIS['Mismatch 700-800 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '700-800'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 700-800 nm'][i]
        if abs(SPECTRAL_MIS['Mismatch 800-900 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '800-900'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 800-900 nm'][i]
        if abs(SPECTRAL_MIS['Mismatch 900-1100 nm'][i] -1) > abs(max_spectral_mis['Mismatch'][i] - 1):
            max_spectral_mis['Wavelength Intervall [nm]'][i] = '900-1100'
            max_spectral_mis['Mismatch'][i] = SPECTRAL_MIS['Mismatch 900-1100 nm'][i]
        MAX_SPECTRAL_MIS = pd.DataFrame(data=max_spectral_mis)

    MAX_SPECTRAL_MIS.to_csv(dir + filename_out + "_MaxMis.csv", sep = '\t')
