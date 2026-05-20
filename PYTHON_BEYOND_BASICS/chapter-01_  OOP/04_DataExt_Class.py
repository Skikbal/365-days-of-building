import pandas as pd
class DataEXt:
    
    def __init__(self,file_path:str):
        self.file_path = file_path
        
# it can read both csv and tsv
    def fetch_text(self,separator:str=","):
        # write ur custome logic
        df = pd.read_csv(self.file_path,sep=separator)
        print("\n print original data")
        print(df.head())
        
        # transformation
        df["TotalPrice"] = df["Quantity"] * df["Price"]
        print("\n print transformed data")
        print(df.head())
        return df
    def fetch_json(self):
        # write ur custom logic
        df = pd.read_json(self.file_path)
        print("\n print original data")
        print(df.head())
        
        df["CustomerName"] = df["CustomerName"].str.upper()
        print("\n print transformed data")
        print(df.head())
        return df
    def fetch_parquet(self):
        df = pd.read_parquet(self.file_path)
        print("\n print original data")
        print(df.head())
        df["OrderDate"] = pd.to_datetime(df["OrderDate"])
        print("\n print transformed data")
        print(df.head())
        return df


obj = DataEXt("chapter-01_  OOP/files/orders.csv")
data = obj.fetch_text(",")
print(data)

obj1 = DataEXt("chapter-01_  OOP/files/orders.json")
data1 = obj1.fetch_json()
print(data1)

obj2 = DataEXt("chapter-01_  OOP/files/orders.parquet")
data2 = obj2.fetch_parquet()
print(data2)