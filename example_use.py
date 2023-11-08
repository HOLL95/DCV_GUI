import os
from numpy import loadtxt
from funcs import Automated_trumpet, DCV_peak_area
import matplotlib.pyplot as plt
data_loc=os.getcwd()+"/"
area=0.07
#Works for a list of DCV files (i.e. for a trumpet plot)

"""
peak_position_filename="peak_positions.txt"
Automated_trumpet(file_list=["2023-10-10_TP_GC-Yellow_Fc_3000_1"], trumpet_file_name=peak_position_filename,data_loc=data_loc, area=area, skiprows=2)
"""
#If you just want the core interface
DCV_data=loadtxt(data_loc+"2023-10-10_TP_GC-Yellow_Fc_3000_1", skiprows=2)
time=DCV_data[:,0]
current=DCV_data[:,2]
potential=DCV_data[:,1]
dcvpeak=DCV_peak_area(time, potential, current, area)
dcvpeak.draw_background_subtract()
plt.show()