import copy


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

<<<<<<< HEAD
=======

>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497
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
<<<<<<< HEAD
        self.testT = A
        return optloc

=======

        return optloc



    
>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497
    def search_near(self, sX, sY, pX, pY):
#        print "second V"
#        print self.testT[pX][pY]
#        print self.query_x[pX-1]
#        print self.query_y[pY-1]
<<<<<<< HEAD
#        print pX,pY
#        print len(sX), len(sY)
        if( pX == 1) and (pY == 1 ):
#            sX += copy.deepcopy(self.query_x[pX-1])
#            sY += copy.deepcopy(self.query_y[pY-1])
            result = sX + "\n" + sY
            print self.query_x.lstrip("*")
            print result
            print self.query_y.lstrip("*")
            
        elif(pX == 1 ):
            sX = "*" + sX
            sY = "*" + sY #copy.deepcopy(self.query_y[pY-1]) + sY
            self.search_near(sX,sY,pX,pY-1)
        elif(pY == 1) :
            sX = "*" + sX #copy.deepcopy(self.query_x[pX-1]) + sX
            sY = "*" + sY
=======

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
>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497
            self.search_near(sX,sY,pX-1,pY)
        else:
            dia = self.testT[pX-1][pY-1]
            left = self.testT[pX-1][pY]
            up = self.testT[pX][pY-1]
<<<<<<< HEAD
            if ( dia >= left ) and ( dia >=up):
=======
            if ( dia <= left ) and ( dia <=up):
>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497
                sX = copy.deepcopy(self.query_x[pX-1]) + sX
                sY = copy.deepcopy(self.query_y[pY-1]) + sY

                self.search_near(sX,sY, pX-1, pY-1)
<<<<<<< HEAD
            elif ( left > up):
                sX = "*" + sX #copy.deepcopy(self.query_x[pX-1]) + sX
                sY = "*" + sY
                self.search_near(sX,sY, pX-1, pY)
            else:
                sX = "*" + sX
                sY = "*" + sY #copy.deepcopy(self.query_y[pY-1]) + sY
=======
            elif ( left < up):
                sX = copy.deepcopy(self.query_x[pX-1]) + sX
                sY = "_" + sY
                self.search_near(sX,sY, pX-1, pY)
            else:
                sX = "_" + sX
                sY = copy.deepcopy(self.query_y[pY-1]) + sY
>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497
                self.search_near(sX,sY, pX, pY-1)





<<<<<<< HEAD
    def back_track(self,givenX,givenY):
        pX = givenX
        pY = givenY

        
        sX = "*"* (len(self.query_x) - pX)
        sY = "*"* (len(self.query_y) - pY)
=======
    def back_track(self):
        pX = len(self.query_x)
        pY = len(self.query_y)

        sX = ""
        sY = ""
>>>>>>> abd69e351652ec05e568ad318868bb1c6e9b1497

        self.search_near(sX,sY,pX,pY)
