import pandas as pd

def main():
    print("\n Pandas Concat")
    play_with_contact()
    

def play_with_contact():
    print("\n\n --------------- play_with_contact  ----------------------- ")

    df1, df2, df3 = get_sample_data()
     
    print(df1)
    print(df2)
    print(df3)
    
    # Concat
    res = pd.concat([df1, df2])
    print("\n After concat : ")
    print(res)
    
    # Concat    
    print("\n After Reset Index")
    #Clear the existing index and reset it in the result by setting the ignore_index option to True.
    res = pd.concat([df1, df2], ignore_index=True)
    print(res)


    # concat : Column Name not matching
    print("\n concat : Column Name not matching : non-maching column will be NaN")
    res = pd.concat([df1, df3], ignore_index=True)
    print(res)
    
    # concat : horizantially 
    print("\n concat : horizantially ")
    res = pd.concat([df1, df2, df3], ignore_index=True, axis=1)
    print(res)
    
    

def get_sample_data():
    df1 = pd.DataFrame({
    "item": ["A", "B", "C", "D"],
     "value": [1,5 , 6 , 2]
    })
    df2 = pd.DataFrame({
    "item": ["A", "B", "D", "P"],
     "value": [11 , 15 , 16 , 12]
    })

    df3 = pd.DataFrame({
    "item": ["A", "B", "D", "P"],
     "quantity": [21 , 25 , 26 , 22]
    })    
    return df1, df2, df3

if __name__ == "__main__":
    main()
    
    