import numpy as np

def viterbi(inputx, ylist, scoreFunc):
    ny = len(ylist)
    nx = len(inputx)
    backPointer = [[-1 for j in range(ny)] for i in range(nx)]
    scoreBook = [[0. for j in range(ny)] for i in range(nx)]
    for i in range(nx):
        if i == 0:
            for j in range(ny):
                scoreBook[0][j] = scoreFunc(inputx, ylist, 0, j, -1)
        else:
            for j in range(ny):
                scores = [scoreBook[i-1][t] + scoreFunc(inputx, ylist, i, j, t) for t in range(ny)]
                scoreBook[i][j] = max(value)
                backPointer[i][j] = max


if __name__ == '__main__':
    
    

