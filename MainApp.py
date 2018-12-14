import pandas as pd
from collections import Counter


def main_app():

    df = pd.read_csv('Data.csv')
    dict_df = df.to_dict('index')

    list_of_employees = [x['Employee'] for x in dict_df.values()]
    x = Counter(list_of_employees)
    list_x = sorted(x.items(), key=lambda t: t[1], reverse=True)

    print(f'Name                      - Times record change')
    print('_________________________________________________\n')
    for key, item in list_x:
        print(f'{key:25} - {item}')

if __name__ == '__main__':

    

