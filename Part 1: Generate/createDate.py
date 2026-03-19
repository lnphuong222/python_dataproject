import pandas as pd
import numpy as np
import random

gender = ['Male', 'Female']
education_level = ['High school', 'College', "Bachelor's degree", "Master's degree", 'None']
race = ['Team 1', 'Team 2', 'Team 3', 'Team 4']
test_status = ['Completed', 'None']

df = pd.DataFrame({
    'Gender': [random.choice(gender) for _ in range(1000)],
    'Race': [random.choice(race) for _ in range(1000)],
    'Parental level of education': [random.choice(education_level) for _ in range(1000)],
    'Test status': [random.choice(test_status) for _ in range(1000)],
    'Part A': np.random.randint(0, 51, 1000),
    'Part B': np.random.randint(0, 51, 1000),
    'Part C': np.random.randint(0, 101, 1000), 
    'Part D': np.random.randint(0, 101, 1000)
})

df['Total'] = df['Part A'] + df['Part B'] + df['Part C'] + df['Part D']
df['Test status'] = df['Total'].apply(lambda x: 'Passed' if x >= 150 else 'Failed')

df.to_excel('data.xlsx', engine='openpyxl', index=False, sheet_name='Test Data')
print('Successfully')
