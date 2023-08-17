import plotly.express as px
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics, math
from sklearn.linear_model import LinearRegression
import subprocess
import os

plt.rcParams["font.family"] = "Times New Roman"


dfs = pd.read_excel('face_pressure.xlsx', sheet_name=None)

chainage_list, angle_slide_wedge_list, Vertical_load_ABCDEF_list, Vertical_load_CDEF_list = [], [], [], []
Resistance_load_ADE_BCF_list, Resistance_load_ABEF_list, Design_Load_Earth_Pressure_list  = [], [], []
Design_Load_Water_Pressure_list, Design_Load_Rectangular_Support_Pressure_list = [], []

Design_Load_Circular_Support_Pressure_list, Relevant_minimum_support_pressure_crown_list = [], []

Relevant_optimum_maximum_support_pressure_invert_list, Maximum_vertical_load_above_crown_list = [], []

for name, content in dfs.items():
    chainage = content.iloc[1,2]
    angle_slide_wedge = content.iloc[48,2]
    Vertical_load_ABCDEF = content.iloc[71,2]
    Vertical_load_CDEF = content.iloc[72,2]
    Resistance_load_ADE_BCF = content.iloc[76,2]
    Resistance_load_ABEF = content.iloc[77,2]
    Design_Load_Earth_Pressure = content.iloc[80,2]
    Design_Load_Water_Pressure = content.iloc[81,2]
    Design_Load_Rectangular_Support_Pressure = content.iloc[82,2]
    Design_Load_Circular_Support_Pressure = content.iloc[83,2]
    
    Relevant_minimum_support_pressure_crown = content.iloc[115,2]
    Relevant_optimum_maximum_support_pressure_invert = content.iloc[125,2]
    Maximum_vertical_load_above_crown = content.iloc[132,2]
    
    
    chainage_list.append(chainage)
    angle_slide_wedge_list.append(angle_slide_wedge)
    Vertical_load_ABCDEF_list.append(Vertical_load_ABCDEF)
    Vertical_load_CDEF_list.append(Vertical_load_CDEF)
    Resistance_load_ADE_BCF_list.append(Resistance_load_ADE_BCF)
    Resistance_load_ABEF_list.append(Resistance_load_ABEF)
    
    Design_Load_Earth_Pressure_list.append(Design_Load_Earth_Pressure)
    Design_Load_Water_Pressure_list.append(Design_Load_Water_Pressure)
    Design_Load_Rectangular_Support_Pressure_list.append(Design_Load_Rectangular_Support_Pressure)
    Design_Load_Circular_Support_Pressure_list.append(Design_Load_Circular_Support_Pressure)
    Relevant_minimum_support_pressure_crown_list.append(Relevant_minimum_support_pressure_crown)
    Relevant_optimum_maximum_support_pressure_invert_list.append(Relevant_optimum_maximum_support_pressure_invert)
    Maximum_vertical_load_above_crown_list.append(Maximum_vertical_load_above_crown)
    
face_pressure_data = pd.DataFrame()

face_pressure_data['Chainage'] = pd.Series(chainage_list).values
face_pressure_data['Angle of Sliding Wedge'] = pd.Series(angle_slide_wedge_list).values  
 
face_pressure_data['Vertical Load (ABCDEF)'] = pd.Series(Vertical_load_ABCDEF_list).values  
face_pressure_data['Vertical Load (CDEF)'] = pd.Series(Vertical_load_CDEF_list).values  

face_pressure_data['Resistance Load (ADE+BCF)'] = pd.Series(Resistance_load_ADE_BCF_list).values
face_pressure_data['Resistance Load (ABEF)'] = pd.Series(Resistance_load_ABEF_list).values
face_pressure_data['Design Load Earth Pressure'] = pd.Series(Design_Load_Earth_Pressure_list).values
face_pressure_data['Design Load Water Pressure'] = pd.Series(Design_Load_Water_Pressure_list).values
face_pressure_data['Design Load Rectangular Support Pressure'] = pd.Series(Design_Load_Rectangular_Support_Pressure_list).values
face_pressure_data['Design Load Circular Support Pressure'] = pd.Series(Design_Load_Circular_Support_Pressure_list).values   
face_pressure_data['Relevant Minimum Support Pressure (crown)'] = pd.Series(Relevant_minimum_support_pressure_crown_list).values      
face_pressure_data['Relevant Optimum Maximum Support Pressure (invert)'] = pd.Series(Relevant_optimum_maximum_support_pressure_invert_list).values 
face_pressure_data['Maximum Vertical Load Above Crown'] = pd.Series(Maximum_vertical_load_above_crown_list).values 
face_pressure_data.to_csv('face_pressure_data.csv')