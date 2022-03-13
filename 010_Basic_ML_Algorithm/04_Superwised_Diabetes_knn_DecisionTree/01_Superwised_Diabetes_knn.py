"""
Case Study : Diabetes Predictions
  - Calculate the accuracy of model for different values of k (draw the graph)
  
"""

#############################################################

# Author        : Jayadip Halake
# Date          : 6-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Knn
# DataSet       : diabetes.csv
# Features      : 
# Label         : Outcome



#############################################################

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

import pandas as pd


def diabetes_predictor():
    # ----------------------------------------------------------
    # Step 1 : get the features and labels from data
    # 1.1 : Read csv
    csv_file = "diabetes.csv"
    data_df = pd.read_csv(csv_file)
    #print(data_df.isna().sum())
    print(data_df.columns)
    
    y = data_df["Outcome"]
    data_df.drop(columns =["Outcome"], inplace=True)
    x = data_df
    print(x.head(5))
    print(y.head(5))
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
    
    training_accuracy = []
    testing_accuracy = []
    
    k_range = range(2, 20)
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors = k )
        knn.fit(x_train, y_train)
        predict = knn.predict(x_test)
        
        train_score = knn.score(x_train, y_train)
        test_score = knn.score(x_test, y_test)
        training_accuracy.append(train_score)
        testing_accuracy.append(test_score)
    

    draw_graph(k_range, training_accuracy, testing_accuracy)

def draw_graph(k_range: list, training_accuracy: list, testing_accuracy: list):
    print(max(training_accuracy), "---- ", training_accuracy)
    print(max(testing_accuracy), "---- ", training_accuracy)
    
    
    plt.plot(k_range, training_accuracy, label="Training Accuracy")
    plt.plot(k_range, testing_accuracy, label="Testing Accuracy")
    
    plt.xlabel("n_neighbors")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig("knn_compare_model")
    plt.show()
    

# Main Entry function
def main():
    print("\n---- Diabetes Model by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Knn ---- ")
   
    diabetes_predictor()
    
  

# Starter
if __name__ == "__main__":
    main()
