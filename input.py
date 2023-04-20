'''


Refrence 

EST_COST_RANGE          object
MODEOFTENDER            object
METHOD_OF_PURCHASE      object
FINANCIAL_POWER_CODE    object
CFA_CODE                object
CONCURRENCE_BY          object
BUDGET_HEAD_CODE        object
IS_PAC                    bool
TOTAL_DAYS_RANGES       object
dtype: object




95 colums as input to the model

['IS_PAC', 'EST_COST_RANGE_0 - 10L', 'EST_COST_RANGE_10L - 25L',
       'EST_COST_RANGE_1CR - 5CR', 'EST_COST_RANGE_25L - 50L',
       'EST_COST_RANGE_50L - 1CR', 'EST_COST_RANGE_5CR - 10CR',
       'EST_COST_RANGE_> 10CR', 'MODEOFTENDER_CAPSI', 'MODEOFTENDER_CARS',
       'MODEOFTENDER_Factory Indents', 'MODEOFTENDER_Global',
       'MODEOFTENDER_Limited', 'MODEOFTENDER_Open',
       'MODEOFTENDER_Procurement Through GeM', 'MODEOFTENDER_Proprietary',
       'MODEOFTENDER_Rate Contracts', 'MODEOFTENDER_Repeat Order',
       'MODEOFTENDER_Repeat Order on Other Estt.', 'MODEOFTENDER_SWOD',
       'MODEOFTENDER_Single Tender', 'MODEOFTENDER_Through LPC',
       'METHOD_OF_PURCHASE_CAPSI', 'METHOD_OF_PURCHASE_CARS',
       'METHOD_OF_PURCHASE_Factory Indents', 'METHOD_OF_PURCHASE_Global',
       'METHOD_OF_PURCHASE_Limited', 'METHOD_OF_PURCHASE_Open',
       'METHOD_OF_PURCHASE_Procurement Through GeM',
       'METHOD_OF_PURCHASE_Proprietary', 'METHOD_OF_PURCHASE_Rate Contracts',
       'METHOD_OF_PURCHASE_Repeat Order',
       'METHOD_OF_PURCHASE_Repeat Order on Other Estt.',
       'METHOD_OF_PURCHASE_SWOD', 'METHOD_OF_PURCHASE_Single Tender',
       'METHOD_OF_PURCHASE_Through LPC', 'FINANCIAL_POWER_CODE_202001',
       'FINANCIAL_POWER_CODE_202002', 'FINANCIAL_POWER_CODE_202004',
       'FINANCIAL_POWER_CODE_202005', 'FINANCIAL_POWER_CODE_202008',
       'FINANCIAL_POWER_CODE_202009', 'FINANCIAL_POWER_CODE_202011',
       'FINANCIAL_POWER_CODE_202012', 'FINANCIAL_POWER_CODE_202013',
       'FINANCIAL_POWER_CODE_202014', 'FINANCIAL_POWER_CODE_202015',
       'FINANCIAL_POWER_CODE_202016', 'FINANCIAL_POWER_CODE_202017',
       'FINANCIAL_POWER_CODE_202018', 'FINANCIAL_POWER_CODE_202019',
       'FINANCIAL_POWER_CODE_202020', 'FINANCIAL_POWER_CODE_205001',
       'FINANCIAL_POWER_CODE_205002', 'FINANCIAL_POWER_CODE_205003',
       'FINANCIAL_POWER_CODE_205004', 'FINANCIAL_POWER_CODE_205008',
       'FINANCIAL_POWER_CODE_205010', 'FINANCIAL_POWER_CODE_205012',
       'FINANCIAL_POWER_CODE_205013', 'FINANCIAL_POWER_CODE_205015',
       'FINANCIAL_POWER_CODE_205016', 'FINANCIAL_POWER_CODE_205018',
       'FINANCIAL_POWER_CODE_205022', 'FINANCIAL_POWER_CODE_205024',
       'FINANCIAL_POWER_CODE_205025', 'FINANCIAL_POWER_CODE_208003',
       'FINANCIAL_POWER_CODE_208005', 'FINANCIAL_POWER_CODE_208008',
       'FINANCIAL_POWER_CODE_208023', 'FINANCIAL_POWER_CODE_208034',
       'FINANCIAL_POWER_CODE_209007', 'CFA_CODE_DGC', 'CFA_CODE_DIR',
       'CFA_CODE_PDC', 'CFA_CODE_PGD', 'CFA_CODE_PJA', 'CFA_CODE_PM1',
       'CFA_CODE_SED', 'CONCURRENCE_BY_DFA', 'CONCURRENCE_BY_DIR(Fin)',
       'CONCURRENCE_BY_DY IFA', 'CONCURRENCE_BY_IFA',
       'CONCURRENCE_BY_JS & Addl.FA', 'CONCURRENCE_BY_None',
       'BUDGET_HEAD_CODE_AF', 'BUDGET_HEAD_CODE_GC', 'BUDGET_HEAD_CODE_GN',
       'BUDGET_HEAD_CODE_MS', 'BUDGET_HEAD_CODE_NY', 'BUDGET_HEAD_CODE_PC',
       'BUDGET_HEAD_CODE_PG', 'BUDGET_HEAD_CODE_PR', 'BUDGET_HEAD_CODE_RD',
       'BUDGET_HEAD_CODE_SM', 'BUDGET_HEAD_CODE_SP']

'''




