import pandas as pd


def pd_series():
    a = [1,4,3,5,2, 9,1,-11, 3]
    print(a)
    print(type(a)) # Type is list
    
    # convert list into pandans series
    # Seiries is single dimentsion COLUMN of data
    a = pd.Series(a)
    print(f"Seiries type : {type(a)}")
    print(a)
  
    
    # get value at index
    print("\n get the value at index : a[2]")
    print(a[2])
    
    # get first 3 values    
    print("\n first 3 value : a[:3]")
    print(a[:3])
    
    # values from index 2
    print("\n values from index 2 : a[2:]")
    print(a[2:])
    
    # value is present
    print("\n values is present : 1 in a")
    print(f"1 in a : {1 in a} ")
    print(f"10 in a : {10 in a} ")
      
    # get min
    print(f"\n min value : {a.min()}")
    
    # get max
    print(f"\n Max value : {a.max()}")
    
    # get the frequency of values
    print("\n Frequency of values : value_counts()")
    print(a.value_counts())
    
     # get the unique 
    print("\n unique values : unique()")
    print(a.unique())
      
    
    # pd_sorting(a)
    
    

def pd_sorting(a):
    # sort values Ascending
    print("\n Sort the value : sort_values()")
    print(a.sort_values())
    
    print("\n sort_values() will not change the acutal series ")
    print(a)

    # sort values Descending
    print("\n Sort the Decending  : sort_values( ascending=False )")
    print(a.sort_values(ascending=False))
    
    
    # sort the values in ASC series and save it
    print("\n Sort the value and SAVE in series : a.sort_values(ascending=True, inplace=True)")
    a.sort_values(ascending=True, inplace=True)
    print(a)

def main():
    pd_series()


if __name__ == "__main__":
    main()