import pandas as pd
import sys
file_path = sys.argv[1]
df =pd.read_csv(file_path)
df.to_csv('data_raw.csv', index=False) 
print("finished ingesting datajust checking if its working")