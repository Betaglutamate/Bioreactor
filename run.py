import os
import pandas as pd
import matplotlib.pyplot as plt
from models import Bioreactor
from calculations import pandas_array, generate_OD_plot, generate_LN_plot

##generate input file list
directory = (input("enter file directory: ").replace("\\", "/"))
entries = os.listdir(directory)
print(directory)

for files in entries:
    if ".TXT" in files:
        reactorname = files.split(sep=".")[0]
        reactor = Bioreactor(reactorname, directory)
        reactor.set_data()
        pandasreactor = reactor.pandas_subreactor()
        pandas_df = pd.concat(pandasreactor)
        #Generate plots
        generate_OD_plot(pandas_df, reactorname)
        generate_LN_plot(pandas_df, reactorname)
        
    




