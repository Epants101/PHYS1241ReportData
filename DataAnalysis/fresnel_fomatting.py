import numpy as np
import pandas as pd

df=pd.read_csv("./RawData/Fresnel.csv")
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

pivot.to_csv("./RawData/fresnel_formatted.csv", header=["l1","l2","l3","l4","l5","d1","d2","d3","d4","d5"],index_label="angles")
#melted.to_csv("./RawData/fresnel_formatted.csv",index=False)