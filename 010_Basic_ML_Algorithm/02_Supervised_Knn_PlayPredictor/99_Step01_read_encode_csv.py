import pandas as pd
from sklearn import preprocessing

def main():
    # Step 1 : Get the data from CSV
    csv_file = "PlayPredictor.csv"
    play_data_df = pd.read_csv(csv_file);

    # print top 5 entries
    print("\n Top 5 rows in CSV")
    print(play_data_df.head(n=5))
    

    # Step 2 : Encode
    # Encode [Weather], [Temperature], [Play] column
    # for Encoding, use sklearn.preprocessing.LabelEncoder -> fit_transform

    label_encoder = preprocessing.LabelEncoder()
   
    #encode [Weather] column and append the result as [weather_enc] in data frame  [play_data_df]
    play_data_df["weather_enc"] = label_encoder.fit_transform(play_data_df["Weather"])
    
    # store encoding mapping
    weather_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    print(f"\n weather_mapping---{weather_mapping}")
    
    input_weather = "Sunny"
    encoded_input_weather = weather_mapping.get(input_weather)
    decoded_input_weather =  get_key_from_value(weather_mapping, encoded_input_weather)
    print(f" weather = {input_weather},  Encoded  = { encoded_input_weather }, decoded = {decoded_input_weather} ")

    
    
    play_data_df["temperture_enc"] = label_encoder.fit_transform(play_data_df["Temperature"])
    temperture_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    
    play_data_df["play_enc"] = label_encoder.fit_transform(play_data_df["Play"])
    play_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    
    #print top 5 entries and check encoded columns weather_enc, temperture_enc, play_enc
    print("\n Printing top 2 records. Encoded columns are also present")
    print(play_data_df.head(n=5))
    
    
    
    features = play_data_df[ ["weather_enc", "temperture_enc"]]
    labels = play_data_df[ ["play_enc"]]
    print(f"\n features = {features}")
    print(f"\n labels = {labels}")
    
    return features, labels


def get_key_from_value(data: dict, value):
    result = None

    for key, val in data.items():
        if val == value:
            result = key
            break
    return result


# Starter
if __name__ == "__main__":
    main()
