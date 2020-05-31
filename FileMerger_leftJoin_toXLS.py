import pandas as pd

#Open the 2 different files to merge in CSV 
df1 = pd.read_csv("C:\\Users\\david\\Desktop\\SalReview_Summary_20200512.csv")
df2 = pd.read_csv("C:\\Users\\david\\Desktop\\Sal_CrossCheck.csv")

#Merge both files using left join
merged_left = pd.merge(left=df1, right=df2, how='left', left_on='USERID', right_on='USERID')

#Save to excel format with UTF-8 encoding
merged_left.to_excel("C:\\Users\\david\\Desktop\\FullSal.xlsx", index=False, encoding='utf-8')