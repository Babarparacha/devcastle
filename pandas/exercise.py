import pandas as pd

#=========read data from csv file into dataframe============

df = pd.read_csv('F:\Python course\devcastle\pandas\e_data.csv') #-----same for excel read_excel("abc.xlsx") or json file(read_json("file.json"))
#print(df.head())  #first 5 rows
# print(df.tail()) #last 5  rows
# print(df.info()) #-----display info about data set-----
# print(df)

# after clean used data 
data={
    "name":['ahsan','noman','jameel'],
    "age":[30,40,50],
    "salary":[30000,40000,50000],
    "city":['lahore','karachi','bahawalnagar'],
}
# df=pd.DataFrame(data) #----------used to store and work with data in rows and columns-----------.
# --------------print("descriptive statistics")-------------------
# print(df.describe()) #-----Data ka summary nikalna-----------------
# print(f"shape:{df.shape}")  #-----give us file dimension nd return tuple---------
# print(f"column:{df.columns}")  #--------return column name---------
#print(f"Column name:\n{df['name'].to_string(index=False)}")  #----accesing column----------
#print(df[['name','age','salary']])  #----------accesing multiple column---------
#print(df[df['salary']>30000]) # ---------filter data-----------
# print(df[(df['salary'] > 30000) & (df['age'] > 30)]) # ----------filter data on multiple condition------
# print(df[(df['salary'] > 30000) | (df['age'] > 40)]) #------filter data on multiple condition---------
# print(df)
# create file for this data 
# df.to_csv("F:\Python course\devcastle\pandas\data.csv", index=False)
# print("File created successfully!")