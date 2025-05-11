import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

user = 'root'
password = 'Yugal%402005'
host = 'localhost'
database = 'sales'
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Monthly sales aggregate
query = """
SELECT 
    DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m') AS month,
    SUM(sales) AS revenue
FROM superstoreorders
GROUP BY
    DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m')
ORDER BY 
    month;
"""
df = pd.read_sql(query, engine)

# Line plot for monthly revenue
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='month', y='revenue', marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
