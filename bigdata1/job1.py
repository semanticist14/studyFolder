import pandas as pd
import sys 

path = "data/mtcars.csv"
df = pd.read_csv(path)

# print(df)

qsec = df.loc[:, 'qsec']

# print(qsec)

# print(min)
# print(max)

qsec_min, qsec_max = qsec.min(), qsec.max()

qsec = [ (i-qsec_min)/(qsec_max-qsec_min) for i in qsec 
if (i-qsec_min)/(qsec_max-qsec_min)
 > 0.5 ] 

print(len(qsec))