import pandas as pd
import pickle
import sys
import numpy as np
filename = '/home/koushal/beproject/Random_forest_model.sav'
filenamexgboost='/home/koushal/beproject/xgboost_model.sav'


loaded_model = pickle.load(open(filename, 'rb'))
loaded_model_xgboost=pickle.load(open(filenamexgboost,'rb'))

# input_cols = ["EST_COST_RANGE", "MODEOFTENDER", "METHOD_OF_PURCHASE", "FINANCIAL_POWER_CODE", "CFA_CODE", "CONCURRENCE_BY", "BUDGET_HEAD_CODE", "IS_PAC"]
input_cols = ['SUPPLY_ORDER_NO', 'TOTAL_COST', 'MODE_OF_TENDER_CODE', 'MODEOFTENDER',
       'PROCUREMENT_MODE_CODE', 'PROCUREMENT_MODE_DESC', 'DEMAND_NO', 'RFP_NO',
       'FINANCIAL_POWER_CODE', 'FINANCIAL_POWER_SERIAL_NO', 'CFA_CODE',
       'CONCURRENCE_LEVEL_CODE', 'UO_NO', 'GEM_CONTRACT_NO',
       'BUDGET_HEAD_CODE', 'AGAINST_SANCTION_NO', 'MAJOR_HEAD', 'MINOR_HEAD',
       'HEAD_CODE', 'UNITCODE', 'UNITCODE_DESCRIPTION', 'DIVISION_NO',
       'DIVISION_NAME', 'FIN_POWER_DEMAND_FS', 'IS_PAC', 'CONCURRENCE_BY',
       'CFA', 'TOTAL_DAYS_RANGES']

output_value=["TOTAL_DAYS_RANGES"]

input_val=sys.argv[1]
input_val = input_val.split(",")
# print("input",input_val)
cost=int(input_val[0])
# print("cost :",cost)

cost_ranges = [(0, 1000000), (1000001, 2500000), (2500001, 5000000), (5000001, 10000000), (10000001, 50000000), (50000001, 100000000)]
cost_ranges_endcoding = ['0 - 10L', '10L - 25L', '25L - 50L', '50L - 1CR', '1CR - 5CR', '5CR - 10CR', '> 10CR']

EST_COST_RANGE='> 10CR'

for i in range(len(cost_ranges_endcoding) - 1):
    if cost_ranges[i][0] <= cost <= cost_ranges[i][1]:
        EST_COST_RANGE=cost_ranges_endcoding[i]
        break
   

if(input_val[7]=='True'):
    input_val[7]=True
else:
    input_val[7]=False

input_val_2=[]
input_val_2.append(EST_COST_RANGE)
for i in range(1,len(input_val)):
    input_val_2.append(input_val[i])


# df = pd.DataFrame({
#         "EST_COST_RANGE": [input_val_2[0]],
#         "MODEOFTENDER": [input_val_2[1]],
#         "METHOD_OF_PURCHASE": [input_val_2[2]],
#         "FINANCIAL_POWER_CODE": [input_val_2[3]],
#         "CFA_CODE": [input_val_2[4]],
#         "CONCURRENCE_BY": [input_val_2[5]],
#         "BUDGET_HEAD_CODE": [input_val_2[6]],
#         "IS_PAC": bool([input_val_2[7]]),

