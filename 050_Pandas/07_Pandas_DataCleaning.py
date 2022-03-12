import pandas as pd
import numpy as np

def data_process():
    print("Hello Data cleaning")
    csv_path = "amazon_fires.csv"
    
    # csv contain Latin alphabet so use encoding to "ISO-8859-1"
    df = pd.read_csv(csv_path, encoding="ISO-8859-1")
    
    #print(df.tail())
    df = change_column_name_values_and_order(df)   
    #print(df.head())
    process_number_of_fires_columns(df)
    #print(df.head())
    
    # create copy of df : DataFrame.copy(deep=True)
    # When deep=True (default), a new object will be created with a 
    #        copy of the calling object’s data and indices. 
    # Modifications to the data or indices of the copy will not be
    #        reflected in the original object
    df_bkp = df.copy() 
       
    handle_missing_data(df)
    
    play_fillna()
   
    drop_column_row(df)
    
    #--------------------- Titanic age update -------
    print("\n\n --- Titanic Age processing ---")
    titanic_data = pd.read_csv("titanic.csv")
    #print(titanic_data.isna().sum())
  
    print("Before processing : Age Null :", titanic_data["age"].isna().sum())
    age_slice = titanic_data["age"].copy()
    min_age = age_slice.dropna().min()
    max_age = age_slice.dropna().max()
    age_null_cnt=age_slice.isna().sum()
    # generate range age values
    random_age = np.random.randint(low=min_age, high=max_age, size=(age_null_cnt))
    
    #
    age_slice[np.isnan(age_slice)] = random_age
    titanic_data["age"] = age_slice
    print("After processing : Age Null :", titanic_data["age"].isna().sum())
    
   
def drop_column_row(df):
    print("\n\n ---------- drop_column_row ----------------- ")
    
    df_drop=df.copy()
    
    # drop column
    print("\n Before column [date] drop :")
    print(df_drop.head())
    df_drop = df_drop.drop(columns='date')              # drop column
    #df_drop = df_drop.drop(columns=['date', 'month']) # drop multiple column
    #df_drop = df_drop.drop("date", axis=1)            # Axis =1 => columns
    
    print("\n After column [date] drop :")
    print(df_drop.head())
    
    # Drop row by index
    print( "\n Drop a row by index" )
    df_drop=df.copy()
    df_drop = df_drop.drop([1,2])
    print(" Row index 1, 2 are deleted, so it is not present in dataframe")
    print(df_drop.head()) # Row index 1, 2 are deleted, so it is not present in dataframe
    
    # Reindex (reset_index) the datafram
    print("\n After Reidex : df_drop.reset_index() ")
    df_drop = df_drop.reset_index()
    print(df_drop.head()) 
    
    # delete by filter
    df_drop=df.copy()

    
def play_fillna():
    print("\n\n ---------- play_fillna ----------------- ")
    # https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html 
    # Series.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
    # - method{‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None
    #         Method to use for filling holes in reindexed Series 
    #         pad / ffill: propagate last valid observation forward to next valid 
    #         backfill / bfill: use next valid observation to fill gap.
    #
    df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
    print(df)
    
    # Replace all NaN elements with 0s. 
    print("\n Replace all NaN elements with 0s.")
    print(df.fillna(0))
    
    # Replace all NaN elements : previous valid value.[ffill] 
    print("\n Replace all NaN elements : previous valid value.[ffill] ")
    print(df.fillna(method="ffill"))
    
    # Replace all NaN elements : Next valid value.[bfill] 
    print("\n Replace all NaN elements : Next valid value.[bfill] ")
    print(df.fillna(method="bfill"))
    
    # Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively
    print("\n Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively")
    default_values = {"A":0, "B":1, "C":3, "D":4}
    print( df.fillna(value=default_values) )
    
    # Only replace the first NaN element.
    print("\n  Only replace the first NaN element.")
    print( df.fillna(value=default_values, limit=1) )

    # Only replace valus using ANOTHER DATAFRAME
    # When filling using a DataFrame, replacement happens along the same column names and same indices
    print("\n  Only replace valus using another DATAFRAME : replacement happens along the same column names and same indices")
    df2 = pd.DataFrame( np.zeros((3,4)), columns=list("ABCE"))
    print(" Before datafrme :")
    print( df )
    print(" DataFrame (values) to copy from DF2 ")
    print(df2)
    print(" After datafrme copy :")
    print( df.fillna(value=df2) ) # Only matching column_names and row index will be copied. so [column D is NOT changed] and [Row =4 is NOT changes]

def handle_missing_data(df):
    print("\n\n ------------ handle_missing_data ---------")
    
    # identify null records
    print("\n Sum of missing value in each column")
    print(df.isnull())
    print(df.isnull().sum())
    
    # print null records
    print("\n print null records")
    print(df[df["number_of_fires"].isnull()])
    
    # replace null with 0
    print("replace null with 0")
    df.fillna(value =0 , inplace=True )   # inplace=True so values will be replaced in dataframe
    print(df.iloc[[68,110,127], :])   # [68,110,127] are index of Nan from previous print
    
    
    
    
def process_number_of_fires_columns(df):
    print("\n\n ---------------------- process_number_of_file_columns --------------------------")
    print("\n DF info :")
    print(df.info())
   
    # check if number_of_fires is numberic data only
    print("\n isnumeric : number_of_fires")
    print(df["number_of_fires"].str.isnumeric())
    
    print("\n Remove word fire from number_of_fires")
    # remove [Fires] from number_of_fires columns
    df["number_of_fires"] = df["number_of_fires"].str.strip(" Fires")
    print(df.head())
    
    

def change_column_name_values_and_order(df):
    print("\n\n ---------------------- change_column_name_values_and_order --------------------------")
    #print("\n Data :")
    #print(df.head())

    # Rename the columns
    print(df.columns)
    new_columns_names = {
        "ano":"year",
        "mes":"month",
        "estado":"state",
        "numero":"number_of_fires",
        "encontro":"date"
    }
    df.rename(columns=new_columns_names, inplace=True)
    #print("\n After column Rename :")
    #print(df.head())
    
    # change column order
    column_new_order=["year","month", "date", "state","number_of_fires"]
    df.reindex(columns = column_new_order)
    
    # re-arrange by colummn index
    #new_order = [0,1,4,2,3]
    #df = df[df.columns[new_order]]
    
    print("\n After column order change")
    print(df.head())
    
    # column values
    print("\n month column values :" , df["month"].unique()) 
    
    month_value_map = {"Janeiro": "January",  "Fevereiro": "February", "Março": "March",
    "Abril": "April", "Maio": "May", "Junho": "June", "Julho": "July",
    "Agosto": "August", "Setembro": "September", "Outubro": "October",
    "Novembro": "November", "Dezembro": "December"}
    
    print("\n After replancing month values :  df[\"month\"] = df[\"month\"].map(month_value_map)" )
    
    df["month"] = df["month"].map(month_value_map)
    print("\n month column values :" , df["month"].unique()) 
    print(df.head())
    
    return df;
    
    
    
    

def main():
    data_process()
    
if __name__ == "__main__":
    main()
    