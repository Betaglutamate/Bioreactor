import numpy as np
from numpy import genfromtxt
import os

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
            self.set_data()
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

            return subreactorA, subreactorB, subreactorC, subreactorD

        

    # def reformat():
    
    # ## time in minutes
    # time = my_data[1:, 0]
    # time = time *60
    # ##concatenate
    # time = time.reshape(-1, 1)
    # ODA = np.concatenate((time, OD[0:,0].reshape(-1,1)), axis=1)
    # ODB = np.concatenate((time, OD[0:,1].reshape(-1,1)), axis=1)
    # ODC = np.concatenate((time, OD[0:,2].reshape(-1,1)), axis=1)
    # ODD = np.concatenate((time, OD[0:,3].reshape(-1,1)), axis=1)
    # arraylist =[ODA, ODB, ODC, ODD]
    # arraylistnew = []
    # arraylistpandas = []
    # for array in arraylist:
    #     arraylistnew.append(find_zero(array))
    #     arraylistpandas.append(pandas_array(array))
    # return arraylistnew, arraylistpandas

reactor = Bioreactor('1.02')
print (reactor.reactornumber)
print (reactor.data)
reactor.set_data()
print (reactor.data)