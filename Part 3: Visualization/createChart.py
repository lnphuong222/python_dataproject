import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('saleData.xlsx', engine='openpyxl')

'''df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date').resample('Y')['Total Price'].sum().plot()
plt.title('Tổng doanh thu theo năm')
plt.ylabel('Doanh thu')'''

df.groupby('Product')['Total Price'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Tổng doanh thu theo mặt hàng')
plt.xlabel('Sản phẩm')
plt.ylabel('Doanh thu')
plt.tight_layout()
plt.show()
