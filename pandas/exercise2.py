import pandas as pd

data={
    "name":["ahsan",'noman','jameel'],
    "age":[95,None,40],
    "salary":[30000,40000,50000],
    "city":['lahore','karachi',None],
    "date":[12-12-2026,13-12-2026,None],
}
df=pd.DataFrame(data)
# --------------adding a new column--------------------
# df['bonus']=df['salary']*0.1 
# df['salary']=df['salary']*0.1 #####-----update existing values------------
# df.insert(4, "rating", 5) #########------(index,column,value) using inset method-----------
# df.insert(0, "Employess_id", [1,2,3])  #----------(index,column,value) using inset method-------
# df.loc[0,'salary']=55000 #-------update specific values------------
# ---------------df.dropcolumns(["column_name",inplace=True=update org directly])drop specific column-------
# print(df.drop(columns=['city',"age"],inplace=True))

#------------handling missing data---------------------
# print(df.isnull()) # ---------return true for missing values nd false to non missing-------
# print(df.isnull().sum()) # -------return sum of null or missing value------------
# -------------drop specific data from a column-----------------
# print(df.dropna(axis=0,inplace=True)) #------axis=0 means delete val from rows----------
#-----------fill null or missing values---------------
# df.fillna(0,inplace=True) # --------fill missng val with 0 -----------
# df['age'].fillna(df['age'].mean(),inplace=True)
# print(df)

#-----ineterpolation=means fill value estimated in missing value----------
#polynomial
#time
# df.interpolate(method="linear",axis=0,inplace=True) ##---------linear----------
# df.interpolate(method="polynomial", order=2,axis=0,inplace=True) 
# df.interpolate(method="time",axis=0,inplace=True) 
# print(df)
#-----------sorting ------------
# df.sort_values(by=['age','date'],ascending=[False,False],inplace=True) #---------df.sort_values="column_name",order=trues,false,inplace=True-----
# print(df)
#------- summary -----------
# print(df['salary'].mean())  # mean salary 
# -------------grouping-split data into parts-------------
data2={
    "name":["badar",'ahsan','ali'],
    "age":[30,27,40],
    "salary":[130000,240000,350000],
    "city":['lahore','karachi','fsd']
}
# df1=pd.DataFrame(data2)
# print(df1.groupby(['name','age'])['salary'].sum()) #-----similar min,max ,count etc------
# print(df1.groupby(['name','age'])['salary'].min()) #------similar min,max ,count etc----
# print(df1.groupby(['name','age'])['salary'].max()) #----similar min,max ,count etc-----
# print(df1.groupby(['name','age'])['salary'].count()) #----similar min,max ,count etc-------
#----------merging= combine =matches keys----------
df_cus=pd.DataFrame({
   "customer_id":[1,2,3,4],
    "name":["badar",'ahsan','ali','faisal']
})
df_order=pd.DataFrame({
   "customer_id":[1,1,3,4],
    "orderAmount":[250,40,350,500]
})
# print(pd.merge(df_cus,df_order,on="customer_id",how="outer")) #---------join(left,right,outer,inner,cross) replace with NaN if value not match------
#-----------concatination-------------

df1 = pd.DataFrame({
    "Name": ["Ali", "Ahmed"],
    "country": ["pakistan", "india"]
})
df2 = pd.DataFrame({
    "Name": ["Sara", "Zain"],
    "country": ["iran", "afghanistan"]
})

print(pd.concat([df1, df2], axis=0,ignore_index=True))