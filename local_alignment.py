def make_matrix(sx, sy):
    return [[0]*sy for i in xrange(sx)]

class l_table:

    def __init__(self, X, Y,gap,match,mismatch):
        self.query_x = "*"+X
        self.query_y = "*"+Y
        self.query_g = gap
        self.query_m = match
        self.query_mi = mismatch
        self.testT = []


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

        return optloc



    
    def search_near(self, sX, sY, pX, pY):
#        print "second V"
#        print self.testT[pX][pY]
#        print self.query_x[pX-1]
#        print self.query_y[pY-1]

#        print len(sX), len(sY)
        if( pX == 0) and (pY == 0 ):
#            sX += copy.deepcopy(self.query_x[pX-1])
#            sY += copy.deepcopy(self.query_y[pY-1])
            result = sX + "\n" + sY
            print result
        elif(pX == 0 ):
            sX = "_" + sX
            sY = copy.deepcopy(self.query_y[pY-1]) + sY
            self.search_near(sX,sY,pX,pY-1)
        elif(pY == 0) :
            sX = copy.deepcopy(self.query_x[pX-1]) + sX
            sY = "_" + sY
            self.search_near(sX,sY,pX-1,pY)
        else:
            dia = self.testT[pX-1][pY-1]
            left = self.testT[pX-1][pY]
            up = self.testT[pX][pY-1]
            if ( dia <= left ) and ( dia <=up):
                sX = copy.deepcopy(self.query_x[pX-1]) + sX
                sY = copy.deepcopy(self.query_y[pY-1]) + sY

                self.search_near(sX,sY, pX-1, pY-1)
            elif ( left < up):
                sX = copy.deepcopy(self.query_x[pX-1]) + sX
                sY = "_" + sY
                self.search_near(sX,sY, pX-1, pY)
            else:
                sX = "_" + sX
                sY = copy.deepcopy(self.query_y[pY-1]) + sY
                self.search_near(sX,sY, pX, pY-1)





    def back_track(self):
        pX = len(self.query_x)
        pY = len(self.query_y)

        sX = ""
        sY = ""

        self.search_near(sX,sY,pX,pY)
