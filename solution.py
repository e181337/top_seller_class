import argparse
from getdata import getData
from sellerdata import sellerData
from productdata import productData
from branddata import brandData
from citydata import cityData


def get_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min-date', dest='min_date', type=str, default='2020-01-01')
    parser.add_argument('--max-date', dest='max_date', type=str, default='2020-06-30')
    parser.add_argument('--top', dest='top', type=int, default=3)
    args = parser.parse_args()
    print("min_date: " + args.min_date)
    print("max_date: " + args.max_date)
    print("top: " + str(args.top))
    return args
    
def main():
    args = get_inputs()
    data_class = getData(args.top, args.min_date, args.max_date)
    productData.get_grouped_output(data_class)
    sellerData.get_grouped_output(data_class)
    brandData.get_grouped_output(data_class)
    cityData.get_grouped_output(data_class)


 
if __name__ == '__main__':
    main()
