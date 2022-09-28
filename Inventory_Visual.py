import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plot
import seaborn as sb
import datetime as dt
 %matplotlib inline
os.chdir("C:\\Users\\ullahm2\\Downloads") 
cwd = os.getcwd() 
print (cwd)
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
root.withdraw() #Prevents the Tkinter window to come up
exlpath = askopenfilename()
root.destroy()
print(exlpath)
df = pd.read_csv(exlpath)

df1 = df[df['AVAILABLE_DATE'].notnull()]
df['AVAILABLE_DATE'] = pd.to_datetime(df['AVAILABLE_DATE'], format='%m/%d/%Y')
df['TIME_NEEDED'] = pd.to_datetime(df['TIME_NEEDED'], format='%m/%d/%Y')

df.plot.line(x = 'TIME_NEEDED', y =['BOH_WO_SS'] , title="Part: 4266490",linewidth=.8, figsize=(16,9));
plot.ylabel('BOH including SS')
plot.xlabel('Time')
plot.show(block=True);

df[df['AVAILABLE_DATE'].notnull()].BOH_WO_SS.describe()
