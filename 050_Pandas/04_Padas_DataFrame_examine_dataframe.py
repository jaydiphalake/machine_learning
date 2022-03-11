import pandas as pd

def play_with_dataframe():
    print("Pandas data frame")
     
    csv_path = "titanic.csv"
    # read csv 
    df = pd.read_csv(csv_path)
    
    # examining the dataframe / dataframe info     
    examine_dataframe(df)
    

def examine_dataframe(df):
     # print top rows
    print("\n Top 10 rows : df.head(10)")
    print(df.head(10))
    
    # print bottom rows
    print("\n bottom 10 rows : df.tail(10)")
    print(df.tail(10))
    
    # dataframe column info
    print("\n dataframe column info : df.info()")
    print(df.info())
    
    # describe the data : Summary statictis of data (numeric columns)
    print("\n Summary statictis of data (numeric columns) : df.describe()")
    print(df.describe())
    
    # column types
    print("\n column tupes : df.dtypes ")
    print(df.dtypes)
    
    # column names
    print("\n column names : df.columns ")
    print(df.columns)
    #df_columns = df.columns
    #print(df_columns)
    #for a in df_columns:
        #print(a)
        
    # describe column
    print("\n Desciribe columns : df['ticket'].describe() ")
    print( df["ticket"].describe() )
    
def main():
    play_with_dataframe()
    
if __name__ == "__main__":
    main();
    
    