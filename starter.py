# import numpy as np
# import pandas as pd
# drug_df = pd.read_csv('DE1_0_2008_to_2010_Prescription_Drug_Events_Sample_1.csv')
# ben_df_08 = pd.read_csv('DE1_0_2008_Beneficiary_Summary_File_Sample_1.csv')
# ben_df_09 = pd.read_csv('DE1_0_2009_Beneficiary_Summary_File_Sample_1.csv')
# ben_df_10 = pd.read_csv('DE1_0_2010_Beneficiary_Summary_File_Sample_1.csv')
# in_claims_df = pd.read_csv('DE1_0_2008_to_2010_Inpatient_Claims_Sample_1.csv')
# out_claims_df = pd.read_csv('DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv')
# ben_df = ben_df_08.append(ben_df_09)
# ben_df = ben_df.append(ben_df_10)
# print(ben_df_08.shape)
# print(ben_df_09.shape)
# print(ben_df_10.shape)
# print(ben_df.shape)
# top_drug_df =drug_df.groupby(['PROD_SRVC_ID']).size().reset_index(name = 'count').sort_values(by = 'count',ascending = False).head(100)
# selected_ids_df = pd.merge(left = drug_df, right = top_drug_df, how = 'inner', left_on = 'PROD_SRVC_ID', right_on = 'PROD_SRVC_ID')
# print(selected_ids_df.shape)
# print(selected_ids_df.head(10))
# print(len(selected_ids_df.DESYNPUF_ID.unique()))
# selected_ben = selected_ids_df.DESYNPUF_ID.unique()
# ben_df.columns
# print(ben_df_08[ben_df_08['DESYNPUF_ID'].isin(selected_ben)].shape)
# print(ben_df_09[ben_df_09['DESYNPUF_ID'].isin(selected_ben)].shape)
# print(ben_df_10[ben_df_10['DESYNPUF_ID'].isin(selected_ben)].shape)
# summary_in_claims = in_claims_df[in_claims_df[u'DESYNPUF_ID'].isin(selected_ben)].groupby(by = [u'DESYNPUF_ID',u'NCH_BENE_DSCHRG_DT'])['CLM_PMT_AMT'].sum().reset_index(name = 'SUM_CLM_AMT')
# summary_in_claims['year'] = summary_in_claims[u'NCH_BENE_DSCHRG_DT'].apply(lambda x: str(x)[:4])
# p = summary_in_claims.plot(x = 'DESYNPUF_ID', y = 'SUM_CLM_AMT')
# plt.show(p)

# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

drug_df = pd.read_csv('DE1_0_2008_to_2010_Prescription_Drug_Events_Sample_1.csv')
ben_df_08 = pd.read_csv('DE1_0_2008_Beneficiary_Summary_File_Sample_1.csv')
ben_df_09 = pd.read_csv('DE1_0_2009_Beneficiary_Summary_File_Sample_1.csv')
ben_df_10 = pd.read_csv('DE1_0_2010_Beneficiary_Summary_File_Sample_1.csv')
in_claims_df = pd.read_csv('DE1_0_2008_to_2010_Inpatient_Claims_Sample_1.csv')
out_claims_df = pd.read_csv('DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv')


# In[3]:

ben_df_08['YEAR'] = 2008
ben_df_09['YEAR'] = 2009
ben_df_10['YEAR'] = 2010
ben_df = ben_df_08.append(ben_df_09)
ben_df = ben_df.append(ben_df_10)


# In[4]:

print(ben_df_08.shape)
print(ben_df_09.shape)
print(ben_df_10.shape)
print(ben_df.shape)


# In[7]:

top_drug_df =drug_df.groupby(['PROD_SRVC_ID']).size().reset_index(name = 'count').sort_values(by = 'count',ascending = False).head(100)


# In[8]:

selected_ids_df = pd.merge(left = drug_df, right = top_drug_df, how = 'inner', left_on = 'PROD_SRVC_ID', right_on = 'PROD_SRVC_ID')


# In[9]:

print(selected_ids_df.shape)
print(selected_ids_df.head(10))
print(len(selected_ids_df.DESYNPUF_ID.unique()))
selected_ben = selected_ids_df.DESYNPUF_ID.unique()


# In[11]:

ben_df.columns
print(ben_df[ben_df['DESYNPUF_ID'].isin(selected_ben)].shape)
print(len(ben_df.columns))


# In[29]:

print(in_claims_df.shape)
print(in_claims_df[in_claims_df.columns[:38]].shape)


# In[33]:

in_claims_df.columns


# In[58]:

out_claims_df['CLM_FROM_DT'].unique()
out_claims_df.fillna(0, inplace = True)


# In[60]:

in_claims_df = in_claims_df[in_claims_df.columns[:36]]
in_claims_df['IN_YEAR'] = in_claims_df['CLM_ADMSN_DT'].apply(lambda x : str(x)[:4])
in_claims_df['IN_YEAR'] = in_claims_df['IN_YEAR'].astype('int64')
summary_in_claims = in_claims_df[in_claims_df[u'DESYNPUF_ID'].isin(selected_ben)]
# out_claims_df=out_claims_df[out_claims_df.columns[:28]]
# out_claims_df['OUT_YEAR'] = out_claims_df[u'CLM_FROM_DT'].apply(lambda x : str(x)[:4])
# out_claims_df['OUT_YEAR'] = out_claims_df['OUT_YEAR'].astype('int64')
# summary_out_claims = out_claims_df[out_claims_df[u'DESYNPUF_ID'].isin(selected_ben)]


# In[63]:

ben_df_1 = pd.merge(left = ben_df, right = summary_in_claims, how = 'left', left_on = ['DESYNPUF_ID','YEAR'], right_on = ['DESYNPUF_ID','IN_YEAR'])
print(ben_df_1.shape)
# ben_df_2 = pd.merge(left = ben_df_1, right = summary_out_claims, how = 'inner', left_on =['DESYNPUF_ID','YEAR'], right_on = ['DESYNPUF_ID','OUT_YEAR'])
# print(ben_df_2.shape)


# In[67]:

drug_df['D_YEAR'] = drug_df['SRVC_DT'].apply(lambda x : str(x)[:4])
drug_df['D_YEAR'] = drug_df['D_YEAR'].astype('int64')


# In[68]:

drug_df.head(10)


# In[69]:

ben_df_2 = pd.merge(left = ben_df_1, right =drug_df , how = 'left', left_on = ['DESYNPUF_ID','YEAR'], right_on = ['DESYNPUF_ID','D_YEAR'])
print(ben_df_1.shape)

