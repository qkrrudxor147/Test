def make_matrix(sx, sy):
    return [[0]*sy for i in xrange(sx)]

class l_table:

    def __init__(self, X, Y,gap,match,mismatch):
        self.query_x = X
        self.query_y = Y
        self.query_g = gap
        self.query_m = match
        self.query_mi = mismatch
        self.testT = []

    def make_init_T(self):
        testL = []
        for y in range(len(self.query_y)+1):
            testL.append(y)
        self.testT.append(testL)

        for x in range(len(self.query_x)):
            tmpL = [x+1]
            for y in range(len(self.query_y)):
                tmpL.append("")
            self.testT.append(tmpL)


    def local_align(self):

        A = make_matrix(len(self.query_x) + 1, len(self.query_y) + 1)

        best = 0
        optloc = (0,0)

        for i in range(1,len(self.query_x)):
            a = A[i]
            stream = ""
            for j in range(1,len(self.query_y)):

                A[i][j] = max(
                    A[i][j-1] + float(self.query_g),
                    A[i-1][j] + float(self.query_g),
                    A[i-1][j-1] + (float(self.query_m) if self.query_x[i] == self.query_y[j] else float(self.query_mi)),0)

                if A[i][j] >= best:
                    best = A[i][j]
                    optloc = (i,j)

                stream += str(a[j]) + "\t"

            print stream.rstrip("\t")

        return best, optloc

def main():
    qX = raw_input("str1 : ")
    qY = raw_input("str2 : ")
    qg = raw_input("gap penalty: ")
    qm = raw_input("match score: ")
    qmi = raw_input("mismatch penalty: ")

    print qX, qY, qg, qm, qmi

    one = l_table(qX,qY,qg,qm,qmi)

    one.make_init_T()

    print one.local_align()

main()