import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

RESOLUTION=500
DROP_OUTLIER=0
PATH="./DataAnalysis/fresnel_trend_line.csv"

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

n_g=curve_fit(model,x_data,y_data,bounds=(1,np.inf))[0][0]

x=np.linspace(0,np.pi/2,RESOLUTION)
y=model(x,n_g)

df=pd.DataFrame({'x': x, 'y': y})
df.to_csv(PATH, index=False)
