import pandas as pd
import os
#Reading data from csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "data")
input_path=os.path.join(data_dir,"raw_data.csv")
df = pd.read_csv(input_path)


#Checking the basic info and dimensions of data sets
print(df.info())
print(df.shape)

#Coverting the column names for better accessing
df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
print(df.columns)

#Handling missing values
df['customerid']=df['customerid'].fillna(df['customerid'].median())
df['tenure']=df['tenure'].fillna(df['tenure'].median())

#Fix the data type of churn
df['churn']=df['churn'].astype('Int64')

#Coverting the column names for better accessing
df=pd.get_dummies(df,columns=['gender','subscription_type','contract_length'],
                  drop_first=True)

#Creating new features
# Customer value 
df['avg_spend_per_tenure'] = df['total_spend'] / (df['tenure'] + 1)

# Support intensity 
df['support_calls_per_tenure'] = df['support_calls'] / (df['tenure'] + 1)

# Payment behavior 
df['delayed_payment_flag'] = (df['payment_delay'] > 0).astype('Int64')

# Engagement score
df['engagement_score'] = (df['usage_frequency'] /(df['support_calls'] + 1))

#Removing Outliers
Q1 = df['total_spend'].quantile(0.25)
Q3 = df['total_spend'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['total_spend'] >= Q1 - 1.5 * IQR) &
        (df['total_spend'] <= Q3 + 1.5 * IQR)]

#Checking the correlation
corr = df.corr(numeric_only=True)
corr['churn'].sort_values(ascending=False)

#Droping columns
df.drop(columns=['customerid'], inplace=True)

#Saving processed data
output_path=os.path.join(data_dir,"processed_data.csv")
df.to_csv(output_path)


