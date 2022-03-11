"""
Case Study : Insurance Data 
    - Data set contain person age and insurance is purchased or not
    - Calculate F1 score and display confusion_matrix
    
Dataset url : https://github.com/codebasics/py/blob/master/ML/7_logistic_reg/insurance_data.csv


    #confusion matrix  :  Total Sample (n) = 165
    #                  : predicted_no (55) -> Predicted_yes (110)
    # actual_no (60)   :  TN  = 50         -> FP  = 10
    # acutal_yes (105) :  FN  = 5          -> TP = 100
    
    # Accuarcy = (TN + TP) / (total Sample) = (50+100)/165 = 0.91
    # miss classification = wrong prediction rate = 1-accuracy = 1-.91 = .09 = (FP+FN)/total
    # Recall = True Positivity rate = TP / acutal_yes = 100 / 105 = 0.95
    # Specificity = True Negativity Rate = TN / actual_no = 50/60 = 0.83
    # Precision  = TP / predicted_yes = 100 / 115 = 0.91
    # Prevelance = acutal_yes / total = 102 / 165 = 0.64
    
    # f1_Scope = Model Accuarcy  
               = 2 * ( (recall * precision) / (recall + precision) )
               = 2 * ( (0.95 * 0.91)/ (0.95+.091) ) = 0.92
    
     

"""

#############################################################

# Author        : Jayadip Halake
# Date          : 19-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Logistic Regression
# DataSet       : insurance_data.csv
# Features      : age
# Label         : bought_insurance

#############################################################

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def insurance_logestic(data_file_path):
    df = pd.read_csv(data_file_path)
    print("\n First entries : ")
    print(df.head(5))
    
    # show data on graph
    plt.scatter(x=df.age, y= df.bought_insurance, marker="+", color="red")
    #plt.show()
    
    # split the data
    x_train, x_test, y_train, y_test = train_test_split(df[["age"]], df.bought_insurance, train_size= 0.5  )
    
    print("\n Indepdent variable of training x_train: ")
    print(x_train)
    
    print("\n Dedepdent variable of training y_train: ")
    print(y_train)
    
    print("\n Indepdent variable of Test x_test: ")
    print(x_test)
    
    print("\n Dedepdent variable of Test y_test: ")
    print(y_test)
    
    model = LogisticRegression();
    # train the model
    model.fit(x_train, y_train)
    
    # predict the output
    y_predicted = model.predict(x_test)
    print("\n predict outut y_predicted: ")
    print(y_predicted)
    
    # Probability
    prob = model.predict_proba(x_test)
    print(f"\n Probability is Result : 0 and 1 are ")
    print(prob)
 
    # confusion_matrix
    print("\n confusion_matrix is :")
    print(confusion_matrix(y_test, y_predicted))
        
    
    # classification report
    class_report = classification_report(y_test, y_predicted)
    print("\n Calssification reports of Logistic regression is :")
    print(class_report)
    
     
    

# Main Entry function
def main():
    print("\n---- Insurance Case Study : Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Logistic Regression ---- ")

    data_file_path = "insurance_data.csv"
    insurance_logestic(data_file_path)

# Starter
if __name__ == "__main__":
    main()
