import pandas as pd

def play_with_dataframe():
    print("Pandas data frame")
     
    csv_path = "titanic.csv"
    # read csv 
    df = pd.read_csv(csv_path)
    
    # print top rows
    print("\n Top 10 rows : df.head(10)")
    print(df.head(10))
   

def main():
    play_with_dataframe()
    
if __name__ == "__main__":
    main();
    
    