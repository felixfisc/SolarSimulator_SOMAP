import math
import numpy as np
import pandas as pd
import plotly.express as px
import scipy.integrate 


from utils_solarsim import PlotlyMakeHeatmap as PMH

#callback function

def shortenArray(array, name_x, name_y, start_x, end_x):
    if end_x < start_x:
        print("Upper boundary smaller than lower boundary")
        return 0


    newArray = pd.DataFrame(data={name_x: [], name_y: []})
    j = 0
    z = 0
    for i in array[name_x]:
        if (i >= start_x) and (i < end_x):
            temp = {name_x: array[name_x][z], name_y: array[name_y][z]}
            temp2 = pd.DataFrame(temp, index = [j])
            newArray = pd.concat([newArray, temp2], axis = 0).reset_index(drop=True)
            j += 1
        z += 1
    return newArray

def integrateBetween(data, name_x, name_y, start_x, end_x):
    DataList = shortenArray(data, name_x, name_y, start_x, end_x)
    Integrated = scipy.integrate.simpson(DataList[name_y], DataList[name_x])
    return Integrated    



def test():
    AM15G_csv = 'C:/Users/Felix/Documents/JKU/Siebtes Semenster Physik/Bac/Quellen/AM15 solar spectrum/' + 'astmg173' + '.csv'
    AM0_csv = 'C:/Users/Felix/Documents/JKU/Siebtes Semenster Physik/Bac/Quellen/AM15 solar spectrum/' + 'astm_0' + '.csv'

    data_AM15G = PMH.load_file_csv(filename_in= AM15G_csv, seperator= '\t')
    data_AM0 = PMH.load_file_csv(filename_in= AM0_csv, seperator= '\t')




    ### Calculate intensity of the complete spectrum

    AM15G_completeSpectrum_W_p_m2 = scipy.integrate.simpson(data_AM15G['ASTM G15 W pro m^2 pro nm'], data_AM15G['Wavelength nm'])
    print("AM1.5G spectrum, I = " + str(round(AM15G_completeSpectrum_W_p_m2,2)) + " W/m^2")

    AM0_completeSpectrum_W_p_m2 = scipy.integrate.simpson(data_AM0['ASTM0 W pro m^2 pro nm'], data_AM0['Wavelength nm'])
    print("AM0 spectrum, I = " + str(round(AM0_completeSpectrum_W_p_m2,2)) + " W/m^2")

    ### Calculate intensity in ranges 400-500-600-700-800-900-1100 nm

    data_AM15G_below_400 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',0,400)
    inten_AM15G_below_400 = scipy.integrate.simpson(data_AM15G_below_400['ASTM G15 W pro m^2 pro nm'], data_AM15G_below_400['Wavelength nm'])
    print("AM15G spectrum below 400nm, I = " + str(round(inten_AM15G_below_400,2)) + " W/m^2")

    data_AM15G_400_500 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',400,500)
    inten_AM15G_400_500 = scipy.integrate.simpson(data_AM15G_400_500['ASTM G15 W pro m^2 pro nm'], data_AM15G_400_500['Wavelength nm'])
    print("AM15G spectrum between 400nm and 500nm, I = " + str(round(inten_AM15G_400_500,2)) + " W/m^2")

    data_AM15G_500_600 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',500,600)
    inten_AM15G_500_600 = scipy.integrate.simpson(data_AM15G_500_600['ASTM G15 W pro m^2 pro nm'], data_AM15G_500_600['Wavelength nm'])
    print("AM15G spectrum between 500nm and 600nm, I = " + str(round(inten_AM15G_500_600,2)) + " W/m^2")

    data_AM15G_600_700 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',600,700)
    inten_AM15G_600_700 = scipy.integrate.simpson(data_AM15G_600_700['ASTM G15 W pro m^2 pro nm'], data_AM15G_600_700['Wavelength nm'])
    print("AM15G spectrum between 600nm and 700nm, I = " + str(round(inten_AM15G_600_700,2)) + " W/m^2")

    data_AM15G_700_800 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',700,800)
    inten_AM15G_700_800 = scipy.integrate.simpson(data_AM15G_700_800['ASTM G15 W pro m^2 pro nm'], data_AM15G_700_800['Wavelength nm'])
    print("AM15G spectrum between 700nm and 800nm, I = " + str(round(inten_AM15G_700_800,2)) + " W/m^2")

    data_AM15G_800_900 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',800,900)
    inten_AM15G_800_900 = scipy.integrate.simpson(data_AM15G_800_900['ASTM G15 W pro m^2 pro nm'], data_AM15G_800_900['Wavelength nm'])
    print("AM15G spectrum between 800nm and 900nm, I = " + str(round(inten_AM15G_800_900,2)) + " W/m^2")

    data_AM15G_900_1100 = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',900,1100)
    inten_AM15G_900_1100 = scipy.integrate.simpson(data_AM15G_900_1100['ASTM G15 W pro m^2 pro nm'], data_AM15G_900_1100['Wavelength nm'])
    print("AM15G spectrum between 900nm and 1100nm, I = " + str(round(inten_AM15G_900_1100,2)) + " W/m^2")

    data_AM15G_1100_up = shortenArray(data_AM15G,'Wavelength nm','ASTM G15 W pro m^2 pro nm',1100,4001)
    inten_AM15G_1100_up = scipy.integrate.simpson(data_AM15G_1100_up['ASTM G15 W pro m^2 pro nm'], data_AM15G_1100_up['Wavelength nm'])
    print("AM15G spectrum between 1100nm and up, I = " + str(round(inten_AM15G_1100_up,2)) + " W/m^2")

    inten_AM0_400_500 = integrateBetween(data_AM0, 'Wavelength nm', 'ASTM0 W pro m^2 pro nm', 400, 500)
    print("AM0 spectrum between 400 nm and 500 nm, I = " + str(inten_AM0_400_500))


    """ Plots, seem legit bro
    fig = px.scatter(data_AM0, x=data_AM0['Wavelength nm'], y=data_AM0['ASTM0 W pro m^2 pro nm'], )
    fig.update_xaxes(range=[200,3000])
    fig.write_image("AM0_scatter.png")
    """
