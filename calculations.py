import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from cycler import cycler

def find_baseline(array):
    baseline = np.average(array[0:10,1])
    return baseline

def align_array(array):
    values = array['ln(OD600)']
    bool_vector = [bool(value) if not math.isnan(value) else False for value in values]
    bool_vector = pd.Series(bool_vector, name='bools')
    allign_df = array[bool_vector]
    time_zero = allign_df['Time (min)'].values[0]
    allign_df = allign_df.assign(
    new_time = lambda dataframe: dataframe['Time (min)'].map(lambda Time: Time - time_zero) 
    )
    return allign_df

def pandas_array(array):
    baseline = find_baseline(array)
    array[0:,1] = np.subtract(array[0:,1], baseline)
    lastzero = np.where(array[0:,1] <= 0)[0][-1]
    newOD = array[lastzero+1:,]
    log_array = np.log(newOD[:,1])
    log_array = np.insert(log_array, [0]*(lastzero+1), np.nan, axis=None)
    pandasOD = np.concatenate((array, log_array.reshape(-1,1)), axis=1)
    pandas_array = pd.DataFrame(pandasOD, columns=(["Time (min)", "OD", "ln(OD600)"]))
    pandas_array = align_array(pandas_array)
    return pandas_array

def generate_OD_plot(pandas_df, reactorname):
    pandas_df = pandas_df[pandas_df['OD'] != 0]
    pandas_df.set_index('new_time', inplace=True)

    fig, ax = plt.subplots()
    pandas_df.groupby("group")['OD'].plot(ax=ax, legend=True, title=reactorname+'_OD600')
    ax.set_xlabel("Time (min)")
    ax.set_ylabel(r'$OD_{[600]}$')
    ax.set_xlim(0,500)
    fig.savefig(reactorname+'_OD600')
    plt.close()

def generate_LN_plot(pandas_df, reactorname):
    pandas_df = pandas_df[pandas_df['OD'] != 0]
    pandas_df.set_index('new_time', inplace=True)

    fig, ax = plt.subplots()
    pandas_df.groupby("group")['ln(OD600)'].plot(ax=ax, legend=True, title=reactorname+'_ln_OD600')
    ax.set_xlabel("Time (min)")
    ax.set_ylabel(r'$ln(OD_{[600]})$')
    ax.set_xlim(0,500)
    fig.savefig(reactorname+'_ln_OD600')
    plt.close()


def calculate_growthrate(pandasreactor, reactorname, subreactor_name):
    growth_rates = []
    for i in range(0,4):
        name_of_reactor = subreactor_name[i]
        current_reactor = pandasreactor[i]
        current_reactor_growthrate = current_reactor[(current_reactor['OD'] > 0.1) & (current_reactor['OD'] <0.4)]
        finaltime_list = []
        for i in range(0,len(current_reactor_growthrate['OD'])-2):
                if current_reactor_growthrate['OD'].values[i+2] <= current_reactor_growthrate['OD'].values[i]:
                     finaltime_list.append(i)
        if len(finaltime_list) != 0:
            finaltime = np.min(finaltime_list)
            current_reactor_growthrate = current_reactor_growthrate[0:finaltime]

        X = current_reactor_growthrate.get('Time (min)').values.reshape(-1, 1)  # values converts it into a numpy array
        Y = current_reactor_growthrate.get('ln(OD600)').values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        growth_rate = (linear_regressor.coef_)[0][0]
        growth_rates.append(growth_rate)

        plt.rc('axes', prop_cycle=(cycler('color', ['tab:blue', 'tab:orange', 'tab:green', 'tab:red'])))
        plt.scatter(X, Y, label=name_of_reactor)
        plt.plot(X, Y_pred)
        

    plt.ylabel(r'$ln(OD_{[600]})$')    
    plt.xlabel("Time (min)")
    plt.legend()
    plt.title(reactorname+"Logarithmic Growth Rate")
    plt.savefig(reactorname+'predicted_growthrate')
    plt.close()

    return growth_rates

def calculate_doubling_time(row):
    np.log(2)/row


