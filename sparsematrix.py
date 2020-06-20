import random
import datetime

class sparsem1() :
    def __init__(self):
        self.data=None
        self.iloc=None


class sparsem2():
    data:list
    def __init__(self):
        self.data=[()]
        self.iloc=None
        self.nextj=None


def iloc1(data1):
    data2=sorted(data1,key=lambda x: str(x[0]).rjust(5)+str(x[1]).rjust(5))

    n = max([x[1] for x in data1]) + 1
    iloc=[-1]*100
    for p, e in enumerate(data2):
        if iloc[e[0]] == -1:
            iloc[e[0]] = p

    return iloc


def iloc2(data2):
    iloc=[-1]*100
    nextj=len(data2)*[-1]
    for p,e in enumerate(data2):
        if (iloc[e[0]]==-1):
            iloc[e[0]]=p
        else:
            nxt=iloc[e[0]]
            while(nextj[nxt] != -1):
                nxt=nextj[nxt]
            nextj[nxt]=p


    return iloc,nextj


def printsp1(sp1):
    counter=0
    data2=[]
    print(" \t\tSparse Matrix 1")


    for i,e in enumerate(sp1.iloc):
        final=0
        if(i==len(sp1.iloc)-1):
            if(sp1.iloc[i]!=-1):
                data2=sp1.data[sp1.iloc[i]:len(sp1.data)]
                print(i,data2)
            else:
                data2=[]
                print(i,data2)
        else:
            if(sp1.iloc[i] != -1):
                nxt=i+1


                while(sp1.iloc[nxt] == -1):
                    nxt+=1
                    if(nxt == len(sp1.iloc)):
                        final=1
                        break

                if(final==1):
                        data2=sp1.data[sp1.iloc[i]:len(sp1.data)]
                        print(i,data2)
                else:

                    if(sp1.iloc[nxt]!=-1):
                        data2=sp1.data[sp1.iloc[i]:sp1.iloc[nxt]]
                        print(i,data2)
                    else:
                        data2=[]
                        print(i,data2)
            else:
                data2=[]
                print(i,data2)

    return



def printsp2(sp2):
    data2=[]
    print(" \t\tSparse Matrix 2")
    print("   i   j   val  iloc nextj ")
    for i,e  in enumerate(sp2.iloc):
        data2=[]
        if(sp2.iloc[i]==-1):
            print(i,data2)
        else:
            data2.append(sp2.data[sp2.iloc[i]])
            nxt=sp2.nextj[sp2.iloc[i]]
            while(nxt!=-1):
                data2.append(sp2.data[nxt])
                nxt=sp2.nextj[nxt]
            data2.sort(key=lambda x:x[1])
            print(i,data2)
    return


def addsp2(val,matrix2):
    matrix2.data.append(val)
    matrix2.nextj.append(-1)
    if(matrix2.iloc[val[0]] !=-1):
            nxt=matrix2.iloc[val[0]]

            while(matrix2.nextj[nxt]!=-1):
                nxt=nextj[nxt]
            matrix2.nextj[nxt]=len(matrix2.data)-1
    else :
           matrix2.iloc[val[0]]=len(matrix2.data)-1

    return matrix2




def addsp1(val, matrix):


    x=-1
    y=0
    if(matrix.iloc[val[0]]!=-1):
        for i,e in enumerate(matrix.data):
            if((val[0]<e[0] )or (val[0]==e[0] and val[1]<e[1])):
                matrix.data.insert(i,val)
                x=i+1
                y=val[0]
                break
        if(x==-1):
            matrix.data.append(val)
            x=len(matrix.data)-1
            y=val[0]



        for i in range(x,len(matrix.data),1):
                if(matrix.data[i][0]>y):
                    matrix.iloc[matrix.data[i][0]]+=1
                    y=matrix.data[i][0]


    else:
        for i,e in enumerate(matrix.data):
            print(e)
            if(val[0]<e[0] or (val[0]==e[0] and val[1]<e[1])):
                matrix.data.insert(i,val)

                matrix.iloc[val[0]] = i
                x=i
                y=val[0]
                break
        if(x==-1):
            matrix.data.append(val)
            matrix.iloc[val[0]]=len(matrix.data)-1
            x=len(matrix.data)-1
            y=val[0]

        for i in range(x+1,len(matrix.data),1):
            if(matrix.data[i][0] > y):
                matrix.iloc[matrix.data[i][0]]+=1
                y=matrix.data[i][0]

    return matrix



def  multiplysp1(matrix):
    y=[0]*100
    x=[1]*100
    temp=[0]*100
    for i,e in enumerate(matrix.iloc):
        temp[i]=next((tmp for x,tmp in enumerate(matrix.iloc) if  x>i and tmp>-1 ),len(matrix.data) )
    for i,e in  enumerate(matrix.iloc):
        if(matrix.iloc[i]!=-1):
            for w in range(matrix.iloc[i],temp[i],1):
                y[i]+=matrix.data[w][2]*x[i]
    return y



