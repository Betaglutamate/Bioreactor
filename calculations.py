import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_baseline(array):
    baseline = np.average(array[0:10,1])
    return baseline

def pandas_array(array):
    baseline = find_baseline(array)
    array[0:,1] = np.subtract(array[0:,1], baseline)
    lastzero = np.where(array[0:,1] <= 0)[0][-1]
    newOD = array[lastzero+1:,]
    log_array = np.log(newOD[:,1])
    log_array = np.insert(log_array, [0]*(lastzero+1), 0, axis=None)
    pandasOD = np.concatenate((array, log_array.reshape(-1,1)), axis=1)
    pandas_array = pd.DataFrame(pandasOD, columns=(["Time (min)", "OD", "ln(OD600)"]))
    return pandas_array

def generate_OD_plot(pandas_df, reactorname):
        fig, ax = plt.subplots()
        ax.set_xlabel("x label")
        ax.set_ylabel("y label")
        pandas_df = pandas_df[pandas_df['OD'] != 0]
        pandas_df.groupby("group")['OD'].plot(x='Time (min)', y='ln(OD600)', ax=ax, legend=True, title="title")
        fig.savefig(reactorname+'_OD600')

def generate_LN_plot(pandas_df, reactorname):
        fig, ax = plt.subplots()
        ax.set_xlabel("x label")
        ax.set_ylabel("y label")
        pandas_df = pandas_df[pandas_df['ln(OD600)'] != 0]
        pandas_df.groupby("group")['ln(OD600)'].plot(x='Time (min)', y='ln(OD600)', ax=ax, legend=True, title="title")
        fig.savefig(reactorname+'_LNOD600')


def calculate_growthrate(array):
    pass
