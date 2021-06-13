import numpy as np

def printMatrixLatex(A, BlueIdx, PrintIdx):
    print "\\left[ \\begin{array}{%s}"%("c"*A.shape[1]),
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if BlueIdx[i, j]:
                print "\\textcolor{blue}{",
            if PrintIdx[i, j]:
                print A[i, j],
            else:
                print "-",
            if BlueIdx[i, j]:
                print "}",
            if j < A.shape[1] - 1:
                print "&",
        if i < A.shape[0]-1:
            print " \\\\",
    print "\\end{array} \\right] ",

if __name__ == '__main__':
    A = np.array([[3, 4], [3, -3], [4, -1], [0, 2]])
    B = np.array([[1, 2, 3], [-2, 4, 2]])
    AB = A.dot(B)
    PrintMask = np.zeros(AB.shape)
    for i in range(AB.shape[0]):
        MaskRow = np.zeros(A.shape)
        MaskRow[i, :] = 1
        for j in range(AB.shape[1]):
            PrintMask[i, j] = 1
            print "\\begin{frame}{Matrices And Matrix Multiplication}"
            print "\\[",
            printMatrixLatex(A, MaskRow, np.ones(A.shape))
            MaskCol = np.zeros(B.shape)
            MaskCol[:, j] = 1
            printMatrixLatex(B, MaskCol, np.ones(B.shape))
            print " = ",
            Mask = np.zeros(AB.shape)
            Mask[i, j] = 1
            printMatrixLatex(AB, Mask, PrintMask)
            print "\\]"
            print "\\end{frame}\n\n"

#\[ AB_{i,j} = A_i \cdot B^j \]

#\[ AB_{1, 2} = (3, 4) \cdot (3, 2) = 3(3) + 4(2) = 17 \]

#\end{frame}
