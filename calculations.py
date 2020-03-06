import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_od_plot(np_list):
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)
    fig.suptitle('OD600', fontsize=16)

    ax1.plot(np_list[0][0:,0],np_list[0][0:,1])
    ax1.title.set_text('Reactor A')
    ax2.plot(np_list[1][0:,0],np_list[1][0:,1])
    ax2.title.set_text('Reactor B')
    ax3.plot(np_list[2][0:,0],np_list[2][0:,1])
    ax3.title.set_text('Reactor C')
    ax4.plot(np_list[3][0:,0],np_list[3][0:,1])
    ax4.title.set_text('Reactor D')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('OD600_Growth_curve.png')

def generate_ln_plot(np_list):
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)
    fig.suptitle('OD600', fontsize=16)

    ax1.plot(np_list[0][0:,0],np_list[0][0:,1])
    ax1.title.set_text('Reactor A')
    ax2.plot(np_list[1][0:,0],np_list[1][0:,1])
    ax2.title.set_text('Reactor B')
    ax3.plot(np_list[2][0:,0],np_list[2][0:,1])
    ax3.title.set_text('Reactor C')
    ax4.plot(np_list[3][0:,0],np_list[3][0:,1])
    ax4.title.set_text('Reactor D')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('OD600_Growth_curve.png')

def find_baseline(array):
    baseline = array[0,1]
    return baseline

def pandas_array(array):
    baseline = find_baseline(array)
    array[0:,1] = np.subtract(array[0:,1], baseline)
    lastzero = np.where(array[0:,1] == 0)[0][-1]
    newOD = array[lastzero+1:,]
    log_array = np.log(newOD[:,1])
    log_array = np.insert(log_array, [0]*(lastzero+1), 0, axis=None)
    pandasOD = np.concatenate((array, log_array.reshape(-1,1)), axis=1)
    pandas_array = pd.DataFrame(pandasOD, columns=(["Time (min)", "OD", "ln(OD600)"]))
    return pandas_array


# ##Plot log growth curves


# fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)
# fig.suptitle('ln(OD600)', fontsize=16)

# ax1.plot(curvefitter[0][0][0:,0],curvefitter[0][0][0:,2])
# ax1.title.set_text('Reactor A')

# ax2.plot(curvefitter[0][1][0:,0],curvefitter[0][1][0:,2])
# ax2.title.set_text('Reactor B')

# ax3.plot(curvefitter[0][2][0:,0],curvefitter[0][2][0:,2])
# ax3.title.set_text('Reactor C')

# ax4.plot(curvefitter[0][3][0:,0],curvefitter[0][3][0:,2])
# ax4.title.set_text('Reactor D')

# fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.savefig('ln(OD600)Growth_curve.png')


# reactor_names = ['A', 'B', 'C', 'D']

# x=0
# for i in reactor_names:
#     np.savetxt(f"reactor2fitter_{i}.csv", curvefitter[0][x], delimiter=",")
#     x +=1


# ## replace 0 with Nan here and merge into a single dataframe

# dataframe_list = []
# for i in range(0, len(curvefitter[1])):
#     df = curvefitter[1][i]
#     df['ln(OD600)'] = df['ln(OD600)'].replace(0, np.nan)
#     dataframe_list.append(df)

# mergeABCD = reduce(lambda x, y: pd.merge(x, y, on = 'Time (min)'), dataframe_list)
# mergeABCD.to_csv('Growthrate_summary.csv', index=True, header=True, sep=',')

# print("execution successful, check directory of file")

# f = open("C:/data/bioreactor_converter/directory.txt", "w")
# f.write(cor_dir)
# f.close()

# command = ("C:/Program Files/R/R-3.6.1/bin/x64/Rscript.exe " "--vanilla C:/data/bioreactor_converter/20200113_Bioreactor2Growthrate_subroutine.R")

# subprocess.Popen(command).wait()
