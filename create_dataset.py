import os
import pandas as pd

outfile='portrait_itep.csv'
path='3x4'

data = {'RG': [], 'PortraitFilepath': []}

# r=root,d=directories,f=files
for r,d,f in os.walk(path):
    for file in f:
        data['RG'].append(file.split('_')[0])
        data['filepath'].append('/'.join([path, file])) # Bug: os.pathsep returning :


df=pd.DataFrame.from_dict(data)
df.to_csv(outfile, index=False)
