from getdata import getData

class productData(getData):
            
    def get_grouped_output(self):
        temd_df = self.df.groupby('name')['quantity'].sum().reset_index()
        print("-- top seller product --")
        return self.get_store_ids(temd_df, self.n)

        
    