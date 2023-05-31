import numpy as np
import pandas as pd
import sys

input_val = sys.argv[1].split(",")

# print(input_val)

filepath = '/Users/siddharth/Desktop/procurement_timeframe/dataset.xlsx'
df = pd.read_excel(filepath, sheet_name='Sheet1')

save_df=df.tail(1)

TOTAL_COST = int(input_val[0])
MODE_OF_TENDER_CODE = input_val[1]
FINANCIAL_POWER_CODE = int(input_val[2])
FINANCIAL_POWER_SERIAL_NO = float(input_val[3])
CFA_CODE = input_val[4]
# UO_NO = input_val[4]
GEM_CONTRACT_NO = input_val[5]
BUDGET_HEAD_CODE = input_val[6]
BUDGET_HEAD_DESCRIPTION = " ".join(input_val[7].split("_"))
# AGAINST_SANCTION_NO = input_val[8]
MINOR_HEAD = int(input_val[8])
UNITCODE = int(input_val[9])
ESTIMATED_COST = int(input_val[10])
DIVISION_NO = input_val[11]
FIN_POWER = float(input_val[12])
FIN_POWER_DEMAND_FS = float(input_val[13])
BUDGET_HEAD_DESCRIPTION_1 = " ".join(input_val[14].split("_"))
# CONCURRENCE_BY = input_val[16]
APPROVAL_AMOUNT = int(input_val[15])
SUPPLY_ORDER_DATE = input_val[16]

cols = {'TOTAL_COST': [TOTAL_COST], 
        'MODE_OF_TENDER_CODE': [MODE_OF_TENDER_CODE], 
        'FINANCIAL_POWER_CODE': [FINANCIAL_POWER_CODE], 
        'FINANCIAL_POWER_SERIAL_NO': [FINANCIAL_POWER_SERIAL_NO], 
        'CFA_CODE': [CFA_CODE], 
        # 'UO_NO': [UO_NO], 
        'GEM_CONTRACT_NO': [GEM_CONTRACT_NO], 
        'BUDGET_HEAD_CODE': [BUDGET_HEAD_CODE], 
        'BUDGET_HEAD_DESCRIPTION': [BUDGET_HEAD_DESCRIPTION], 
        # 'AGAINST_SANCTION_NO': [AGAINST_SANCTION_NO], 
        'MINOR_HEAD': [MINOR_HEAD], 
        'UNITCODE': [UNITCODE], 
        'ESTIMATED_COST': [ESTIMATED_COST], 
        'DIVISION_NO': [DIVISION_NO], 
        'FIN_POWER': [FIN_POWER], 
        'FIN_POWER_DEMAND_FS': [FIN_POWER_DEMAND_FS], 
        'BUDGET_HEAD_DESCRIPTION_1': [BUDGET_HEAD_DESCRIPTION_1], 
        # 'CONCURRENCE_BY': [CONCURRENCE_BY], 
        'APPROVAL_AMOUNT': [APPROVAL_AMOUNT], 
        'SUPPLY_ORDER_DATE': [SUPPLY_ORDER_DATE]}

for col in cols:
  save_df[col]=cols[col]

df=df.append(save_df,True)
# df = pd.concat([df, save_df], ignore_index=True)

df['SUPPLY_ORDER_DATE']=pd.to_datetime(df['SUPPLY_ORDER_DATE'])
df["SUPPLY_ORDER_DATE_Year"] = df["SUPPLY_ORDER_DATE"].dt.year
df["SUPPLY_ORDER_DATE_Month"] = df["SUPPLY_ORDER_DATE"].dt.month
df["SUPPLY_ORDER_DATE_Day"] = df["SUPPLY_ORDER_DATE"].dt.day
df['SUPPLY_ORDER_DATE_Time']=df['SUPPLY_ORDER_DATE'].dt.time

df['SANCTION_DATE']=pd.to_datetime(df['SANCTION_DATE'])
df["SANCTION_DATE_Year"] = df["SANCTION_DATE"].dt.year
df["SANCTION_DATE_Month"] = df["SANCTION_DATE"].dt.month
df["SANCTION_DATE_Day"] = df["SANCTION_DATE"].dt.day
df['SANCTION_DATE_Time']=df['SANCTION_DATE'].dt.time

