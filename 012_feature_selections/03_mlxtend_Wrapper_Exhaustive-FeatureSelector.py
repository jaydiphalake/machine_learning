"""
Wrapper Type- Exhaustive Feature Selection
    - This is MOST ROBUST feature selectio  method
    - It tries every possible combination of varaible and return best performing subset
    - Its heavy and time consuming ( as all the possible combination has to check)

http://rasbt.github.io/mlxtend/user_guide/feature_selection/ExhaustiveFeatureSelector/

"""

##############################################################################

# Author                 : Jayadip Halake
# Date                   : 5-Mar-2022
# Feature Selection Type : Wrapper Methods
# Methods                : Exhaustive Feature Selection
##############################################################################


from matplotlib import pyplot as plt
import pandas as pd
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import  load_iris, load_wine
from mlxtend.plotting  import plot_sequential_feature_selection as plot_sfs

# Main Entry function
def main():
    print("\n---- Feature Selection : Jayadip Halake : ")
    print("--- Type : Wrapper Methods---- ")
    print("--- Techniques : Exhaustive Feature Selection ---- ")
    
    exhus_feature_selection()



def exhus_feature_selection():
    # load data
    X, Y = load_wine(as_frame=True, return_X_y=True)
    #print(X)
    #print(Y) 
    print(X.info())
    features_name = X.columns
   
    model = KNeighborsClassifier(n_neighbors=3)

    # Forward feature selection
    efs = EFS(estimator=model
            ,min_features=1, max_features=7
            ,scoring="accuracy"
            ,cv=2
            , print_progress=True
            , n_jobs = -1         # CPU count. -1= all CPU
             )

    efs = efs.fit(X, Y)
    matrix = efs.get_metric_dict()

    best_features_names = efs.best_feature_names_
    best_features_idx = efs.best_idx_
    best_score = efs.best_score_
    print(f"\n best_features_names : {best_features_names}")
    print(f"\n best_features_idx : {best_features_idx}")
    print(f"\n cv_score : {best_score}")

    df = pd.DataFrame.from_dict(matrix).T
    df.sort_values("avg_score", inplace=True, ascending=False)
    print(df)



if __name__ == "__main__":
    main()