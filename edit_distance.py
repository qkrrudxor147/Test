import sys, copy

class c_table:
    def __init__(self, X, Y):
        self.query_x = X
        self.query_y = Y
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


    def cal_up(self, pX, pY):
        before_n = self.testT[pX-1][pY]
        return int(before_n) + 1
    
    def cal_left(self, pX, pY):
        before_n = self.testT[pX][pY-1]
        return int(before_n) + 1
    
    def cal_dia(self, pX, pY):
        before_n = self.testT[pX-1][pY-1]
        if ( self.query_x[pX-1] == self.query_y[pY-1] ):
            return before_n
        else:
            return int(before_n)+1

        
    def showT(self):
        for l in range(len(self.query_x)+1):
            x = self.testT[l]
            stream = ""
            for y in range(len(self.query_y)+1):
                stream += str(x[y]) +"\t" 

            print stream.rstrip("\t")
                    
        

    def do_cal(self, pX, pY):
        t = self.cal_up(pX,pY)
        if ( t > self.cal_left(pX,pY)) :
            t = self.cal_left(pX,pY)
        if ( t > self.cal_dia(pX,pY)):
            t = self.cal_dia(pX,pY)
        return t

    def mark(self):
        for x in range(len(self.query_x)):
            for y in range(len(self.query_y)):
                self.testT[x+1][y+1] = self.do_cal(x+1,y+1) 


    def search_near_old(self, sX, sY, pX, pY):
        print self.testT[pX][pY]
        print self.query_x[pX-1]
        print self.query_y[pY-1]
        
#        print len(sX), len(sY)
        if( pX == 0) and (pY == 0 ):
#            sX += copy.deepcopy(self.query_x[pX-1])
#            sY += copy.deepcopy(self.query_y[pY-1])
            result = sX + "\n" + sY
            print result
        elif(pX == 0 ):
            sX += "_"
            sY += copy.deepcopy(self.query_y[pY-1])
            self.search_near(sX,sY,pX,pY-1)
        elif(pY == 0) :
            sX += copy.deepcopy(self.query_x[pX-1])
            sY += "_"
            self.search_near(sX,sY,pX-1,pY)
        else:
            dia = self.testT[pX-1][pY-1]
            left = self.testT[pX-1][pY]
            up = self.testT[pX][pY-1]
            if ( dia <= left ) and ( dia <= up):
                sX += copy.deepcopy(self.query_x[pX-1])
                sY += copy.deepcopy(self.query_y[pY-1])
                
                self.search_near(sX,sY, pX-1, pY-1)
            elif ( left < up):
                sX += copy.deepcopy(self.query_x[pX-1])
                #sY += "_"
                self.search_near(sX,sY, pX-1, pY)
            else:
                sX += "_"
                #sY += copy.deepcopy(self.query_y[pY-1])
                self.search_near(sX,sY, pX, pY-1)

    
    def search_near(self, sX, sY, pX, pY):
        print "second V"
        print self.testT[pX][pY]
        print self.query_x[pX-1]
        print self.query_y[pY-1]
        
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




def main():
    qX = raw_input("str1 : ")
    qY = raw_input("str2 : ")
    print qX, qY

    one = c_table(qX,qY)

#    print one.query_x, one.query_y

    one.make_init_T()
#    print one.showT()
    one.mark()
    print one.showT()

    T = one.back_track()
    print T
    
main()
