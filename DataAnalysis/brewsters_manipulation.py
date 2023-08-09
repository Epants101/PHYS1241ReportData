import numpy as np
import pandas as pd

ANGLE_ERROR=1

raw_data=pd.read_csv("./RawData/Brewsters.csv")
angles=np.unique(raw_data["Angle"].to_numpy())

angles_output=[]
systematic_errors_angle=[]
mean_intensity=[]
standard_error_intensity=[]

for angle in angles:
    angle_data=raw_data.loc[raw_data["Angle"] == angle]
    angles_output.append(angle)
    systematic_errors_angle.append(ANGLE_ERROR)
    mean_intensity.append(angle_data["Intensity"].mean())
    standard_error_intensity.append(angle_data["Intensity"].std())

data=pd.DataFrame({'ang': angles_output, 'ang_err': systematic_errors_angle, 'rel_int': mean_intensity, 'rel_int_err': standard_error_intensity})
data["ang"]=np.deg2rad(data["ang"])
data["ang_err"]=np.deg2rad(data["ang_err"])

data.to_csv("./DataAnalysis/brewsters_manipulated.csv", index=False)