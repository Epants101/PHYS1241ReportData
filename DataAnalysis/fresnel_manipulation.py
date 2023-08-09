import numpy as np
import pandas as pd

ANGLE_ERROR=1
INTENSITY_RESOLUTION=0.001
INTENSITY_ERROR=INTENSITY_RESOLUTION/2
SCALING_FACTOR=1
SCALING_ERROR=0.016

raw_data=pd.read_csv("./RawData/Fresnel.csv")
angles=np.unique(raw_data["Angle"].to_numpy())

angles_output=[]
systematic_errors_angle=[]
mean_intensity_with=[]
standard_error_intensity_with=[]
mean_intensity_without=[]
standard_error_intensity_without=[]

for angle in angles:
    angle_data=raw_data.loc[raw_data["Angle"] == angle]
    angles_output.append(angle)
    systematic_errors_angle.append(ANGLE_ERROR)
    mean_intensity_with.append(angle_data["with_light"].mean())
    standard_error_intensity_with.append(angle_data["with_light"].sem())
    mean_intensity_without.append(angle_data["without_light"].mean())
    standard_error_intensity_without.append(angle_data["without_light"].sem())

data=pd.DataFrame({'ang': angles_output, 'ang_err': systematic_errors_angle, 'rel_int_with': mean_intensity_with, 'rel_int_with_stat': standard_error_intensity_with, 'rel_int_without': mean_intensity_without, 'rel_int_without_stat': standard_error_intensity_without})
data["ang"]=np.deg2rad(data["ang"])
data["ang_err"]=np.deg2rad(data["ang_err"])

data["rel_int_with_syst"]=np.sqrt((INTENSITY_ERROR/SCALING_FACTOR)**2+(data["rel_int_with"]*SCALING_ERROR/SCALING_FACTOR**2)**2)
data["rel_int_without_syst"]=np.sqrt((INTENSITY_ERROR/SCALING_FACTOR)**2+(data["rel_int_without"]*SCALING_ERROR/SCALING_FACTOR**2)**2)
data["rel_int_with"]=data["rel_int_with"]/SCALING_FACTOR
data["rel_int_without"]=data["rel_int_without"]/SCALING_FACTOR

data["delta_int"]=data["rel_int_with"]-data["rel_int_without"]
data["delta_int_stat"]=data["rel_int_with_stat"]+data["rel_int_without_stat"]
data["delta_int_syst"]=data["rel_int_with_syst"]+data["rel_int_without_syst"]

data_delta=data[["ang","ang_err","delta_int","delta_int_stat","delta_int_syst"]]
data_delta["delta_int_err"]=np.sqrt((data_delta["delta_int_stat"])**2+(data_delta["delta_int_syst"])**2)

data_delta.to_csv("./DataAnalysis/fresnel_manipulated.csv",index=False)