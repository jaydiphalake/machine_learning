import pandas as pd

def play_with_dataframe():
    print("Pandas data frame")

    list_a = [1, 5, 6, 7, 9, "a", "b", "c"]
    print(f"\n list_a : {list_a}")
    
    df_a = pd.DataFrame(list_a)
    print("\n data frame from list :   pd.DataFrame(list_a)")
    print(df_a)
    
    print("\n dataframe from Dictonary ")
    dict_b = {
        "city" : ["tokyo", "mumbai", "NY", "London"],
        "country": ["Japan", "India", "US", "UK"]
    }
    # print(dict_b)
    df_b= pd.DataFrame(dict_b)
    print(df_b)

def main():
    play_with_dataframe()
    
if __name__ == "__main__":
    main();
    
    