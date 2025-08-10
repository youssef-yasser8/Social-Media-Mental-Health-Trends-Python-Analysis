#==========================================================================================================
"""
Social Media and Mental Health Analysis  
Author: Mohamed Samy  
Date: February 2025  
----------------------------------
Description:  
This script analyzes the relationship between social media usage and mental health.  
It processes survey data, extracts insights, and visualizes key trends.  
----------------------------------
Libraries:  
- pandas: Data manipulation  
- numpy: Numerical analysis  
- matplotlib: Visualization  
----------------------------------
Steps:  
1. Load data from CSV  
2. Clean data (handle missing values, duplicates, and date conversion)  
3. Analyze gender, relationship status, and occupation trends  
4. Extract insights on social media distraction, comparison, and mental health impact  
5. Generate visualizations (bar charts, pie charts)  
----------------------------------
Note: Some visualization code is commented out. Uncomment for analysis.  
"""
#==========================================================================================================

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Getting Data 
data=pd.read_csv(r'F:\Projects\Python_Hotle_Dashboard\Row_Data.csv')

#Data Cleaning 
#Check for missing values
print(data.isnull())
#Check for duplicates 
print(data.duplicated())
#Getting data types 
print(data.dtypes)
#Handling Date Column
data['Timestamp']=pd.to_datetime(data['Timestamp'])

#==========================================================================================================


# data['Month']=pd.to_datetime(data['Timestamp']).dt.month_name()

# a=data.groupby(by='Month')[['f','t','i','y']].sum()

# fig,ax=plt.subplots()
# a.reset_index(inplace=True)
# ax.bar(x=a['Month'],height=a[['f','t','i','y']])


# plt.show()

#===================================================================================================================================

#Gender Distribution

# fig,ax=plt.subplots()
# data['2. Gender']=[ i if i in ['Male','Female'] else 'Non-binary' for i in data['2. Gender'] ]
# colors=['#FCDDBC','#B8D8BA','#B4B5A8']
# gender_counts = data['2. Gender'].value_counts()
# ax.pie(gender_counts,labels=gender_counts.index,autopct='%1.2f%%',colors=colors)
#===================================================================================================================================

#User Status

# fig,ax=plt.subplots()
# group_count=data['3. Relationship Status'].value_counts()
# colors=['#2F3E46','#354F52','#52796F','#84A98C']
# ax.barh(group_count.index,group_count,color=colors)
# ax.set_title('User Relationship Status',fontsize=22,color='#6a7165',fontweight='bold')
# ax.spines[['top','right','left','bottom']].set_visible(False)
# ax.xaxis.set_visible(False)
# ax.yaxis.set_ticks_position('none')
# ax.tick_params(axis='y',labelsize=8.5,pad=0)
# for i in ax.patches:
#     plt.text((i.get_width())+3,(i.get_y())+.35,str(round(((i.get_width())/sum(group_count))*100,2))+'%')
#===================================================================================================================================

#Occupation Status

# figm,ax=plt.subplots()
# group_count=data['4. Occupation Status'].value_counts()
# colors=['#584d3d','#9F956C','#CBBF7A','#f4e87c']
# ax.bar(group_count.index,group_count,color=colors)
# ax.spines[['top','right','left','bottom']].set_visible(False)
# ax.yaxis.set_visible(False)
# ax.xaxis.set_ticks_position('none')
# ax.set_title('Occupation Status',fontweight='bold',fontsize=22,color='#8E935D')
# ax.tick_params(axis='x',labelsize=8.5)
# for i in ax.patches:
#     plt.text(i.get_x()+.25,i.get_height()+5,str(round((i.get_height()/sum(group_count))*100,2))+'%')

#===================================================================================================================================

#Insights

# print(round(np.average(data['9. How often do you find yourself using Social media without a specific purpose?']),2))
# print(round(np.average(data['10. How often do you get distracted by Social media when you are busy doing something?']),2))
# print(round(np.average(data['14. Do you find it difficult to concentrate on things?']),2))
# print(round(np.average(data['15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?']),2))
# print(round(np.average(data['18. How often do you feel depressed or down?']),2))
# print(round(np.average(data['20. On a scale of 1 to 5, how often do you face issues regarding sleep?']),2))

#===================================================================================================================================

#Platforms Distribution

# fig,ax=plt.subplots()
# data['Facebook']=data['7. What social media platforms do you commonly use?'].str.contains('Facebook')
# data['X-Twitter']=data['7. What social media platforms do you commonly use?'].str.contains('Twitter')
# data['Instagram']=data['7. What social media platforms do you commonly use?'].str.contains('Instagram') 
# data['YouTube']=data['7. What social media platforms do you commonly use?'].str.contains('YouTube') 
# value_count=[sum(data['Facebook']),sum(data['X-Twitter']),sum(data['Instagram']),sum(data['YouTube'])]
# colors=['#30A1D2','black','#FA7921','#DF3000']
# ax.bar(['Facebook','X-(Twitter)','Instagram','YouTube'],value_count,color=colors)
# ax.set_title('Platforms Usage',fontsize=20,fontweight='bold',color='black')
# ax.tick_params(axis='x',labelsize=8.5)
# ax.spines[['top','right','left','bottom']].set_visible(False)
# ax.yaxis.set_visible(False)
# ax.xaxis.set_ticks_position('none')
# for i in ax.patches:
#     plt.text(i.get_x()+.21,i.get_height()+5,str(round(((i.get_height())/sum(value_count))*100,2))+'%')
# plt.show()




