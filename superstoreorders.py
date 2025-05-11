import pandas as pd
from sqlalchemy import create_engine

# Replace with your actual credentials
user = 'root'
password = 'Yugal%402005'
host = 'localhost'
database = 'sales'

# Create connection engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Example query: Monthly revenue
query = """
SELECT DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m') AS MONTH,
    SUM(sales)
FROM superstoreorders
GROUP BY
	DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m')
ORDER BY 
	MONTH;
"""

# Load query results into DataFrame
df = pd.read_sql(query, engine)
print(df)