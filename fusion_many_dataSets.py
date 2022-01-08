import pandas as pd
import chardet
import glob

from pandas.core.frame import DataFrame

# you need just the path pf your datasets 
path = r"C:\\Users\\rabi3\Desktop\\ML project\\ML Project Indeed Companies reviews\\dataSets"

all_paths = glob.glob(path + "\*.csv")
all_files = [x.split("\\")[-1] for x in all_paths]
li = []

for filename in all_files:
    try:
        df = pd.read_csv(r"C:\\Users\\rabi3\Desktop\\ML project\\ML Project Indeed Companies reviews\\dataSets\\"+filename, sep='~', header=0,  index_col=False)
        li.append(df)
    except:
        with open(r"C:\\Users\\rabi3\Desktop\\ML project\\ML Project Indeed Companies reviews\\dataSets\\"+filename, 'rb' ) as f:
            result = chardet.detect(f.read())
        df = pd.read_csv(r"C:\\Users\\rabi3\Desktop\\ML project\\ML Project Indeed Companies reviews\\dataSets\\"+filename, sep='~', header=0,  index_col=False, encoding=result['encoding'])
        li.append(df)
    

df = pd.concat(li, axis=0 , ignore_index=True)

print(type(df))
print(len(df))
print(df)
