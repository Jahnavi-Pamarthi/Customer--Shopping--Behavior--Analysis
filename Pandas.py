
import pandas as pd
df=pd.read_csv("C:\\Users\\jahnavi\\Downloads\\customer_shopping_behavior (1).csv")
print(df.head())
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
#create a coloumn age_group
labels=['young adult','adult','middle-aged','senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(10))
#create a column purchase_frequency_days
frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
df=df.drop('promo_code_used',axis=1)
print(df.columns)
#connect to sql
#replace placeholders with your actual details
from sqlalchemy import create_engine
# MySQL connection details
username = "root"          # your MySQL username
password = "340734" # your MySQL password
host = "localhost"
port = "3306"              # default MySQL port
database = "analysis"
engine=create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
#write Dataframe to sql
table_name="table"
df.to_sql(table_name , engine,if_exists="replace",index=False)
print("data sucessfully uploaded!")







