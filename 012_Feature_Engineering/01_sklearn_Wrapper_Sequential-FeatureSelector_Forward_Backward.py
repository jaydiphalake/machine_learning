"""

 Wrapper Methods :  Compare combination of features with different combination of features
  
SequentialFeatureSelector
    - This Sequential Feature Selector adds (forward selection) or removes (backward selection)
             features to form a feature subset in a greedy fashion.
    - At each stage, this estimator chooses the best feature to add or remove based on the cross-validation score of an estimator

    - Forward-SFS is a greedy procedure that iteratively finds the best new feature to add to the set of selected features. 
        Concretely, we initially start with zero feature and find the one feature that maximizes a cross-validated score when an estimator is trained on this single feature. 
        Once that first feature is selected, we repeat the procedure by adding a new feature to the set of selected features. 
        The procedure stops when the desired number of selected features is reached, as determined by the n_features_to_select parameter.

    - Backward-SFS follows the same idea but works in the opposite direction: instead of starting with no feature and greedily adding features, 
        we start with all the features and greedily remove features from the set. The direction parameter controls whether forward or backward SFS is used.

    - In general, forward and backward selection do not yield equivalent results. 
            Also, one may be much faster than the other depending on the requested number of selected features: 
            if we have 10 features and ask for 7 selected features, forward selection would need to perform 7 iterations while backward selection would only need to perform 3.

sklearn version : scikit-learn      1.0.2

https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html

"""

##############################################################################

# Author                 : Jayadip Halake
# Date                   : 5-Mar-2022
# Feature Selection Type : Wrapper Methods
# Methods                : Forward Selection and Backward Selection
##############################################################################


import pandas as pd
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Main Entry function
def main():
    print("\n---- Supervised Feature Selection : Jayadip Halake : ")
    print("--- Type : Wrapper Methods---- ")
    print("--- Techniques : Forward Selection and Backward Selection ---- ")
    iris_feature_selection()

def iris_feature_selection():
    # load data
    X, Y=load_iris(return_X_y=True, as_frame=True)
    features_names = X.columns
    #print(X)
    #print(Y)
    #print(features_names)

    # create model 
    knn = KNeighborsClassifier(n_neighbors=3)
    
    # forward feature selection
    sfs_forward = SequentialFeatureSelector(knn, n_features_to_select=3, direction="forward"
        , scoring="accuracy") 
    sfs_forward = sfs_forward.fit(X, Y)
    print("Selected features : ", sfs_forward.get_feature_names_out())

    # Bckword feature selection
    sfs_backward = SequentialFeatureSelector(knn, n_features_to_select=3, direction="backward"
        , scoring="accuracy") 
    sfs_backward = sfs_backward.fit(X, Y)
    print("Backword Selected features : ", sfs_backward.get_feature_names_out())





if __name__ == "__main__":
    main()