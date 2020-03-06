# required imports
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13, 1) # creates an array in the range of [1, 12) with an interval of 1 between any two elements [1, 2, 3,..., 12]
y = np.arange(1, 11, 1) # creates an array in the range of [1, 10) with an interval of 1 between any two elements [1, 2, 3,..., 10]

global equipotentialValues
with open('equipotentialvalues.csv', 'r') as fin:
    equipotentialValues = fin.readlines() # read every line of equipotentialvalues.csv (including newlines at the end)
    equipotentialValues = [line.strip().split(',') for line in equipotentialValues] # turn the contents of previously read csv into a 2-d array
    equipotentialValues = np.array(equipotentialValues) # cast python array into an np array
    equipotentialValues = equipotentialValues.astype(np.float) # case every element in the np array to be an np float type
    print(equipotentialValues) # 2-d array of all voltage values

X, Y = np.meshgrid(x, y) # X represents a 2-d array of all xcor values of each point in the grid
                         # Y represents a 2-d array of all ycor values of each point in the grid
# X (10 rows and 12 columns)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

# Y (10 rows and 12 columns)
# [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#  [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#  [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#  [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#  [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#  [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#  [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

Z = np.array(equipotentialValues) # store csv values as a 2-d array here

plt.contour(X, Y, Z, colors="black") # create the contour map (this does not show the plot) using X, Y, Z coordinates with a black coloring

plt.xlabel("A-L") # x-axis label
plt.ylabel("1-10") # y-axis label
plt.title("equipotentials contour map") # title
plt.legend(['equipotential field lines']) # legend
plt.show() # show the plot