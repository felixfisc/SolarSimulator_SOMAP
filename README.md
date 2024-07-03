# Solar Simulator
## Bachelor thesis July 2024
### Felix Fischer

This repository is used to archive the code that was necessary for the design and the charaterization of the solar simulator as presented in the thesis.

## Simulator_Control
This folder contains a single arduino code used to control the LED intensities with PWM signals. The AM1.5 spectrum is used by default. A custom spectrum can be used to test single LEDs. The simulator's buttons can be used to switch between the profiles.

## Measurement_Devices
Code for the characterization procedures described in section 3 in the thesis.

### Spectral Match
Singlepoint measurements to gain the whole spectrum. Two spectrometers have to be combined. Both scripts output a CSV with spectral intensity over wavelength in their operating interval. To get the complete spectrum, the CSVs have to be combined.

spec665_singlepoint.py to use with the SpectraScan PR665.
specthor_singlepoint.py to use with the Thorlabs spectrometer.

Rasterizing measurements to calculate the spectral match factor for each point in the plane. Two spectrometers have to be combined. Both of their scripts output a CSV with integrated intensity over wavelength intervals. The merger connects both CSVs, adjusts the values according to the calibration, and calculates the spectral match factor. A number of CSVs are emitted.

spec665_manual_rastering.py to use with the SpectraScan PR665.
specthor_manual_rastering.py to use with the Thorlabs spectrometer.
spec665_merge_new.py to merge both files. The name of the CSVs have to be hard-coded before use.

### Non-uniformity of irradiance
homog_manual_rastering.py triggeres the Keithley to make a measurement when ENTER key is pushed. Stores values in CSV with XY-position.

### Temporal instability
time_keith_volt.py - Keithley makes measurements after some time, for some time.

## PCBs_KiCad
Stores the PCB designs for the LED PCB as well as the LED driver PCB. Also the footprints are included.

## Result_Data
Stores the CSV that were used in the thesis.



This project is licensed under the terms of the MIT license