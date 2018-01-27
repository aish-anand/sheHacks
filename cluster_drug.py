from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
import csv
import sys
from sklearn.model_selection import train_test_split
X=[]
Y=[]
X_test=[]
Y_test=[]
#df = pd.read_csv("/media/d/9485fdcc-4df8-4558-a82b-390eaf04ac40/d/DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv")
with open('/media/d/9485fdcc-4df8-4558-a82b-390eaf04ac40/d/ben_drug_claims.csv', 'r') as csvfile:
     reader = csv.reader(csvfile)
     i=0
     min=float(sys.maxsize)
     max=-min
     for row in reader:
         if(i==0):
            print(row)
            i=1
            continue
        
         X.append([float(row[13]),float(row[14]),float(row[15]),float(row[16])])
         if(float(row[19])<min):
                    min=float(row[18])
         if(float(row[18])>max):
                    max=float(row[18])
         Y.append(float(row[18]))
         i+=1
         if(i>10000):
            break
         #except:
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=40)
neigh = KNeighborsClassifier(n_neighbors=10)
neigh.fit(X_train, Y_train) 

p=neigh.predict(X_test)
s=[(x==y) for (x,y) in zip(p,Y_test)]
sum=0
for i in s:
    if (i):
        sum+=1
print(sum/len(p))