df['CONCURRENCE_DATE']=pd.to_datetime(df['CONCURRENCE_DATE'])
df["CONCURRENCE_DATE_Year"] = df["CONCURRENCE_DATE"].dt.year
df["CONCURRENCE_DATE_Month"] = df["CONCURRENCE_DATE"].dt.month
df["CONCURRENCE_DATE_Day"] = df["CONCURRENCE_DATE"].dt.day
df['CONCURRENCE_DATE_Time']=df['CONCURRENCE_DATE'].dt.time

df['DEMAND_DATE']=pd.to_datetime(df['DEMAND_DATE'])
df["DEMAND_DATE_Year"] = df["DEMAND_DATE"].dt.year
df["DEMAND_DATE_Month"] = df["DEMAND_DATE"].dt.month
df["DEMAND_DATE_Day"] = df["DEMAND_DATE"].dt.day
df['DEMAND_DATE_Time']=df['DEMAND_DATE'].dt.time

df['CONCURRENCE_DATE']=pd.to_datetime(df['CONCURRENCE_DATE'])
df["CONCURRENCE_DATE_Year"] = df["CONCURRENCE_DATE"].dt.year
df["CONCURRENCE_DATE_Month"] = df["CONCURRENCE_DATE"].dt.month
df["CONCURRENCE_DATE_Day"] = df["CONCURRENCE_DATE"].dt.day
df['CONCURRENCE_DATE_Time']=df['CONCURRENCE_DATE'].dt.time

df['CFA_APPROVAL_DATE']=pd.to_datetime(df['CFA_APPROVAL_DATE'])
df["CFA_APPROVAL_DATE_Year"] = df["CFA_APPROVAL_DATE"].dt.year
df["CFA_APPROVAL_DATE_Month"] = df["CFA_APPROVAL_DATE"].dt.month
df["CFA_APPROVAL_DATE_Day"] = df["CFA_APPROVAL_DATE"].dt.day
df['CFA_APPROVAL_DATE_Time']=df['CFA_APPROVAL_DATE'].dt.time

date_cols = ['SUPPLY_ORDER_DATE','DEMAND_DATE']
for col in date_cols:
  df[col] = pd.to_datetime(df[col])

df['TOTAL_DAYS'] = (df['SUPPLY_ORDER_DATE'] - df['DEMAND_DATE']).dt.days
# df['TOTAL_DAYS']

date_cols = ['SUPPLY_ORDER_DATE', 'SANCTION_DATE', 'CONCURRENCE_DATE', 'GEM_CONTRACT_DATE', 'DEMAND_DATE', 'CONCURRENCE_DATE_1', 'CFA_APPROVAL_DATE']

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

label_encoder = LabelEncoder()
df.iloc[:,0] = label_encoder.fit_transform(df.iloc[:,0]).astype('float64')


object_cols=['SUPPLY_ORDER_NO',
 'MODE_OF_TENDER_CODE',
 'MODEOFTENDER',
 'PROCUREMENT_MODE_CODE',
 'PROCUREMENT_MODE_DESC',
 'DEMAND_NO',
 'RFP_NO',
 'FINANCIAL_POWER_SERIAL_NO',
 'CFA_CODE',
 'CFA_DESCRIPTION',
 'CONCURRENCE_LEVEL_CODE',
 'CONCURRED_BY',
 'UO_NO',
 'GEM_CONTRACT_NO',
 'BUDGET_HEAD_CODE',
 'BUDGET_HEAD_DESCRIPTION',
 'AGAINST_SANCTION_NO',
 'MAJOR_HEAD',
 'MINOR_HEAD',
 'HEAD_CODE',
 'UNITCODE',
 'UNITCODE_DESCRIPTION',
 'DEMAND_NO_1',
 'DIVISION_NO',
 'DIVISION_NAME',
 'FIN_POWER',
 'FIN_POWER_DEMAND_FS',
 'METHOD_OF_PURCHASE',
 'BUDGET_HEAD_DESCRIPTION_1',
 'PROCUREMENT_MODE_DESC_1',
 'IS_PAC',
 'CONCURRENCE_BY',
 'CFA',

 'CFA_APPROVAL_REFERENCE']

label_encoder = LabelEncoder()
for i in object_cols:
  df[i]=df[i].astype(str)

  df[i] = label_encoder.fit_transform(df[i]).astype('float64')

df.drop(columns=["SANCTION_DATE_Year",            
"SANCTION_DATE_Month",           
"SANCTION_DATE_Day" ,            
"CONCURRENCE_DATE_Year" ,       
"CONCURRENCE_DATE_Month" ,      
"CONCURRENCE_DATE_Day" ],inplace=True)

