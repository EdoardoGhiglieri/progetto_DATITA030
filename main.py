

import pandas as pd


pd.set_option('display.max.rows',None)
pd.set_option('display.max.columns', None)
pd.set_option('display.width',None)

df1 = pd.read_csv('data/raw/olistPW_2016_customers.csv')
df2 = pd.read_csv('data/raw/olistPW_2016_orders.csv')
df3 = pd.read_csv('data/raw/olistPW_2016_categories.csv')
df4 = pd.read_csv('data/raw/olistPW_2016_sellers.csv')
df5 = pd.read_csv('data/raw/olistPW_2016_items.csv')
df6 = pd.read_csv('data/raw/olistPW_2016_products.csv')
df7 = pd.read_csv('data/processed/products_list_20250924125029.csv')



#print(df6)
print(df7.dtypes)

#df2['order_estimated_delivery_date'] = pd.to_datetime(df2['order_estimated_delivery_date'])

#df7[["order_delivered_customer_date","order_estimated_delivery_date"]] = df7[['order_delivered_customer_date','order_estimated_delivery_date']].apply(pd.to_datetime)
#df7["order_estimated_delivery_date"] = pd.to_datetime(df7["order_estimated_delivery_date2"])

#df7["order_estimated_delivery_date"] = df2["order_estimated_delivery_date"].dt.date
#print(df7["order_estimated_delivery_date"].dtype)
#print(df2)
#print(df6[df6.duplicated()])





'''df1['cap'] = df1['cap'].astype(str)
df1['cap_length'] = df1['cap'].str.len()
print (df1['cap_length'])
df1['cap'] = df1['cap'].apply(lambda value : "00" + value)
df1 = df1.drop(columns= ['cap_length'])
print(df1)'''

'''df1({'cap':['83100',0]})
print(df1)'''
'''cap = df1['cap'].astype(str)



for i in cap:
    if len(i) == 3:
        i = '00' + cap
    elif len(i) == 4:
        i = '0' + cap
'''

'''for i in df1['cap']:
    print(len(df1['cap']))'''

#print(df3.nunique())
#print(df2.nunique())

#print(duplicates)

#duplicates2 = df2[df2.duplicated('customer_id')]
#print(duplicates2)

#df2 = df1.duplicated()
'''for row in df1.duplicated():
    if row == True:
        print (row)


for row2 in df2.duplicated():
    if row2 == True:
        print (row2)
'''

