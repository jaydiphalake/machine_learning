"""
Case Study : Diabetes Predictions - using Random Forest
  - Change the paramaters and check accuracy
  - check feature importance 
  
"""

#############################################################

# Author        : Jayadip Halake
# Date          : 12-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Randon Forest
# DataSet       : diabetes.csv
# Features      : 
# Label         : Outcome



#############################################################
from statistics import mode
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np


def diabetes_predictor():
    csv_path = "diabetes.csv"
    df_diabetes  = pd.read_csv(csv_path)
    #print(df_diabetes.head(5))
    print(df_diabetes.info()) # all columns are int and float
    print(df_diabetes.isna().sum()) # No null values

    y = df_diabetes["Outcome"]
    x = df_diabetes.loc[:, df_diabetes.columns != "Outcome"]
    print(y.head(5))
    print(x.head(5))

    x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8)
    print(len(x_train))
    print(len(y_train))

    model = RandomForestClassifier(n_estimators=100)
    model.fit(x_train,y_train)
    y_predicted = model.predict(x_test)

    train_score = model.score(x_train,y_train)
    test_score  = model.score(x_test,y_test)
    print("Train Accuracy : {:.3f}".format(train_score))
    print("Test Accuracy : {:.3f}".format(test_score))
    draw_feature_importance(model, tittle="Feature Importance ")
  

    model = RandomForestClassifier(n_estimators=10, max_depth=3)
    model.fit(x_train,y_train)
    y_predicted = model.predict(x_test)

    train_score = model.score(x_train,y_train)
    test_score  = model.score(x_test,y_test)
    print("Train Accuracy : {:.3f}".format(train_score))
    print("Test Accuracy : {:.3f}".format(test_score))
    draw_feature_importance(model, tittle="Feature Importance max_depth=5")

def draw_feature_importance(model : RandomForestClassifier, tittle: str = "Fetaure Importance"):
    features = model.feature_names_in_
    features_importance = model.feature_importances_
    print("feature ",features)
    print("feature Importance", features_importance)

    plt.figure(figsize=[8, 6])
    plt.barh(features, features_importance)
    plt.xlabel(xlabel="Feature Importance")
    plt.xticks(np.arange(0, 1, step=0.1))  
    plt.ylabel(ylabel="Feature Name")
    plt.title(label=tittle)

    plt.show()



# Main Entry function
def main():
    print("\n---- Diabetes Model by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Random Forest ---- ")
   
    diabetes_predictor()
    
  

# Starter
if __name__ == "__main__":
    main()
