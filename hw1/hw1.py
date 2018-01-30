import numpy as np
import pandas as pd
import sys
import csv
from math import *

def readCSV():
    #read training csv and return train_x
    text=pd.read_csv('./train.csv',encoding='Big5')
    text=text.as_matrix()
    row=len(text)
    x=[]
    for i in range(18):
        x.append([])
    for r in range(row):
        for c in range(3,27):
            if(text[r][c]!="NR"):
                x[r%18].append(float(text[r][c]))
            else:
                x[r%18].append(0.0)
    return x

def formatX(train_x):
    #format train_x and generate training data x,y
    row=len(train_x)
    col=len(train_x[0])
    x=[]
    y=[]
    for c in range(col-9):
        x.append([1])
        for r in range(18):
            for i in range(9):
                x[c].append(train_x[r][c+i])
        y.append(train_x[9][c+9])
    x=np.array(x)
    y=np.array(y)
    return x,y

def GradientDescent(x,y):
    #save and return the weight
    x_t=x.transpose()
    s_gra=np.zeros(len(x[0]))
    w=np.zeros(len(x[0]))
    for i in range(iteration):
        
        y_=np.dot(x,w.transpose())
        loss=y_-y
        cost=np.sqrt(np.sum(loss**2)/len(x))
        gra=2*np.dot(x_t,loss)
        s_gra+=gra**2
        ada=np.sqrt(s_gra)
        w=w-l_rate*gra/ada
        print("iteration: %d | cost: %f"%(i,cost))
    return w

def readTestData(readPath):
    #return test data
    x=[]
    text=pd.read_csv(readPath,header=None,encoding='Big5')
    text=text.as_matrix()
    row=len(text)
    for r in range(row):
        if(r%18==0):
            x.append([1])
            for c in range(2,11):
                index=r//18
                x[index].append(float(text[r][c]))
        else:
            for c in range(2,11):
                if(text[r][c]!="NR"):
                    x[index].append(float(text[r][c]))
                else:
                    x[index].append(0.0)
    return x

def predict(w,test_x):
    #predict y
    y_predict=np.dot(test_x,w)
    for i,y in enumerate(y_predict):
        if y_predict[i]<0:
            y_predict[i]=int(0)
        elif (y_predict[i]-floor(y))>0.5:
            y_predict[i]=ceil(y)
        else:
            y_predict[i]=floor(y)
    return y_predict

def writeCSV(y_,writePath):
    #save predict_y to csv
    row=len(y_)
    text=open(writePath,"w+")
    s=csv.writer(text,delimiter=',',lineterminator='\n')
    s.writerow(["id","value"])
    for r in range(row):
        s.writerow(["id_"+str(r),+y_[r]])
    text.close()

if __name__ == "__main__":
    iteration=10000
    l_rate=10
    train_x=readCSV()
    x,y=formatX(train_x)
    w=GradientDescent(x,y)
    test_x=readTestData(sys.argv[1])
    y_predict=predict(w,test_x)
    writeCSV(y_predict,sys.argv[2])




