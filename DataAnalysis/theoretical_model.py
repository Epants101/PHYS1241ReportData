import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

RESOLUTION=500
PATH="./DataAnalysis/theoretical.csv"

#model
def model(theta_r, n_g=1.52):
    return ((n_g**2*np.cos(theta_r)-np.sqrt(n_g**2-np.sin(theta_r)**2))/(n_g**2*np.cos(theta_r)+np.sqrt(n_g**2-np.sin(theta_r)**2)))**2

x=np.linspace(0,np.pi/2,RESOLUTION)
y=model(x)

df=pd.DataFrame({'x': x, 'y': y})
df.to_csv(PATH, index=False)