def multiplysp2(matrix):
    y=[0]*100
    x=[1]*100
    #print(matrix.iloc)
    for i,e in enumerate(matrix.iloc):
        if(matrix.iloc[i]!=-1):
            nxt=matrix.iloc[i]
            while(nxt !=-1):
                y[i]+= matrix.data[nxt][2]*x[i]
                nxt=matrix.nextj[nxt]
        else:
            y[i]=0
    return  y


def mulsp1(matrix):
    m=100
    c = [[0] * m for _ in range(m)]
    temp=[0]*m
    for i,e in enumerate(matrix.iloc):
        temp[i]=next((tmp for x,tmp in enumerate(matrix.iloc) if  x>i and tmp>-1 ),len(matrix.data) )
    for i in range(0,m):
        drow = []
        if(matrix.iloc[i]!=-1):
            for l in range(matrix.iloc[i],temp[i],1):
                a=(matrix.data[l][1],matrix.data[l][2])
                drow.append(a)
            for j in range(i,m):
                if(matrix.iloc[j]!=-1):
                    dcol=[]
                    for z in range (matrix.iloc[j],temp[j],1):
                        p=(matrix.data[z][1],matrix.data[z][2])
                        dcol.append(p)
                    for q in drow:
                        for k in dcol:
                            if(q[0]==k[0]):
                                c[i][j]+=q[1]*k[1]
                    c[j][i]=c[i][j]

    return c


def mulsp2(matrix):

        m=100
        c = [[0] * m for _ in range(m)]
        for i  in range(m):
            drow=[]
            if(matrix.iloc[i]!=-1):
                nxt=matrix.iloc[i]
                while(nxt!=-1):
                    a=(matrix.data[nxt][1],matrix.data[nxt][2])
                    drow.append(a)
                    nxt=matrix.nextj[nxt]
                for j in range (i,m):
                    dcol=[]
                    if(matrix.iloc[j]!=-1):
                        nxt1= matrix.iloc[j]
                        while(nxt1!=-1):
                            k=(matrix.data[nxt1][1],matrix.data[nxt1][2])
                            dcol.append(k)
                            nxt1=matrix.nextj[nxt1]
                        for q in drow:
                            for k in dcol:
                                if(q[0]==k[0]):
                                    c[i][j]+=q[1]*k[1]
                        c[j][i]=c[i][j]

        return c







if __name__== "__main__":

    random.seed(1053649)
    data=[]
    for i in range(200000) :
        q=0
        i=random.randint(0,99)
        j=random.randint(0,9999)
        val=random.randint(1,99)
        x=(i,j,val)


        data.append(x)
    iloc1=iloc1(data)

    iloc,nextj = iloc2(data)
    sp1=sparsem1()

    sp1.data= sorted(data,key=lambda x: str(x[0]).rjust(5)+str(x[1]).rjust(5))

    sp1.iloc=iloc1


    printsp1(sp1) #εκτύπωση κατα γραμμές της πρώτης αραιάς μήτρας

    sp2=sparsem2()
    sp2.data=data
    sp2.iloc=iloc
    sp2.nextj=nextj

    val=(1,2,102)
    start=datetime.datetime.now()
    sp1 = addsp1(val,sp1) #πρόσθεση στοιχείου στην πρώτη αραιά μήτρα
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))
    start=datetime.datetime.now()
    sp2=addsp2(val,sp2) #Πρόσθεση στοιχείου στη δεύτερη αραιά μήτρα
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))

    printsp2(sp2) # εκτύπωση κατα γραμμές της δεύτερης αραιάς μήτρας
    start=datetime.datetime.now()
    b=multiplysp2(sp2) #Πολλαπλασιαμός της δεύτερης αραιάς μήτρας με τον ανάστροφο
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))
    for i,e in enumerate(b):

        print(i,e)


    start=datetime.datetime.now()
    a=mulsp1(sp1)  #Πολλαπλασιαμός της πρώτης αραιάς μήτρας με τον ανάστροφο
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))

    for i,e in enumerate(a):
        print(i,e)

    start=datetime.datetime.now()
    b=mulsp2(sp2) #Πολλαπλασιαμος της δευτερης αραιάς μήτρας με μοναδιαίο διανυσμα
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))
    for i,e in enumerate(b):
        print(i,e)
    start=datetime.datetime.now()
    c=multiplysp1(sp1)  # Πολλαπλασιαμος της πρώτης αραιάς μήτρας με μοναδιαίο διανυσμα
    end=datetime.datetime.now()
    print("i did that in : ",(end - start))
    for i,e in enumerate(c):
        print(i,e)
