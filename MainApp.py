import pandas as pd
from collections import Counter

with open('Api_key.txt', 'r') as file_key:
    key_api = file_key.read()
CODE = 51


def get_data(start_date, end_date):

    ''' this grap the data from the website and download as a csv file and upload it in to a pandas dataframe'''

    raw_data = f"https://api.mytimestation.com/v0.1/reports/?api_key={key_api}" \
        f"&Report_StartDate={start_date}&Report_EndDate={end_date}&id={CODE}&exportformat=csv"
    csv_data = pd.read_csv(raw_data)
    return csv_data


def main_app(df):

    ''' we use this function to analise and re-organize the information of the provide by the get_data '''

    dict_df = df.to_dict('index')
    list_of_employees = [x['Employee'] for x in dict_df.values()]
    x = Counter(list_of_employees)
    list_x = sorted(x.items(), key=lambda t: t[1], reverse=True)

    print(f'Name                      - Times record change')
    print('_________________________________________________\n')
    for key, item in list_x:
        print(f'{key:25} - {item}')


if __name__ == '__main__':

    start = input('[+] - Start date (yyyy-mm-dd) --> ')
    end = input('[+] - End date (yyyy-mm-dd) --> ')

    raw_data = get_data(start_date=start, end_date=end,)
    main_app(df=raw_data)




