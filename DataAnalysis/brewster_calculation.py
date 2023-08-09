import numpy as np
import pandas as pd

TRIAL_NUMBER=5000000

def draw_random(data, uncertainty):
    values=[]
    for i in range(data.size):
        values.append(np.random.normal(data[i],uncertainty[i]))
    return values

raw_data=pd.read_csv("./DataAnalysis/brewsters_manipulated.csv")
intensity=raw_data["rel_int"].to_numpy()
intensity_error=raw_data["rel_int_err"].to_numpy()
angles=raw_data["ang"].to_numpy()

minima=[]

for i in range(TRIAL_NUMBER):
    intensity_sample=draw_random(intensity,intensity_error)
    minima.append(angles[intensity_sample.index(min(intensity_sample))])

theta_b=np.average(minima)
stat_theta_b=np.std(minima)
syst_theta_b=np.average(raw_data["ang_err"].to_numpy())

print("brewsters Average: ", theta_b)
print("brewsters Statistical Error: ", stat_theta_b)
print("brewsters Systematic Error: ", syst_theta_b)

n=np.tan(theta_b)
n_stat=(np.cos(theta_b))**(-2)*stat_theta_b
n_syst=(np.cos(theta_b))**(-2)*syst_theta_b

print("n Average: ", n)
print("n Statistical Error: ", n_stat)
print("n Systematic Error: ", n_syst)
