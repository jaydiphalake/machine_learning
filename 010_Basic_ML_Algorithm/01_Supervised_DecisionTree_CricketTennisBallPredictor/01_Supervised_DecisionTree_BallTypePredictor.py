"""
Case Study
  - Data contain two types of ball : [Tennis] and [Cricket]
  - Ball can be identified based on [Weight] and [Surface]
  
  - From given [Weight] and [Surface], identify type of ball (Cricket or Tennis)
"""

#############################################################

# Author : Jayadip Halake
# Date   : 1-Feb-2022

# Classifier    : Decision Tree
# DataSet       : Ball Data
# Features      :  Weight & Surface
# Label         : Tennis and Cricket
# Training Dataset : 15 Entries
# Testing Dataset  : 1 Entry

#############################################################

from sklearn import tree


def ball_predictor(weight: int = 40, surface: int = 1):
    print("---")
    # Step 1 : get the data
    balls_feature, balls_name = get_data()
    # print(f"balls_feature :-  {balls_feature}")
    # print(f"balls_name :-  {balls_name}")

    # Step 2 : Algorithm
    dec_tree = tree.DecisionTreeClassifier()

    # Step 3 : Train the algorithm 
    # [fit] method is used to train the algorithm
    dec_tree_model = dec_tree.fit(balls_feature, balls_name)

    # Step 4: Predict the result
    result = dec_tree_model.predict([[weight, surface]])

    return result


# Main Entry function
def main():
    print("\n---- Cricket or Tennis Ball Predictor by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Decision tree ---- ")

    weight = 40
    surface = 1  # surface 1 = Rough , 0 = Smooth

    # get the values from user
    weight, surface = get_user_input()

    # Predict Ball type
    result_ball_type = ball_predictor(weight, surface)
    # print(f"--result_ball_type-- {result_ball_type}")

    # 1 = Tennis,  2=Cricket
    if result_ball_type == 1:
        print("Ball Look like a : Tennis Ball")
    elif result_ball_type == 2:
        print("Ball Look like a : Cricket Ball")


def get_user_input():
    weight = int(input("Enter the Ball Weight : "))
    surface_str = input("Enter the surface Smooth or Rough : ")
    surface = 0
    if surface_str.lower() == "rough":
        surface = 1
    elif surface_str.lower() == "smooth":
        surface = 0
    else:
        print("Invalid Surface..")
        exit()

    return weight, surface


def get_data():
    # Step 1 : Get the data
    # Currently data is hardcoded. It can be read from csv or excel
    # Algorithm function [Fit] and [predict] function, accept only integer or float, so convert data into numbers
    # As this is first Algorithm so will do it manually. Later will use inbuilt function to get and coded the data

    # ball weight and type of surface
    balls_features_raw = [
        [35, "Rough"], [47, "Rough"], [90, "Smooth"], [48, "Rough"], [90, "Smooth"], [35, "Rough"], [92, "Smooth"]
        , [40, "Rough"], [35, "Rough"], [40, "Rough"], [96, "Smooth"], [43, "Rough"], [110, "Smooth"], [35, "Rough"]
        , [95, "Smooth"]
    ]

    # Output (Ball Type) for each feature
    balls_name_raw = [
        "Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket"
        , "Tennis", "Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis"
        , "Cricket"
    ]
    print(f"balls_features_raw :-  {balls_features_raw}")
    print(f"balls_name_raw :-  {balls_name_raw}")

    # Step 2 : encode the data. 

    # "Rough" to 1  and "Smooth" = 0
    # in balls_features_raw replace "Rough"  with 1 and "Smooth" with 0
    balls_features = [
        [35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0]
        , [40, 1], [35, 1], [40, 1], [96, 0], [43, 1], [110, 0], [35, 1]
        , [95, 0]
        ]
    # 1 = Tennis,  2=Cricket
    # in balls_name_raw replace "Tennis"  with 1 and "Cricket" with 2
    balls_name = [
        1, 1, 2, 1, 2, 1, 2
        , 1, 1, 1, 2, 1, 2, 1
        , 2]
    return balls_features, balls_name


# Starter
if __name__ == "__main__":
    main()
