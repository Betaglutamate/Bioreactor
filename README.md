# Bioreactor
# Bioreactor-curvefitter  This program will take a bioreactor .txt file and generate graphs and growth rates based on it

## Hard-coded parameters:
1. the first 10 values of a reactor are used to find the baseline 0 value.
2. if an OD value is lower than the OD value two reads previously the program will only discard any following values for calculation of growth rates.
3. only .txt files are analysed
4. the columns which contain the OD values for the bioreactor are hardcoded
5. OD for growth rate calculation is measured between 0.1 and 0.4
6. All curves are alligned to y=0.1 as the 0 timepoint.

## dependencies
1. numpy
2. pandas
3. matplotlib
4. sklearn
from cycler import cycler

# Instalation guide
1. install python 3.7 or higher (https://www.python.org/downloads/)
2. install dependencies by entering the following command into command prompt:
    pip install numpy pandas matplotlib sklearn
3. download the repository from github
4. navigate to the location of the repository and execute:
    python run.py
5. you will be asked for the location of your files. You can copy and paste the folder directory path into python.
6. the program will now execute
7. Your files will now be generated in the same directory.
