"""
Case Study : Breast  Cancer Predictions - using SVM ( Support Vector Machine)

SVM details :
https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python

"""

#############################################################

# Author        : Jayadip Halake
# Date          : 13-Feb-2022

# ML Type       : Supervised Learning
# Classifier    : Support Vector Machine
# DataSet       : sklearn.datasets -> breast_cancer

#############################################################

from sklearn import svm
from sklearn import metrics
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def svm_lienar():

    #Load dataset from sklearn.datasets 
    cancer = load_breast_cancer()

    # print  features
    print("Features ", cancer.feature_names)
    print("First 5 records are : ")
    print(cancer.data[0:5])

    # print Target / Label
    print("Target ", cancer.target_names)
    # 0='malignant' 1='benign'
    print(cancer.target[:5])

    #split the data
    x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, train_size=0.8, random_state=44)


    print("\n\n ------kernel=\"linear\" ")
    #Create model
    model_svc_linear = svm.SVC(kernel="linear")

    # Train the model
    model_svc_linear.fit(x_train, y_train)

    # Predict the response
    y_predict = model_svc_linear.predict(x_test)

    # Evaluate the model
    print_accurarcy(y_true=y_test, y_pred=y_predict)

    print("\n\n ------kernel=\"rbf\" ")
    #Create model
    model_svc_rbf = svm.SVC(kernel="rbf")

    # Train the model
    model_svc_rbf.fit(x_train, y_train)

    # Predict the response
    y_predict = model_svc_rbf.predict(x_test)

    # Evaluate the model
    print_accurarcy(y_true=y_test, y_pred=y_predict)


def print_accurarcy(y_true, y_pred):
    # Evaluate the model
    # calcualate accurarcy
    acc_score = accuracy_score(y_true=y_true, y_pred=y_pred)
    print("Accuarcy score : {:.4} ".format(acc_score))

    # get Precision and Recall
    precision = metrics.precision_score(y_true=y_true, y_pred=y_pred)
    print("precision is : {:.4} ".format(precision))

    recall = metrics.recall_score(y_true=y_true, y_pred=y_pred)
    print("recall is : {:.4} ".format(precision))

# Main Entry function
def main():
    print("\n---- Breast Cancer Case Study : Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : SVM ( Support Vector Machine) ---- ")

    svm_lienar()


if __name__ == "__main__":
    main()