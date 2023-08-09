import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

RESOLUTION=500
SD_COUNT=3
PATH="./DataAnalysis/experimental_plots.csv"

#values for n
N=1.5764498760695513
N_ERR=0.02992366718534275

#model
def model(theta_r, n_g):
    return ((n_g**2*np.cos(theta_r)-np.sqrt(n_g**2-np.sin(theta_r)**2))/(n_g**2*np.cos(theta_r)+np.sqrt(n_g**2-np.sin(theta_r)**2)))**2

x=np.linspace(0,np.pi/2,RESOLUTION)
df=pd.DataFrame({'x': x})

for sd_num in range(-SD_COUNT,SD_COUNT+1):
    y=model(x, N+sd_num*N_ERR)
    df["y"+str(sd_num)]=y

df.to_csv(PATH, index=False)