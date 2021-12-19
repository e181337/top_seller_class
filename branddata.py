from getdata import getData

class brandData(getData):
            
    def get_grouped_output(self):
        temd_df = self.df.groupby('brand')['quantity'].sum().reset_index()
        print("-- top seller brand--")
        return self.get_store_ids(temd_df, self.n)