import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import xgboost as xgb
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

location_encoder=LabelEncoder()
Sector_encoder=LabelEncoder()
job_encoder=LabelEncoder()
Eligibility_encoder=CountVectorizer()
data=pd.read_csv("DataSet.csv")

cv=CountVectorizer()
#cv.fit_transform(data["Eli"])

def Convert(df):## train and test set
    encod=df[["Location","Job_Description","Sector","Eligibility","salary","Month"]]
  #  encod=pd.DataFrame()
    encod["Location"]=location_encoder.fit_transform(df["Location"])
    encod["Job_Description"]=job_encoder.fit_transform(df["Job_Description"])
    encod["Sector"]=Sector_encoder.fit_transform(df["Sector"])
    trans=cv.fit_transform(df["Eligibility"])
    trans=pd.DataFrame(trans.todense(),columns=cv.get_feature_names())# Create a dataframe with only Eligibility values
    df2=pd.concat([encod,trans],axis=1)
    return df2

## pridicting data Set


def fun(salary, job_label,Sector_label,City_label, Education, Month=0):

    #Month=0
     #encod=df[["Location","Job_Description","Sector","Eligibility","salary","Month"]
    education_encoded=cv.transform([Education])

    job_int=job_encoder.transform([job_label])#return an array

   # print(job_int)

    city_int=location_encoder.transform([City_label])

    sector_int=Sector_encoder.transform([Sector_label])

    df1=pd.DataFrame([[city_int[0],job_int[0],sector_int[0],int(salary),Month]],columns=["Location","Job_Description","Sector","salary","Month"])#give the data frame which have all the labeles variable


    df2=pd.DataFrame(education_encoded.todense(),columns=cv.get_feature_names())# gives dataframe by encoding EDUCATION

    df1=pd.concat([df1,df2],axis=1)#Combined data frame which is to be predicted

    return df1
    

    
if(__name__) == '__main__':

	X=Convert(data)
	to_predict=fun("3000","SALES & MARKETING AGENT","Engineering","DELHI","BTech")

	##for prediction

	##from xgboost import XGBRFRegressor
	model1=xgb.XGBRegressor()

	X_train,X_test,y_train,y_test=train_test_split(X,data["vacancies"],random_state=0)
	model1.fit(X_train,y_train)
	model1.score(X_test,y_test)
