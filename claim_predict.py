import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
import csv
import sys
# Load CSV and columns
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
        
         if(row[-1]=='2008'):
                 X.append([float(row[-6]),float(row[-5]),float(row[-4]),float(row[-7])])
                 if(float(row[-2])<min):
                    min=float(row[-2])
                 if(float(row[-2])>max):
                    max=float(row[-2])
                 Y.append(float(row[-2]))
         elif(row[-1]=='2010'):
                 X_test.append([float(row[-6]),float(row[-5]),float(row[-4]),float(row[-7])])
                 Y_test.append(float(row[-2]))
         #except:
          #  print(row)
           # pass
#print(df.columns)
#print('Xz')
#Y = df['CLM_PMT_AMT']
#X = df[['NCH_BENE_BLOOD_DDCTBL_LBLTY_AM'],'PRVDR_NUM']
#X.append(df['PRVDR_NUM'])
print(X[:10])
print(len(X),len(Y))
print('maxmin',max,min)
#X=X.reshape(len(X),1)
#Y=Y.reshape(len(Y),1)
 
# Split the data into training/testing sets
#X_train = X[:-550]
#X_test = X[:-550]
 
# Split the targets into training/testing sets
#Y_train = Y[:-550]
#Y_test = Y[:-550]
 
 
# Plot outputs
#plt.scatter(X_test, Y_test,  color='black')
#plt.title('Test Data')
#plt.xlabel('NCE_BENE')
#plt.ylabel('Price')
#plt.xticks(())
#plt.yticks(())
 
#plt.show()

regr = linear_model.LinearRegression(normalize=True,fit_intercept=True)
 
# Train the model using the training sets
regr.fit(X, Y)
 
# Plot outputs
#plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
p=regr.predict(X_test[:150])
plt.plot(p,Y_test[:150])
plt.show()
print(sum(abs(Y_test[:150]-p))/len(p))
