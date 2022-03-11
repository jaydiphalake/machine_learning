import pandas as pd 
import numpy as np


def main():
    print("Hello")
    df = get_amazon_fire_data()
    print(df.head())
    # Aggregation using Group by
    # play_with_groupby(df)
    
    df = get_amazon_fire_data()
    # Aggregation using dataframe -> Pivot
    play_with_pivot(df)

def play_with_groupby(df):
    print("\n\n --------- play_with_groupby --------")
    
    state_groups = df.groupby("state")
    print("Print Group by : size")
    print(state_groups.size())
    
    print("\n Group by state : number_of_fires mean")
    df_agg = df.groupby("state")['number_of_fires'].agg(np.mean)  
    # group by Single column  df.groupby("state") ==> Series 
    print(type(df_agg))
    
    ## Aggregate Multiple functions
    df_agg = df.groupby("state")['number_of_fires'].agg([np.mean, np.max])
    print(df_agg)
    
    ## Group by multiple columns
    # group by Multiple column  df.groupby(["state", "month"]).. ==> DataFrame 
    df_agg = df.groupby(["state", "month"])["number_of_fires"].agg([np.mean, np.max])
    print(df_agg)
    print(type(df_agg))
    
    # using custom aggregate function
    print("\n custom Aggregate function")
    df_agg = df.groupby("state")["number_of_fires"].agg(my_custom_agg_fn)
    print(df_agg)
    
    # Convert series to dataframe
    print("\n Convert series to dataframe")
    df_agg = df.groupby("state")["number_of_fires"].agg(my_custom_agg_fn)
    print(type(df_agg))
    df_new = pd.DataFrame(df_agg).reset_index()
    print(type(df_new))
    print(df_new.head())
    
def my_custom_agg_fn(grouped_data):
        return (grouped_data.max() - grouped_data.min())

def play_with_pivot(df):
    print("\n\n --------- play_with_groupby --------")
    df_agg = df.pivot_table(index="state", values="number_of_fires" , aggfunc=np.mean )
    print(df_agg)

    # PIVOT multiple column + multiple aggregate function
    print("\n pivot multiple column + multiple aggregate function")
    df_agg = df.pivot_table(index=["state", "month"], values="number_of_fires" 
            , aggfunc = [np.mean, np.min]   )    
    print(df_agg)
    


def get_amazon_fire_data():
    csv_path= "amazon_fires.csv"
    df = pd.read_csv(csv_path, encoding="ISO-8859-1")

    new_columns_names = {
        "ano":"year",
        "mes":"month",
        "estado":"state",
        "numero":"number_of_fires",
        "encontro":"date"
    }
    df.rename(columns = new_columns_names, inplace=True)
    reindex_column=["year", "month", "date", "number_of_fires", "state"]
    df = df.reindex(columns=reindex_column)
    
    # convert month to english
    month_value_map = {"Janeiro": "January",  "Fevereiro": "February", "Março": "March",
    "Abril": "April", "Maio": "May", "Junho": "June", "Julho": "July",
    "Agosto": "August", "Setembro": "September", "Outubro": "October",
    "Novembro": "November", "Dezembro": "December"}
    
    df["month"].replace(month_value_map, inplace=True)
    
    # remove fire word from [number_of_fires] 
    df["number_of_fires"] = df["number_of_fires"].str.strip(to_strip=" Fires")
    df["number_of_fires"] = df["number_of_fires"].astype(float)
    
    # replace null with 0
    #print(df.isna().sum())
    df.fillna(0, inplace=True)
    # print(df.isna().sum())
    
   
    
    return df

    

if __name__ == "__main__":
    main()