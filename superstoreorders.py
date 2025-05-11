import pandas as pd
from sqlalchemy import create_engine

user = 'root'
password = 'Yugal%402005'
host = 'localhost'
database = 'sales'

# Create connection engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#monthly sales aggreate
query = """
SELECT DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m') AS MONTH,
    SUM(sales)
FROM superstoreorders
GROUP BY
	DATE_FORMAT(STR_TO_DATE(order_date, '%%d-%%m-%%y'), '%%Y-%%m')
ORDER BY 
	MONTH;
"""

query = """
SELECT 
	product_id, 
    product_name, 
    SUM(quantity)
FROM superstoreorders
GROUP BY 
	product_id, product_name
ORDER BY 
	SUM(quantity) DESC;
    """

#CUSTOMER LIFETIME VALUE
query = """
SELECT 
	customer_name,
    SUM(sales) AS CUSTOMER_LIFETIME_VALUE
FROM superstoreorders
GROUP BY
	customer_name
ORDER BY 
	SUM(sales) desc;
"""
    
#REGION WITH MOST/LEAST SALES
query = """
SELECT 
	region,
    SUM(sales) AS TOTAL_SALES
FROM superstoreorders
GROUP BY 
	region
ORDER BY 
	TOTAL_SALES DESC;
"""


df = pd.read_sql(query, engine)
print(df)