#     })
df = pd.DataFrame({
        'SUPPLY_ORDER_NO': [input_val_2[0]], 'TOTAL_COST': [input_val_2[1]], 'MODE_OF_TENDER_CODE': [input_val_2[2]], 'MODEOFTENDER': [input_val_2[3]],
       'PROCUREMENT_MODE_CODE': [input_val_2[4]], 'PROCUREMENT_MODE_DESC': [input_val_2[5]], 'DEMAND_NO': [input_val_2[6]], 'RFP_NO': [input_val_2[7]],
       'FINANCIAL_POWER_CODE': [input_val_2[8]], 'FINANCIAL_POWER_SERIAL_NO': [input_val_2[9]], 'CFA_CODE': [input_val_2[10]],
       'CONCURRENCE_LEVEL_CODE': [input_val_2[11]], 'UO_NO': [input_val_2[12]], 'GEM_CONTRACT_NO': [input_val_2[13]],
       'BUDGET_HEAD_CODE': [input_val_2[14]], 'AGAINST_SANCTION_NO': [input_val_2[15]], 'MAJOR_HEAD': [input_val_2[16]], 'MINOR_HEAD': [input_val_2[17]],
       'HEAD_CODE': [input_val_2[18]], 'UNITCODE': [input_val_2[19]], 'UNITCODE_DESCRIPTION': [input_val_2[20]], 'DIVISION_NO': [input_val_2[21]],
       'DIVISION_NAME': [input_val_2[22]], 'FIN_POWER_DEMAND_FS': [input_val_2[23]], 'IS_PAC': [input_val_2[24]], 'CONCURRENCE_BY': [input_val_2[25]],
       'CFA': [input_val_2[26]], 'TOTAL_DAYS_RANGES': [input_val_2[27]]
    })





