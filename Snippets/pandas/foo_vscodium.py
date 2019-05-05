#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Snippets/pandas'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd

s = pd.Series([3, -5, 7 ,4], index=['a', 'b', 'c', 'd'])

data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasília'],
    'Population': [11190846, 1303171035, 207847528]
    }

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])


#%%
s


#%%
df


#%%



