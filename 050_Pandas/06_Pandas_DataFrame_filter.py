import pandas as pd

def play_with_dataframe():
    print("Pandas data frame")
     
    csv_path = "titanic.csv"
    # read csv 
    df = pd.read_csv(csv_path)
    
    # examining the dataframe / dataframe info     
    # examine_dataframe(df)
    
    # df.loc[row_label, column_label]
    # loc : LABEL based selection
    #slicing_loc(df)
    
    # iloc : Integer Position based selection
    # df.loc[row_index, column_index]
    #slicing_iloc(df)

    
    # df.[Single column] = Series
    # df.[multiple column] = Dataframe
    #df_more(df)
    
    # filter data
    # a & b (pandas) = a and b (python)
    # a | b (pandas) = a or b (python)
    df_filter_data(df)
    

def df_filter_data(df):
     print("\n\n -------------filter the data : [a & b (pandas) = a and b (python)] ------- [a | b (pandas) = a or b (python)]------------------- ")
     print(df.head())
     
     print("\n Filter data => where pclass is 1")
     is_class_1 = (df["pclass"] == 1)
     print(is_class_1)
     print("")
     df_class_1 = df [ is_class_1] # df_class_1 = df [ df["pclass"]== 1 ]
     print(df_class_1)
     
     print("\n Filter data => where age is greater than 60")
     df_age_over_60 = df [ df["age"] > 60 ]
     print(df_age_over_60)
     
     print("\n Filter data => where age is less 60 AND pclass is 1")
     under_60_pclass_1 = (df["pclass"] == 1) & ( df["age"] > 60  )
     df_under_60_pclass_1 = df [under_60_pclass_1 ]
     print(df_under_60_pclass_1)
     
     print("\n Filter data => where age > 60 OR age < 5")
     over_60_under_5 = (df["age"] > 65) | (df["age"] < 5) 
     df_under_60_pclass_1 = df [over_60_under_5 ]
     print(df_under_60_pclass_1)
     
     print("\n Null check")
     print(df.isnull())

     print("\n Null check : for column : Cabin Null")
     cabin_null = df["cabin"].isnull()
     print(df [ cabin_null])
     
     print("\n NOT Null check - for column : Cabin NOT Null")
  
     print(df [  df["cabin"].notnull()])

def df_more(df):
    print("\n\n -------------df.[Single column] = Series ------------------- ")
     
    print("\n select one column")
    series_age = df["age"]
    print(type(series_age))
    print(series_age)
    
    
    print("\ dataframe of columns")
    df_name_cabin=df[["name", "cabin"]]
    print(type(df_name_cabin))
    print(df_name_cabin)


def slicing_iloc(df):    
    print("\n\n ------------- iloc : Integer Position based selection => df.loc[row_index, column_index] ------------------- ")
    print("\n Top rows : df.head()")
    print(df.head())
    
    print("\n get value of first column at index 4 =>  df.iloc[1, 4] ")
    print( df.iloc[4, 1])
    
    print("\n Slicing an entire column at index 1  =>  df.iloc[:, 1] ")
    print(df.iloc[:, 1] )
    #print(df.iloc[:, -3] )
    
    #  Slicing a row / get rows value at index 
    print("\n Slicing a row    =>  df.iloc[25] ")
    print( df.iloc[25] )
    #print( df.iloc[25, :] )
    
    df_name_sex_age = df.iloc[10:20, 1:4]
    print(type(df_name_sex_age))
    print(df_name_sex_age)
    

def slicing_loc(df):
    print("\n\n ------------- loc : LABEL based selection => df.loc[row_label, column_label] ------------------- ")

    print("\n Top rows : df.head()")
    print(df.head())

    # df.loc[row_label, column_label]    
    print("\n get value of column [name] at index 1 =>  df.loc[1, 'name'] ")
    print( df.loc[1, "name"])

    
    # get all values of column / Slicing an entire column
    print("\n Slicing an entire column  =>  df.loc[:, 'name'] ")
    print(df.loc[:, "name"] )
    
    """
    names =  df.loc[20:30, "name"]
    print( names)
    print( names.head())
    """

    #  Slicing a row / get rows value at index 
    print("\n Slicing a row    =>  df.loc[25, :] ")
    print( df.loc[25, :] )
    # print( df.loc[25] )

    print("\n select specifice rows and columns")
    df_name_sex_age = df.loc[10:20, "name":"age"]
    print(df_name_sex_age)

    

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
    
    