null_cols=['SUB_MAJOR_HEAD','RECEIPT_DETAILS','CONCURRENCE_AMOUNT']
for i in null_cols:
  df.drop(i, axis='columns',inplace=True)

df1=df[['SUPPLY_ORDER_NO', 'TOTAL_COST', 'MODE_OF_TENDER_CODE', 'MODEOFTENDER',
       'PROCUREMENT_MODE_CODE', 'PROCUREMENT_MODE_DESC', 'DEMAND_NO', 'RFP_NO',
       'FINANCIAL_POWER_CODE', 'FINANCIAL_POWER_SERIAL_NO', 'CFA_CODE',
       'CFA_DESCRIPTION', 'CONCURRENCE_LEVEL_CODE', 'CONCURRED_BY', 'UO_NO',
       'GEM_CONTRACT_NO', 'BUDGET_HEAD_CODE', 'BUDGET_HEAD_DESCRIPTION',
       'AGAINST_SANCTION_NO', 'MAJOR_HEAD', 'MINOR_HEAD', 'HEAD_CODE',
       'UNITCODE', 'UNITCODE_DESCRIPTION', 'DEMAND_NO_1', 'ESTIMATED_COST',
       'DIVISION_NO', 'DIVISION_NAME', 'FIN_POWER', 'FIN_POWER_DEMAND_FS',
       'METHOD_OF_PURCHASE', 'BUDGET_HEAD_DESCRIPTION_1',
       'PROCUREMENT_MODE_DESC_1', 'IS_PAC', 'CONCURRENCE_BY', 'CFA',
       'CFA_APPROVAL_REFERENCE', 'APPROVAL_AMOUNT', 'SUPPLY_ORDER_DATE_Year',
       'SUPPLY_ORDER_DATE_Month', 'SUPPLY_ORDER_DATE_Day', 'DEMAND_DATE_Year',
       'DEMAND_DATE_Month', 'DEMAND_DATE_Day', 'CFA_APPROVAL_DATE_Year',
       'CFA_APPROVAL_DATE_Month', 'CFA_APPROVAL_DATE_Day', 'TOTAL_DAYS']]

selected_columns = ['SUPPLY_ORDER_NO', 'TOTAL_COST', 'MODE_OF_TENDER_CODE', 'MODEOFTENDER',
       'PROCUREMENT_MODE_DESC', 'FINANCIAL_POWER_CODE',
       'FINANCIAL_POWER_SERIAL_NO', 'CFA_CODE', 'CFA_DESCRIPTION',
       'CONCURRENCE_LEVEL_CODE', 'CONCURRED_BY', 'UO_NO', 'GEM_CONTRACT_NO',
       'BUDGET_HEAD_CODE', 'BUDGET_HEAD_DESCRIPTION', 'AGAINST_SANCTION_NO',
       'MAJOR_HEAD', 'MINOR_HEAD', 'HEAD_CODE', 'UNITCODE',
       'UNITCODE_DESCRIPTION', 'ESTIMATED_COST', 'DIVISION_NO',
       'DIVISION_NAME', 'FIN_POWER', 'FIN_POWER_DEMAND_FS',
       'METHOD_OF_PURCHASE', 'BUDGET_HEAD_DESCRIPTION_1',
       'PROCUREMENT_MODE_DESC_1', 'IS_PAC', 'CONCURRENCE_BY', 'CFA',
       'APPROVAL_AMOUNT', 'SUPPLY_ORDER_DATE_Year', 'SUPPLY_ORDER_DATE_Month',
       'SUPPLY_ORDER_DATE_Day', 'DEMAND_DATE_Month', 'DEMAND_DATE_Day',
       'CFA_APPROVAL_DATE_Year', 'CFA_APPROVAL_DATE_Month',
       'CFA_APPROVAL_DATE_Day']

data = df1[selected_columns]
data["TOTAL_DAYS"]=df1["TOTAL_DAYS"]


