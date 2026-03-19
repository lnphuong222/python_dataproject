import pandas as pd
import random
df = pd.read_excel('info_data.xlsx', engine='openpyxl')
dob_list = [
    "1998-05-21", "02/11/2000", "2001.12.30", "15-08-1999", "31/02/2001",
    "2025-01-01", "1997/13/05", "abc", "2000-00-15", "",
    "1996-12-45", "1998/07/09", "1990-2-30", "12.12.1995", "07-31-1997",
    "1999.11.31", "2002-04-25", "25/04/2002", "1995-12-31", "32/01/1994" ]

age_list = [
    25, 30, -5, 150, "abc", 0, 99, 101, 45, None,
    35, 60, 27, 85, "50", 120, -1, "?", 32, 200 ]

name = [
    "James Anderson", "Emily Johnson", "Michael Brown", "Olivia Davis", "William Miller",
    "Sophia Wilson", "David Moore", "Isabella Taylor", "Daniel Thomas", "Ava White",
    "Joseph Harris", "Mia Martin", "Andrew Thompson", "Charlotte Garcia", "Benjamin Martinez",
    "Amelia Robinson", "Matthew Clark", "Harper Lewis", "Ethan Lee", "Abigail Walker" ]

df.loc[:19, 'Name'] = name

def wrongdata():
    return random.choice(
        [ round(random.uniform(-10, -0.1), 1),
         random.randint(0, 10),
         None ]
    )
    
object = ['Math', 'English', 'Physical', 'Chemistry']
data = {}
for subject in object:
    df[subject] = [
        wrongdata() if random.random() < 0.4 else round(random.uniform(0, 10), 1)
        for _ in range(len(df))
    ]

df.to_excel("info_data.xlsx", engine='openpyxl', index=False)
