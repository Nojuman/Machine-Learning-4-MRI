# Import Modules as needed
import numpy as np
#import seaborn as sn
import pandas as pd
from pylab import *
from mylocal_functions import * 

# ======== T2 MSME============= #
# Make list of all T2.txt files
T2_list = get_ipython().getoutput('ls ../Study_03_CBA/*T2.txt')

# Allocate variables needed for analysis
T2DF=pd.DataFrame()
TR=np.linspace(.012,.012*12,12)
# Fit T2 and construct dataframe
for names in T2_list:
    #Convert txt file to array
    YDataMatrix=txt_2_array(names)
    #Estimate T2
    T2time=fitT2(TR,YDataMatrix)
    #convert to data frame
    df_T2=pd.DataFrame(T2time.T,columns=["Infected","Healthy_R","St_Inf","Healthy_L"])
    #df_T2=pd.DataFrame(T2time.T,columns=["ROI-1","ROI-2","ROI-3","ROI-4"])
    df_info=name_2_df(names)
    df_final=pd.concat([df_T2,df_info], axis=1)
    T2DF=T2DF.append(df_final,ignore_index=True)

# Plot T2 Density ROIs 1 and 2   
figure(); T2DF[["Infected","Healthy_R","St_Inf","Healthy_L"]].plot.density(); xlabel("T2 time (sec)")


#T2DF[T2DF.Slice==1].iloc[:,:4].plot.density(); title("Slice 01"); xlim((0.025,.15))
#T2DF[T2DF.Slice==2].iloc[:,:4].plot.density(); title("Slice 02"); xlim((0.025,.15))
#T2DF[T2DF.Slice==3].iloc[:,:4].plot.density(); title("Slice 03"); xlim((0.025,.15))
T2DF[T2DF.Slice==4].iloc[:,:4].plot.density(); title("Slice 04"); xlim((0.025,.15))
T2DF[T2DF.Slice==5].iloc[:,:4].plot.density(); title("Slice 05"); xlim((0.025,.15))
