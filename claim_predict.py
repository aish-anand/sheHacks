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
         
         X.append([float(row[-6]),float(row[-5]),float(row[-3]),float(row[-7])])
         if(float(row[-2])<min):
                    min=float(row[-2])
         if(float(row[-2])>max):
                    max=float(row[-2])
                    
         Y.append(float(row[-2]))
         i+=1
         
print(X[:10])
print(len(X),len(Y))
print('maxmin',max,min)

regr = linear_model.LinearRegression(normalize=True,fit_intercept=True)
 
# Train the model using the training sets
regr.fit(X[:-500], Y[:-500])
 
# Plot outputs
#plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
p=regr.predict(X[-500:])

print(sum(abs(Y[-500:]-p))/len(p))
#Max 63000.0 Min 0 MAE=1043.334
'''
['', 'DESYNPUF_ID', 'BENE_BIRTH_DT', 'BENE_DEATH_DT', 'BENE_SEX_IDENT_CD', 'BENE_RACE_CD', 'BENE_ESRD_IND', 'SP_STATE_CODE', 'BENE_COUNTY_CD', 'BENE_HI_CVRAGE_TOT_MONS', 'BENE_SMI_CVRAGE_TOT_MONS', 'BENE_HMO_CVRAGE_TOT_MONS', 'PLAN_CVRG_MOS_NUM', 'SP_ALZHDMTA', 'SP_CHF', 'SP_CHRNKIDN', 'SP_CNCR', 'SP_COPD', 'SP_DEPRESSN', 'SP_DIABETES', 'SP_ISCHMCHT', 'SP_OSTEOPRS', 'SP_RA_OA', 'SP_STRKETIA', 'MEDREIMB_IP', 'BENRES_IP', 'PPPYMT_IP', 'MEDREIMB_OP', 'BENRES_OP', 'PPPYMT_OP', 'MEDREIMB_CAR', 'BENRES_CAR', 'PPPYMT_CAR', 'PDE_ID', 'SRVC_DT', 'PROD_SRVC_ID', 'QTY_DSPNSD_NUM', 'DAYS_SUPLY_NUM', 'PTNT_PAY_AMT', 'TOT_RX_CST_AMT', 'NCH_BENE_DSCHRG_DT', 'SUM_CLM_AMT', 'year']
Predicted:
[ 9146.59987089] 
Test vals:
Male, with Heart failure, renal failure, diabetes, alzheimers, osteoporasis, with drug 490713828, in the year 2009, has predicted $9146 when he actually spent $8000.
8000.0 ['873815', 'FFE7C75AE1426A4D', '19400901', '', '1', '1', '0', '33', '320', '12', '12', '12', '12', '1', '1', '2', '2', '2', '1', '1', '1', '1', '2', '2', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '2660.0', '580.0', '0.0', '233734490227038', '20080215', '490713828', '0.0', '30', '0.0', '400.0', '20090726', '8000.0', '2009']
'''

