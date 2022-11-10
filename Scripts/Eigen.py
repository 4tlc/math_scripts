from Printing import *
import numpy as np

def main():
    a = gatherData("Matrix")
    try:
        w, v = np.linalg.eig(a)
    except:
        prRed("Computation did not converge")
        exit()
    print(w)
    print(v)

def gatherData(name):
    prPurple("Matrix " + name)
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
    except:
        prRed("That is not a number")
        exit()
    if numRow != numCol:
        prRed("Not a square matrix")
        exit()
    try:
        entries = list(map(np.double, input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = np.array(entries).reshape(numRow, numCol)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    prLightGray(matrix)
    prYellow("------------")
    return matrix

if __name__ == "__main__":
    main()
