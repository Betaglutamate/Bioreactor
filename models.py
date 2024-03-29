import os
import numpy as np
from numpy import genfromtxt
from calculations import pandas_array, find_baseline


class Bioreactor:

    '''The entire bioreactor with associated data.'''
    
    allignment_od = [0.05, 0.2]

    def __init__(self, reactorname, directory, data=None):
        self.reactorname = reactorname
        self.data = data
        self.directory = directory

    def set_data(self):
        os.chdir(self.directory)
        self.data = genfromtxt(self.reactorname + '.txt', delimiter=',')
        return self.data

    # construct subreactor out of raw .txt file here. Reactor columns need to
    # be filled with OD values
    def _make_subreactor(self):
        self.subreactor_names = []
        time_column = 0
        reactorA_column = 49
        reactorB_column = 50
        reactorC_column = False
        reactorD_column = 52
        time_in_min = (self.data[1:, time_column] * 60).reshape(-1, 1)
        subreactors = []

        if reactorA_column:
            subreactorA = self.data[1:, reactorA_column].reshape(-1, 1)
            subreactorA = np.concatenate((time_in_min, subreactorA), axis=1)
            subreactorA_baseline = find_baseline(subreactorA)
            subreactorA[0:, 1] = np.subtract(
                subreactorA[0:, 1], subreactorA_baseline)
            subreactors.append(subreactorA)
            self.subreactor_names.append("reactorA")

        if reactorB_column:
            subreactorB = self.data[1:, reactorB_column].reshape(-1, 1)
            subreactorB = np.concatenate((time_in_min, subreactorB), axis=1)
            subreactorB_baseline = find_baseline(subreactorB)
            subreactorB[0:, 1] = np.subtract(
                subreactorB[0:, 1], subreactorB_baseline)
            subreactors.append(subreactorB)
            self.subreactor_names.append("reactorB")

        if reactorC_column:
            subreactorC = self.data[1:, reactorC_column].reshape(-1, 1)
            subreactorC = np.concatenate((time_in_min, subreactorC), axis=1)
            subreactorC_baseline = find_baseline(subreactorC)
            subreactorC[0:, 1] = np.subtract(
                subreactorC[0:, 1], subreactorC_baseline)
            subreactors.append(subreactorC)
            self.subreactor_names.append("reactorC")

        if reactorD_column:
            subreactorD = self.data[1:, reactorD_column].reshape(-1, 1)
            subreactorD = np.concatenate((time_in_min, subreactorD), axis=1)
            subreactorD_baseline = find_baseline(subreactorD)
            subreactorD[0:, 1] = np.subtract(
                subreactorD[0:, 1], subreactorD_baseline)
            subreactors.append(subreactorD)
            self.subreactor_names.append("reactorD")

        return subreactors

    # make pandas tables of subreactors return a 2 lists each containing 4
    # reactors
    def pandas_reactor(self):
        reactor_list = self._make_subreactor()
        self.subreactor_names = self.subreactor_names
        pandas_list = []
        pandas_df_list = []
        for i in range(0, len(reactor_list)):
            append_df, append_pandas = pandas_array(
                reactor_list[i], self.allignment_od)
            pandas_list.append(append_pandas)
            pandas_list[i].insert(3, "group", self.subreactor_names[i])
            pandas_df_list.append(append_df)
            pandas_df_list[i].insert(2, "group", self.subreactor_names[i])
        return pandas_list, pandas_df_list