# model_input_cols=['IS_PAC', 'EST_COST_RANGE_0 - 10L', 'EST_COST_RANGE_10L - 25L',
#        'EST_COST_RANGE_1CR - 5CR', 'EST_COST_RANGE_25L - 50L',
#        'EST_COST_RANGE_50L - 1CR', 'EST_COST_RANGE_5CR - 10CR',
#        'EST_COST_RANGE_> 10CR', 'MODEOFTENDER_CAPSI', 'MODEOFTENDER_CARS',
#        'MODEOFTENDER_Factory Indents', 'MODEOFTENDER_Global',
#        'MODEOFTENDER_Limited', 'MODEOFTENDER_Open',
#        'MODEOFTENDER_Procurement Through GeM', 'MODEOFTENDER_Proprietary',
#        'MODEOFTENDER_Rate Contracts', 'MODEOFTENDER_Repeat Order',
#        'MODEOFTENDER_Repeat Order on Other Estt.', 'MODEOFTENDER_SWOD',
#        'MODEOFTENDER_Single Tender', 'MODEOFTENDER_Through LPC',
#        'METHOD_OF_PURCHASE_CAPSI', 'METHOD_OF_PURCHASE_CARS',
#        'METHOD_OF_PURCHASE_Factory Indents', 'METHOD_OF_PURCHASE_Global',
#        'METHOD_OF_PURCHASE_Limited', 'METHOD_OF_PURCHASE_Open',
#        'METHOD_OF_PURCHASE_Procurement Through GeM',
#        'METHOD_OF_PURCHASE_Proprietary', 'METHOD_OF_PURCHASE_Rate Contracts',
#        'METHOD_OF_PURCHASE_Repeat Order',
#        'METHOD_OF_PURCHASE_Repeat Order on Other Estt.',
#        'METHOD_OF_PURCHASE_SWOD', 'METHOD_OF_PURCHASE_Single Tender',
#        'METHOD_OF_PURCHASE_Through LPC', 'FINANCIAL_POWER_CODE_202001',
#        'FINANCIAL_POWER_CODE_202002', 'FINANCIAL_POWER_CODE_202004',
#        'FINANCIAL_POWER_CODE_202005', 'FINANCIAL_POWER_CODE_202008',
#        'FINANCIAL_POWER_CODE_202009', 'FINANCIAL_POWER_CODE_202011',
#        'FINANCIAL_POWER_CODE_202012', 'FINANCIAL_POWER_CODE_202013',
#        'FINANCIAL_POWER_CODE_202014', 'FINANCIAL_POWER_CODE_202015',
#        'FINANCIAL_POWER_CODE_202016', 'FINANCIAL_POWER_CODE_202017',
#        'FINANCIAL_POWER_CODE_202018', 'FINANCIAL_POWER_CODE_202019',
#        'FINANCIAL_POWER_CODE_202020', 'FINANCIAL_POWER_CODE_205001',
#        'FINANCIAL_POWER_CODE_205002', 'FINANCIAL_POWER_CODE_205003',
#        'FINANCIAL_POWER_CODE_205004', 'FINANCIAL_POWER_CODE_205008',
#        'FINANCIAL_POWER_CODE_205010', 'FINANCIAL_POWER_CODE_205012',
#        'FINANCIAL_POWER_CODE_205013', 'FINANCIAL_POWER_CODE_205015',
#        'FINANCIAL_POWER_CODE_205016', 'FINANCIAL_POWER_CODE_205018',
#        'FINANCIAL_POWER_CODE_205022', 'FINANCIAL_POWER_CODE_205024',
#        'FINANCIAL_POWER_CODE_205025', 'FINANCIAL_POWER_CODE_208003',
#        'FINANCIAL_POWER_CODE_208005', 'FINANCIAL_POWER_CODE_208008',
#        'FINANCIAL_POWER_CODE_208023', 'FINANCIAL_POWER_CODE_208034',
#        'FINANCIAL_POWER_CODE_209007', 'CFA_CODE_DGC', 'CFA_CODE_DIR',
#        'CFA_CODE_PDC', 'CFA_CODE_PGD', 'CFA_CODE_PJA', 'CFA_CODE_PM1',
#        'CFA_CODE_SED', 'CONCURRENCE_BY_DFA', 'CONCURRENCE_BY_DIR(Fin)',
#        'CONCURRENCE_BY_DY IFA', 'CONCURRENCE_BY_IFA',
#        'CONCURRENCE_BY_JS & Addl.FA', 'CONCURRENCE_BY_None',
#        'BUDGET_HEAD_CODE_AF', 'BUDGET_HEAD_CODE_GC', 'BUDGET_HEAD_CODE_GN',
#        'BUDGET_HEAD_CODE_MS', 'BUDGET_HEAD_CODE_NY', 'BUDGET_HEAD_CODE_PC',
#        'BUDGET_HEAD_CODE_PG', 'BUDGET_HEAD_CODE_PR', 'BUDGET_HEAD_CODE_RD',
#        'BUDGET_HEAD_CODE_SM', 'BUDGET_HEAD_CODE_SP']

convert_dict = {}
convert_dict['IS_PAC']= bool

# for i in model_input_cols:
#     if(i=='IS_PAC'):
#         continue
#     convert_dict[i]=np.uint8

for i in input_cols:
    if (i == 'IS_PAC'):
        continue
    elif (i == 'FINANCIAL_POWER_CODE'):
        convert_dict[i]=np.uint8
    else:  
        convert_dict[i]=np.float



# x=pd.DataFrame(columns=model_input_cols)
x=pd.DataFrame(columns=input_cols)


# df_x = pd.get_dummies(df)

# for i in model_input_cols:
#     if(i == 'IS_PAC'):
#         continue

#     if(i in df_x ):
#         # print("in ", i)
#         x.at[0,i]=np.uint8(1)
#     else:
#         x.at[0,i]=np.uint8(0)


# x = x.astype(convert_dict) 
# x.at[0,'IS_PAC']=input_val_2[7]  
# print(x.dtypes)




output=loaded_model.predict(x)
output_xgboost=loaded_model_xgboost.predict(x)

days_ranges=['0 - 60', '60 - 90', '90 - 120', '120 - 150', '150 - 180', '> 180']

print("output : ", days_ranges[output[0]])
print("output xgboost : " ,days_ranges[output_xgboost[0]])
