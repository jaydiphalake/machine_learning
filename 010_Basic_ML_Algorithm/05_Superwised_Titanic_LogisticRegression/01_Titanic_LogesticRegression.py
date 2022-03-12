"""
Case Study : Titanic Survival Prediction
    - Data set contain multiple feature avout survived and non-survived passanger
    - Use Logestic Regression algorithm to tranin and predict whether passanger is survived or not
    
Dataset url : https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

"""

#############################################################

# Author        : Jayadip Halake
# Date          : 13-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Logestic Regression
# DataSet       : titanic.csv
# Features      : 
# Label         : Survived

#############################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def titanic_logestic():
    # Step 1 : Load Data
    titanic_data = pd.read_csv("titanic.csv")
    
    print("Top 5 enteries from dataset are ")
    print(titanic_data.head(n=5))
    
    print(f"Number of passanger are : { str (len(titanic_data))}")
    
    #Step 2 : Analyze Data
    #analyze_data(titanic_data)

    #Step 3 : Clean Data
    print("\n Data Before Cleaning : ")
    print(titanic_data.head(3))
    titanic_data = data_cleaning(titanic_data)
    print("\n Data After Cleaning : ")
    print(titanic_data.head(3))
    
    #Step 4 : Split data and Train Model
    y = titanic_data["Survived"]
    x = titanic_data.drop("Survived", axis=1)
    
    #print(" Features data : ")
    #print(x.head(3))
    #print(" Label data : ")
    #print(y.head(3))
    x_train, x_test, y_tain, y_test = train_test_split(x, y, test_size=0.2)
    
    model = LogisticRegression()
    model.fit(x_train, y_tain)
    
    # Step 5 : Test model
    prediction = model.predict(x_test)
    
    #Step 6 : Calculate accuracy
    print("\n\n ----Accuracy score ----")
    print(accuracy_score(y_test, prediction ))
    
    print("\n ----Classification Reports----")
    print(classification_report(y_test, prediction ))
    
    print("\n ----confusion_matrix----")
    print(confusion_matrix(y_test, prediction ))
   
    #check the accuracy after droping Age columns
    #x = titanic_data.drop("Age", axis=1)

def data_cleaning(titanic_data):
    #clean data
    # ["PassengerId", "Name", "Ticket"] has no impact, so drop these columns
    titanic_data.drop(titanic_data[["PassengerId", "Name", "Ticket"]], axis=1, inplace= True)
    #print(titanic_data.head(n=5))
  
    titanic_data["Embarked"] = titanic_data["Embarked"].fillna("S")
    #print(titanic_data.isna().sum())
  
    # update age
    #print("Null ", titanic_data["Age"].isna().sum())
    age_slice = titanic_data["Age"].copy()
    min_age = age_slice.dropna().min()
    max_age = age_slice.dropna().max()
    age_null_cnt=age_slice.isna().sum()
    # generate range age values
    random_age = np.random.randint(low=min_age, high=max_age, size=(age_null_cnt))
    
    age_slice[np.isnan(age_slice)] = random_age
    titanic_data["Age"] = age_slice
    #print("Null ", titanic_data["Age"].isna().sum())
  
    titanic_data.drop(titanic_data[["Cabin"]], axis=1, inplace= True)
  
    df_sex =pd.get_dummies(titanic_data["Sex"]  , prefix="Sex"  ) 
    df_sex = pd.get_dummies(titanic_data["Sex"]  , prefix="Sex" , drop_first=True )
    #print(df_sex.head(n=5))
    
    titanic_data = pd.concat([titanic_data, df_sex], axis=1)
    #print(titanic_data.head(n=5))
    
    df_Pclass= pd.get_dummies(titanic_data["Pclass"]  , prefix="Pclass" )
    df_embarked = pd.get_dummies(titanic_data["Embarked"]  , prefix="Embarked" )
    titanic_data = pd.concat([titanic_data,df_Pclass, df_embarked ], axis= 1)
    #print(titanic_data.head(3))
    
    # drop irrelevent columns
    titanic_data.drop(["Pclass","Embarked", "Sex", "SibSp" , "Parch"], axis=1, inplace=True)
    #print(titanic_data.head(n=5))
    
    #print("----------")
    #print(titanic_data.isna().sum())
    
    return titanic_data
    

def analyze_data(titanic_data : pd.DataFrame ):
    
    # ----- Visulization : Survived and non-survived passanger count
    print("Visulization : Survived vs non-survived passanger count")
    plt.figure()
    x_axis_targer = "Survived"
    
    # sns.countplot
    # x, y: This parameter take names of variables in data or vector data, optional, Inputs for plotting long-form data.
    # hue : (optional) This parameter take column name for colour encoding.
    # data : (optional) This parameter take DataFrame, array, or list of arrays, Dataset for plotting. If x and y are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.
    
    
    sns.countplot(data=titanic_data, x= x_axis_targer).set_title("Survived and non-survived passanger count")
    plt.show()
    
    

    # ----- Visulization : Based on Gender - Survived and non-survived passanger  count
    print("\n Visulization : Based on Gender - Survived and non-survived passanger count ")
    plt.figure()
    x_axis_targer = "Survived"
    
    sns.countplot(data=titanic_data, x= x_axis_targer, hue="Sex").set_title("Based on Gender - Survived and non-survived passanger count")
    plt.show()
    
    # ----- Visulization : Based on Passanger Class - Survived and non-survived passanger count 
    print("\n Visulization : Based on Passanger Class  - Survived and non-survived passanger count")
    plt.figure()
    x_axis_targer = "Survived"
    
    sns.countplot(data=titanic_data, x=x_axis_targer, hue="Pclass").set_title("Based on Passanger Class  - Survived and non-survived passanger count")
    plt.show()
    
    # ----- Visulization : Based on Passanger Age - Survived and non-survived passanger count 
    print("\n Visulization : Based on Age  - Survived and non-survived passanger count")
    plt.figure()
    titanic_data.plot.hist(column=["Age"], by="Survived")
    plt.show()
    
    # ----- Visulization : Based on Fare - Survived and non-survived passanger count 
    print("\n Visulization : Fare  - Survived and non-survived passanger count")
    plt.figure()
    titanic_data["Fare"].plot.hist().set_title("Based on Fare  - Survived and non-survived passanger count")
    plt.show()
    

# Main Entry function
def main():
    print("\n---- Titanic Survival Prediction by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Logestic Regression ---- ")

    titanic_logestic()

# Starter
if __name__ == "__main__":
    main()
