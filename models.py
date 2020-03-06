import numpy as np
from numpy import genfromtxt
import os
from calculations import pandas_array

class Bioreactor:
    '''
    The entire bioreactor including 4 subreactors
    '''

    def __init__(self, reactornumber, data = None):
        self.reactornumber = reactornumber
        self.data = data
    
    def set_data(self):
        textfilepath = input("enter file directory: ").replace("\\", "/")
        filename = input("enter file name (including .txt)")
        os.chdir(textfilepath)
        self.data = genfromtxt(filename, delimiter=',')
        return self.data

    def make_subreactor(self):
            if np.all(self.data) == None:
                self.set_data()
            else:
                time_column = 0
                reactorA_column = 5
                reactorB_column = 6
                reactorC_column = 7
                reactorD_column = 8
                time_in_min = (self.data[1:, time_column]*60).reshape(-1,1)

                subreactorA = self.data[1:, reactorA_column].reshape(-1,1)
                subreactorA = np.concatenate((time_in_min, subreactorA), axis=1)

                subreactorB = self.data[1:, reactorB_column].reshape(-1,1)
                subreactorB = np.concatenate((time_in_min, subreactorB), axis=1)

                subreactorC = self.data[1:, reactorC_column].reshape(-1,1)
                subreactorC = np.concatenate((time_in_min, subreactorC), axis=1)

                subreactorD = self.data[1:, reactorD_column].reshape(-1,1)
                subreactorD = np.concatenate((time_in_min, subreactorD), axis=1)

                return [subreactorA, subreactorB, subreactorC, subreactorD]


    def pandas_subreactor(self):
        reactor_list = self.make_subreactor()
        pandas_list = []
        for i in range(0,4):
            pandas_list.append(pandas_array(reactor_list[i]))
        return pandas_list

reactor = Bioreactor('1.02')
reactor.set_data()
reactor.make_subreactor()
pandasreactor = reactor.pandas_subreactor()