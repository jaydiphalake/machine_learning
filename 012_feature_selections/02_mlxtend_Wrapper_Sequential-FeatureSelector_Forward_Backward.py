"""
Wrapper Type- Forward Selection and Backward Selection using [mlxtend]

Version :
scikit-learn      1.0.2
mlxtend           0.19.0

mlxtend =  http://rasbt.github.io/mlxtend/
mlxtend API = http://rasbt.github.io/mlxtend/api_subpackages/mlxtend.feature_selection/#sequentialfeatureselector


"""

##############################################################################

# Author                 : Jayadip Halake
# Date                   : 5-Mar-2022
# Feature Selection Type : Wrapper Methods
# Methods                : Forward Selection and Backward Selection
# Library                : mlxtend
##############################################################################


from matplotlib import pyplot as plt
import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import  load_iris, load_wine
from mlxtend.plotting  import plot_sequential_feature_selection as plot_sfs

# Main Entry function
def main():
    print("\n---- Feature Selection : Jayadip Halake : ")
    print("--- Type : Wrapper Methods---- ")
    print("--- Techniques : Forward Selection and Backward Selection ---- ")
    
    forward_feature_selection()

    backward_feature_selection()


def forward_feature_selection():
    # load data
    X, Y = load_wine(as_frame=True, return_X_y=True)
    #print(X)
    #print(Y) 
    print(X.info())
    features_name = X.columns
   
    model = KNeighborsClassifier(n_neighbors=3)

    # Forward feature selection
    sfs_forward = SFS(estimator = model
                    , k_features="best"
                    , forward=True      # True = forward selection, False = Backward Selection
                    , floating= False
                    , verbose = 0         # loggin level  
                    , scoring="accuracy"
                    , cv = 0
    )
    sfs_forward = sfs_forward.fit(X, Y)
    matrix = sfs_forward.get_metric_dict()

    best_features_names = sfs_forward.k_feature_names_
    best_features_idx = sfs_forward.k_feature_idx_
    cv_score = sfs_forward.k_score_
    print(f"best_features_names : {best_features_names}")
    print(f"best_features_idx : {best_features_idx}")
    print(f"cv_score : {cv_score}")

    df = pd.DataFrame.from_dict(matrix).T
    print(df)

    fig1= plot_sfs(matrix, kind="std_err")
    plt.title("Sequential Forward Selection : Wine Dataset")
    plt.grid()
    plt.show()

  

def backward_feature_selection():
    ##################################################################
    print("\n\n ------ Backward Feature Selection ----")
    # load data Iris_data
    X, Y = load_iris(as_frame=True, return_X_y=True)
    model = KNeighborsClassifier(n_neighbors=3)

    # Backwaord feature selection
    sfs_backward = SFS(estimator = model
                    , k_features="best"
                    , forward=False      # True = forward selection, False = Backward Selection
                    , floating= False
                    , verbose = 0         # loggin level  
                    , scoring="accuracy"
                    , cv = 0
    )
    sfs_backward = sfs_backward.fit(X, Y)

    matrix = sfs_backward.get_metric_dict()
    best_features_names = sfs_backward.k_feature_names_
    best_features_idx = sfs_backward.k_feature_idx_
    cv_score = sfs_backward.k_score_

    print(f"best_features_names : {best_features_names}")
    print(f"best_features_idx : {best_features_idx}")
    print(f"cv_score : {cv_score}")

    df = pd.DataFrame.from_dict(matrix).T
    print(df)

    fig1= plot_sfs(matrix, kind="std_err")
    plt.title("Sequential Backword Selection : Iris")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()