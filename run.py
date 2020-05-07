import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from models import Bioreactor
from calculations import pandas_array, calculate_growthrate

# generate input file list
directory = (input("enter file directory: ").replace("\\", "/"))
entries = os.listdir(directory)
print(directory)

# loop over txt files in subdirectory and generate tables and plots for
# each txt file
for files in entries:
    if ".txt" in files:
        print(f"processing file {files}")
        reactorname = files.split(sep=".")[0]
        reactor = Bioreactor(reactorname, directory)
        reactor.set_data()
        pandasreactor, raw_pandas_df = reactor.pandas_reactor()
        pandas_df = pd.concat(pandasreactor)
        raw_pandas_df = pd.concat(raw_pandas_df)
        # save pandas df
        raw_pandas_df.to_csv(f'./{reactorname}_dataframe.csv', index=False)
        # calculate growth rates and plots
        growth_rates = calculate_growthrate(
            pandasreactor,
            raw_pandas_df,
            reactorname,
            reactor.subreactor_names,
            reactor.allignment_od)
        growth_rate_frame = {
            'Subreactor': reactor.subreactor_names,
            'Growth Rates': growth_rates}
        growth_rate_df = pd.DataFrame.from_dict(growth_rate_frame)
        growth_rate_df['Doubling_time(min)'] = np.log(
            2) / growth_rate_df['Growth Rates']
        growth_rate_df.to_csv(f'./{reactorname}_growthrates.csv', index=False)
