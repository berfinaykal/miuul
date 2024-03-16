"""1. soru"""

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
a=["NUM_"+col.upper() if df[col].dtype!="O" else col.upper() for col in df.columns]
print(a)

"""2. soru"""

df=sns.load_dataset("car_crashes")
df.columns
b=[col.upper()+"_FLAG" if not "no" in col else col.upper() for col in df.columns]
print(b)

"""3.soru"""

df=sns.load_dataset("car_crashes")
df.columns
og_list=["abbrev","no_previous"]
new_cols={col for col in og_list}
new_df=[col for col in df.columns if not col in new_cols]
print(df[new_df])
