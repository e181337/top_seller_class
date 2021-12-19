from getdata import getData

class cityData(getData):
            
    def get_grouped_output(self):
        temd_df = self.df.groupby('city')['quantity'].sum().reset_index()
        print("-- top seller city --")
        return self.get_store_ids(temd_df, self.n)

        
    