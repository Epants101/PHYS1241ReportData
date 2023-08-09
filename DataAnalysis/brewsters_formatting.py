import numpy as np
import pandas as pd

df=pd.read_csv("./RawData/Brewsters.csv")
angles=df["Angle"].to_numpy()
unique_angles=np.unique(df["Angle"].to_numpy())
counts=np.zeros(angles.size)

for angle in unique_angles:
    i=1
    indices=np.where(angles==angle)[0]
    for index in indices:
        counts[index]=i
        i+=1

df["Trial"]=counts
pivot=df.pivot(index="Angle",columns="Trial")
melted=df.melt(id_vars=["Angle", "Trial"])

pivot.to_csv("./RawData/brewsters_formatted.csv", header=["t1","t2","t3","t4","t5","t6","t7","t8"],index_label="angles")