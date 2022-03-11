"""
Case Study : Wine Predictor
  - Wine quality(class) is decided on its contents
  - Calculate the accuracy using - Knn model

"""

#############################################################

# Author        : Jayadip Halake
# Date          : 6-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Knn (KNeighborsClassifier)
# DataSet       : WinePredictor.csv
# Features      : Alcohol,Malic acid,Ash,Alcalinity of ash,Magnesium,Total phenols,Flavanoids,Nonflavanoid phenols,Proanthocyanins,Color intensity,Hue,OD280/OD315 of diluted wines,Proline
# Label         : Class



#############################################################

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd


def wine_predictor():
    # ----------------------------------------------------------
    # Step 1 : get the features and labels from data
    # 1.1 : Read csv
    csv_file = "WinePredictor.csv"
    data_df = pd.read_csv(csv_file)

    # 1.2 create label encoder
    label_encoder = preprocessing.LabelEncoder()

    # 1.3 encode features and labels column and store encoding mapping
    data_df["class_enc"] = label_encoder.fit_transform(data_df["Class"])
    # print (data_df.head(n=5))
    
    data = data_df[["Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]].values
    
    target = data_df["Class"].values
    
    train_data, test_data , train_target, test_target = train_test_split(data, target, test_size = 0.2)

    accuracy_result = {}
    for k in range (2, 16):
        # algo
        classifier = KNeighborsClassifier(n_neighbors = k)
        
        # model
        model = classifier.fit(train_data, train_target)
        
        # Predictions
        predictions = model.predict(test_data)
        
        # accuracy_score        
        acc_score = accuracy_score(test_target, predictions)
        accuracy_result[k] = (acc_score )
        
    return accuracy_result


# Main Entry function
def main():
    print("\n---- Wine Calss Predictor by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Knn (KNeighborsClassifier) ---- ")

    # Note : train_test_split method -> by default shuffle the data. So every time accuracy is different
    for i in range(5):
        accuracy_result = wine_predictor()
        print(f"\n accuracy_result = {accuracy_result}")
  

# Starter
if __name__ == "__main__":
    main()
