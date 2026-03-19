import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('saleData.xlsx', engine='openpyxl')

revenue_by_product = df.groupby('Product')['Total Price'].sum().sort_values(ascending=False).reset_index()

sns.set_theme(style="whitegrid")  
plt.figure(figsize=(8, 5))  

sns.barplot(data=revenue_by_product, x='Product', y='Total Price', palette='viridis')

plt.title('DOANH THU THEO MẶT HÀNG', color='red', fontweight='bold')
plt.xlabel('Sản phẩm')
plt.ylabel('Doanh thu')
plt.tight_layout()
plt.show()
