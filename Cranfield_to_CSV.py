import scipy.io
import pandas as pd
path = "C:\\Users\\esbe1\\Desktop\\Portfolio\\Server\\Cranfield\\Training.mat"
path_ex = "C:\\Users\\esbe1\\Desktop\\Portfolio\\Server\\Cranfield\\"

mat = scipy.io.loadmat(path)
#%%

T1 = pd.DataFrame(mat['T1'])
T2 = pd.DataFrame(mat['T2'])
T3 = pd.DataFrame(mat['T3'])

T1.to_csv(path_ex+'T1.csv')
T2.to_csv(path_ex+'T2.csv')
T3.to_csv(path_ex+'T3.csv')

#%%
explain = {
'Variable nr': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],

'Location': ['PT312', 'PT401', 'PT408', 'PT403', 'PT501', 'PT408', 'PT403', 'FT305', 'FT104', 'FT407', 'LI405', 'FT406', 
'FT407', 'FT406', 'FT104', 'FT407', 'FT406', 'FT104', 'LI504', 'VC501', 'VC302', 'VC101', 'PO1', 'PT417'],

'Measured magnitude': ['Air delivery pressure', 'Pressure in the bottom of the riser', 
'Pressure in top of the riser', 'Pressure in top separator', 
'Pressure in 3 phase separator', 'Diff. pressure (PT401-PT408)', 
'Differential pressure over VC404', 'Flow rate input air',  
'Flow rate input water', 'Flow rate top riser', 
'Level top separator', 'Flow rate top separator output', 
'Density top riser', 'Density top separator output', 
'Density water input', 'Temperature top riser', 
'Temperature top separator output', 'Temperature water input', 
'Level gas-liquid 3 phase separator', 'Position of valve VC501',
'Position of valve VC302','Position of valve VC101',
'Water pump current', 'Pressure in mixture zone 2” line'],

'Unit': ['MPa', 'MPa', 'MPa', 'MPa', 'MPa', 'MPa', 'MPa', 'Sm3/s', 'kg/s', 'kg/s', 'm', 'kg/s', 
'kg/m3', 'kg/m3', 'kg/m3', 'degC', 'degC', 'degC', '%', '%', '%', '%', 'A', 'MPa',],
}

explain = pd.DataFrame(explain)

explain.to_csv(path_ex+'explain.csv')
