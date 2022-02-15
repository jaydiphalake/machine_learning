"""
Case Study : Play Predictor
   - Depending on [Weather] and [Temperature] condition, decide whether to play or not
  
  - Weather conditions are : Sunny, Overcast, Rainy
  - Temperature conditions are : Hot, Cold, Mild

"""

#############################################################

# Author        : Jayadip Halake
# Date          : 5-Feb-2022 

# ML Type       : Supervised Learning
# Classifier    : Knn (KNeighborsClassifier)
# DataSet       : Play Predictor
# Features      : Weather & Temperature
# Label         : Yes and No
# Training Dataset : 39 Entries
# Testing Dataset  : 1 Entry

#############################################################

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


def play_predictor(weather: str = 'Sunny', temperature: str = 'Hot'):
    # ----------------------------------------------------------
    # Step 1 : get the features and labels from data
    # 1.1 : Read csv
    csv_file = "PlayPredictor.csv"
    play_data_df = pd.read_csv(csv_file)

    # 1.2 create label encoder
    label_encoder = preprocessing.LabelEncoder()

    # 1.3 encode features and labels column and store encoding mapping
    play_data_df["weather_enc"] = label_encoder.fit_transform(play_data_df["Weather"])
    weather_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))

    play_data_df["temperature_enc"] = label_encoder.fit_transform(play_data_df["Temperature"])
    temperature_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))

    play_data_df["play_enc"] = label_encoder.fit_transform(play_data_df["Play"])
    play_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    #  print(play_data_df.head(n=5))

    # 1.4 Get encoded features (data) and labels (target)
    data = play_data_df[["weather_enc", "temperature_enc"]].values
    target = play_data_df["play_enc"].values

    # ----------------------------------------------------------
    # Step 2 : Algorithm
    classifier = KNeighborsClassifier(n_neighbors=3)

    # ----------------------------------------------------------
    # Step 3 : Train the algorithm 
    model = classifier.fit(data, target)

    # ----------------------------------------------------------
    # Step 4: Predict the result
    # 4.1 Get the encoded values of input 
    weather_test = weather_mapping.get(weather)
    temperature_test = temperature_mapping.get(temperature)

    # 4.2 Predict the result      
    play_result = model.predict([[weather_test, temperature_test]])

    # 4.3 decode the result
    result = get_key_from_value(play_mapping, play_result)

    return result


def get_key_from_value(data: dict, value):
    result = None

    for key, val in data.items():
        if val == value:
            result = key
            break
    return result


# Main Entry function
def main():
    print("\n---- Play Predictor by  Jayadip Halake : ")
    print("--- ML Type   : Supervised Learning ---- ")
    print("--- Algorithm : Knn (KNeighborsClassifier) ---- ")

    weather = "Rainy"
    temperature = "Mild"

    # get the values from user
    weather, temperature = get_user_input()

    # Predict Ball type
    result = play_predictor(weather, temperature)

    if result.lower() == 'yes':
        print(f"It seem you [CAN PLAY], As Weather is :{weather}] and Temperature is :[{temperature}]")
    else:
        print(f"It seem you [CAN NOT PLAY], as Weather is :[{weather}] and Temperature is :[{temperature}]")


# get the user input
def get_user_input():
    valid_weathers = ["Sunny", "Overcast", "Rainy"]
    valid_temp = ["Hot", "Mild", "Cool"]

    weather = input("Enter the Weather ( Sunny , Overcast or Rainy  ): ")
    temperature = input("Enter the Temperature ( Hot, Mild, Cool) : ")

    if weather not in valid_weathers:
        print("Invalid Weather. ")
        exit()

    if temperature not in valid_temp:
        print("Invalid temperature. ")
        exit()

    return weather, temperature


# Starter
if __name__ == "__main__":
    main()