selected_columns = ['SUPPLY_ORDER_NO', 'TOTAL_COST', 'MODE_OF_TENDER_CODE', 'MODEOFTENDER',
       'PROCUREMENT_MODE_DESC', 'FINANCIAL_POWER_CODE',
       'FINANCIAL_POWER_SERIAL_NO', 'CFA_CODE', 'CFA_DESCRIPTION',
       'CONCURRENCE_LEVEL_CODE', 'CONCURRED_BY', 'UO_NO', 'GEM_CONTRACT_NO',
       'BUDGET_HEAD_CODE', 'BUDGET_HEAD_DESCRIPTION', 'AGAINST_SANCTION_NO',
       'MAJOR_HEAD', 'MINOR_HEAD', 'HEAD_CODE', 'UNITCODE',
       'UNITCODE_DESCRIPTION', 'ESTIMATED_COST', 'DIVISION_NO',
       'DIVISION_NAME', 'FIN_POWER', 'FIN_POWER_DEMAND_FS',
       'METHOD_OF_PURCHASE', 'BUDGET_HEAD_DESCRIPTION_1',
       'PROCUREMENT_MODE_DESC_1', 'IS_PAC', 'CONCURRENCE_BY', 'CFA',
       'APPROVAL_AMOUNT', 'SUPPLY_ORDER_DATE_Year', 'SUPPLY_ORDER_DATE_Month',
       'SUPPLY_ORDER_DATE_Day', 'DEMAND_DATE_Month', 'DEMAND_DATE_Day',
       'CFA_APPROVAL_DATE_Year', 'CFA_APPROVAL_DATE_Month',
       'CFA_APPROVAL_DATE_Day']

import statsmodels.api as sm
def backwardElimination(x, Y, sl, columns):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(Y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
                    columns = np.delete(columns, j)
                    
    regressor_OLS.summary()
    return x, columns

SL = 0.05
data_modeled, selected_columns = backwardElimination(data.iloc[:,1:].values, data.iloc[:,0].values, SL, selected_columns)

# result = pd.DataFrame()
result = pd.DataFrame(data = data_modeled, columns = selected_columns)
result['TOTAL_DAYS']=data['TOTAL_DAYS']

data=result
def range_encoding(df, source_col_name, dest_col_name, ranges, encoding):
  ranges_result = []
  for val in df[source_col_name]:
    flag = False
    for i in range(len(encoding) - 1):
      if ranges[i][0] <= val <= ranges[i][1]:
        ranges_result.append(encoding[i])
        # ranges_result = pd.concat([ranges_result, encoding[i]])
        flag = True
        break
    if not flag:
      ranges_result.append(encoding[len(encoding) - 1])
    #   ranges_result = pd.concat([ranges_result, encoding[len(encoding) - 1]])

  df[dest_col_name] = ranges_result
  return df

day_ranges = [(0, 60), (61, 90), (91, 120), (121, 150), (151, 180)]
day_ranges_encoding = ['0 - 60', '60 - 90', '90 - 120', '120 - 150', '150 - 180', '> 180']

data = range_encoding(data, 'TOTAL_DAYS', 'TOTAL_DAYS_RANGES', day_ranges, day_ranges_encoding)

data.drop('TOTAL_DAYS',axis=1, inplace=True)
to_predict=data.tail(1)

final_to_predict = to_predict[['TOTAL_COST', 'MODE_OF_TENDER_CODE', 'FINANCIAL_POWER_CODE',
       'FINANCIAL_POWER_SERIAL_NO', 'CFA_CODE', 'UO_NO', 'GEM_CONTRACT_NO',
       'BUDGET_HEAD_CODE', 'BUDGET_HEAD_DESCRIPTION', 'AGAINST_SANCTION_NO',
       'MINOR_HEAD', 'UNITCODE', 'ESTIMATED_COST', 'DIVISION_NO', 'FIN_POWER',
       'FIN_POWER_DEMAND_FS', 'BUDGET_HEAD_DESCRIPTION_1', 'CONCURRENCE_BY',
       'APPROVAL_AMOUNT', 'SUPPLY_ORDER_DATE_Year', 'SUPPLY_ORDER_DATE_Day']].copy()

# print(final_to_predict.shape)

# to_predict=to_predict.drop(columns=['TOTAL_DAYS_RANGES'])

# import pickle
# loaded_model = pickle.load(open('final_model.sav', 'rb'))
# output=loaded_model.predict(to_predict)

# answer=["0-60","120-150","150-180","60-90","90-120",">180"]
# # output
# answer[output.item()]

import pickle
loaded_model = pickle.load(open('final_model.sav', 'rb'))
output=loaded_model.predict(final_to_predict)

answer=["0-60","120-150","150-180","60-90","90-120",">180"]
# output
print(answer[output.item()])