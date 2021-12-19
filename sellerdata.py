from getdata import getData

class sellerData(getData):
    
    def get_grouped_output(self):
        temd_df = self.df.groupby('store_name')['quantity'].sum().reset_index()
        print("-- top seller store --")
        #self.df = temd_df
        return self.get_store_ids(temd_df, self.n)
        
    