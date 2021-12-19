import pandas as pd

class getData:

### get merged data
    def __init__(self, n, date_min, date_max):
        ### import data
        data_sales = pd.read_csv('sales.csv', parse_dates=['date'])
        data_product = pd.read_csv('product.csv')
        data_store = pd.read_csv('store.csv')
        
        ### rename columns      
        data_product.columns = ['product', 'name', 'brand']
        data_store.columns = ['store', 'store_name', 'city']
        
        ### join df to generate single df
        df_master = data_sales.merge(data_product, how='inner', left_on=['product'], right_on=['product'])
        df_master = df_master.merge(data_store, how='inner', left_on=['store'], right_on=['store'])
        self.df = df_master.copy()    
        self.df = self.df[(self.df.date >= date_min) & (self.df.date <= date_max)]
        self.n = n
    
    @staticmethod
    def get_store_ids(df, n):    
        print(df[df['quantity'] >= list(df.sort_values(by='quantity', ascending=False).quantity.unique())[n-1]].sort_values(by='quantity', ascending=False).sort_values(by='quantity', ascending=False, ignore_index=True))
       