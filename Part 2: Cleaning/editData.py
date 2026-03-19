import pandas as pd
df = pd.read_excel('info_data.xlsx', engine='openpyxl')

date = pd.to_datetime(df['DOB'], errors='coerce')
age = pd.to_numeric(df['Age'], errors='coerce')

score = ['Math', 'English', 'Physical', 'Chemistry', 'Total']
df[score] = df[score].apply(pd.to_numeric, errors='coerce')
wrongscore = df[(df[score] < 0).any(axis=1) | (df[score] > 10).any(axis=1)]

dataiswrong = df[(date.isna()) | (age <= 0) | (age >= 100)] # | (df[score].lt(0).any(axis=1)) 

dataiswrong.to_excel('info_data_wrong.xlsx', engine='openpyxl')
wrongscore.to_excel('info_data_wrong.xlsx', engine='openpyxl')

df_sai = pd.read_excel('info_data_wrong.xlsx', engine='openpyxl')
df_dung = df.merge(df_sai.drop_duplicates(), how='left', indicator=True)
df_dung = df_dung[df_dung['_merge'] == 'left_only'].drop(columns=['_merge'])
df_dung.to_excel('info_data_right.xlsx', engine='openpyxl')
