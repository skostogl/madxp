# %% Run it
import madxp; 
madxp.madxp('mask.madx', verbose=True)

# %% Read the output.pkl
import pandas as pd
myDF=pd.read_pickle('output.pkl')
myDF

# %% Make markdown
madxp.madx2md('mask.madx','mask.md')