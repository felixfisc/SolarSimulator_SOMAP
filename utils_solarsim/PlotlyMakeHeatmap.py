import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go

filename_out = "Homogenety_Measurements/" + "filename1" + ".pdf"

def load_file_csv(filename_in, seperator):
    data = pd.read_csv(filename_in, sep = seperator)
    return data

def manipulate_data_mykroA(data):
    #change current values from [A] to [mykroA]
    for i in range(data["Current [A]"].__len__()):
        data["Current [A]"][i] = data["Current [A]"][i]*math.pow(10,6)
    return data

def manipulate_data_NonUni_ratio(data):
    #calculate nonuniformity of individual fields after G.Grandi

    #find min_value & max_value
    max_value = 0
    min_value = 100
    #reference_value = 100

    for i in range(data["Current [A]"].__len__()):
        if data["Current [A]"][i] > max_value:
            max_value = data["Current [A]"][i]
        if data["Current [A]"][i] < min_value:
            min_value = data["Current [A]"][i]
    print("max_value = " + str(max_value))
    print("min_value = " + str(min_value))

    #reference_value = (max_value+min_value)/2 #only for testing purposes
    reference_value = max_value

    for i in range(data["Current [A]"].__len__()):
        data["Current [A]"][i] = round(((data["Current [A]"][i] - reference_value) / (data["Current [A]"][i] + reference_value) * 100), 2)
    return data


def make_Heatmap(data, filename_out):
    fig = go.Figure(go.Heatmap(x = data["x [mm]"], y = data["y [mm]"], z = data["Current [A]"], text = data["Current [A]"], texttemplate="%{text}", textfont= {"size":5}))
    fig.update_yaxes(title = 'y [mm]')
    fig.update_xaxes(title = 'x [mm]')

    fig.write_image(filename_out)


def main():

    make_Heatmap(manipulate_data_NonUni_ratio(load_file_csv('C:/Users/Felix/Documents/JKU/Siebtes Semenster Physik/Bac/Python/Homogenety_Measurements/2023-10-18_18-1-21_70mm-13x13_HoMea.csv', '\t')), filename_out)