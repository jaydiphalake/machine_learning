
"""
Case Study : Iris Dataset with K-Mean algotithm
            - Use Elbow method to identify number of cluster

API : https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
"""

#############################################################

# Author        : Jayadip Halake
# Date          : 19-Feb-2022

# ML Type       : Un-Supervised Learning
# Classifier    : K-Mean
# DataSet       : sklearn.datasets -> iris

#############################################################

from matplotlib import pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


def iris_kmean():
    # Load the data set
    dataset = load_iris()
    x = dataset.data[:, :4]
    print(type(x))
    print("target_names : ", dataset.target_names)
    print("feature_names : ", dataset.feature_names)

    # find the optimum number of clusters
    k_range = range(1, 11)
    # inertia = Sum of squared distances of samples to their closest cluster center, 
    k_inertia = []
    for k in k_range:
        k_model = KMeans(n_clusters=k, max_iter=300, random_state=0)
        k_model.fit(x)
        k_inertia.append(k_model.inertia_)

    # plot the k_inertia result on line-graph, and observe "The Elbow"
    draw_elbow(k_inertia)
    
    # Cluster = 3 are ideal cluster count
    model = KMeans(n_clusters=3, random_state= 0, max_iter=300)
    y_kmean = model.fit_predict(x)

    draw_clusters(x, y_kmean, model)

def draw_clusters(x_df, y_kmean, model :KMeans):
    plt.figure()
    plt.xlabel("sepal length (cm)")
    plt.ylabel("sepal width (cm)")
    plt.title("Iris : Clusters")

    # first cluster y_kmean =0
    # get the [y_kmean =0] records index
    y_arr = y_kmean==0
    x = x_df[y_arr, 0] # sepal length (cm)
    y = x_df[y_arr, 1] # sepal width (cm)
    color="gray"
    label ="Iris-Sentosa"
    plt.scatter(x=x, y=y, c=color, label=label)

    # Second cluster y_kmean =1
    x = x_df[y_kmean==1, 0]
    y = x_df[y_kmean==1, 1]
    color="blue"
    label ="Iris-versicolour"
    plt.scatter(x=x, y=y, c=color, label=label)

    # Third cluster y_kmean =2
    x = x_df[y_kmean==2, 0]
    y = x_df[y_kmean==2, 1]
    color="green"
    label ="Iris-virginica"
    plt.scatter(x=x, y=y, c=color, label=label)

    # Plot the centroids of cluster
    x= model.cluster_centers_[:,0]
    y = model.cluster_centers_[:,1]
    color="red"
    label ="Centroids"
    plt.scatter(x=x, y=y, c=color, label=label)
   
    plt.legend()
    plt.show()
    

def draw_elbow(k_inertia : list):
    plt.plot(k_inertia)
    
    plt.title("The Elbow Method")
    plt.xlabel("Number Of Cluster")
    plt.ylabel("inertia : Within Cluster sum Square")

    plt.show()



# Main Entry function
def main():
    print("\n---- Iris Case Study : Jayadip Halake : ")
    print("--- ML Type   : Un-Supervised Learning ---- ")
    print("--- Algorithm : K-Mean ---- ")
    iris_kmean()


if __name__ == "__main__":
    main()