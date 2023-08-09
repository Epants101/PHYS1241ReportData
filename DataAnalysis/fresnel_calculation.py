import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

from matplotlib import pyplot as plt

PLOT_RESOLUTION=200
DROP_OUTLIER=-1
PLOT_RESULT=False
TRIAL_NUMBER=100000

def draw_random(data, uncertainty):
    values=[]
    for i in range(data.size):
        values.append(np.random.normal(data[i],uncertainty[i]))
    return np.array(values)

def run_trial(x,y,x_err,y_err):
    x_sample=draw_random(x, x_err)
    y_sample=draw_random(y, y_err)
    params,pcov=curve_fit(model,x_sample,y_sample,bounds=(1,np.inf))
    return params[0]

def model(x,n):
    return ((n**2*np.cos(x)-np.sqrt(n**2-np.sin(x)**2))/(n**2*np.cos(x)+np.sqrt(n**2-np.sin(x)**2)))**2

def model2(x,A):
    return A*model(x,1.52)

raw_data=pd.read_csv("./DataAnalysis/fresnel_manipulated.csv")
x_data=raw_data["ang"].to_numpy()
y_data=raw_data["delta_int"].to_numpy()
x_syst=raw_data["ang_err"].to_numpy()
x_stat=np.zeros(x_syst.size)
y_syst=raw_data["delta_int_syst"].to_numpy()
y_stat=raw_data["delta_int_stat"].to_numpy()

if DROP_OUTLIER<0:
    x_data=x_data[:DROP_OUTLIER]
    y_data=y_data[:DROP_OUTLIER]

n_syst=[]
n_stat=[]

for i in range(TRIAL_NUMBER):
    n_syst.append(run_trial(x_data,y_data,x_syst,y_syst))
    n_stat.append(run_trial(x_data,y_data,x_stat,y_stat))


print("Average: ", np.average(n_stat+n_syst))
print("Systematic Error: ", np.std(n_syst))
print("Statistical Error: ", np.std(n_stat))
print("Overall Error: ", np.sqrt(np.std(n_stat)**2+np.std(n_syst)**2))

if PLOT_RESULT:
    x_the=np.linspace(0,np.pi/2,PLOT_RESOLUTION)
    plt.plot(x_data,y_data,'ro')
    plt.plot(x_the,model(x_the,np.average(n_syst)))
    plt.plot(x_the,model(x_the,1.52))
    plt.show()