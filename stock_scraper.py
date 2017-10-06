import csv
import requests

URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"

def get_data():
    r = requests.get(URL)
    data = r.text
    results = {'children':[]}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        results['children'].append({
            'name': line['Name'],
            'symbol': line['Symbol'],
            'price': line['lastsale'],
            'net_change': line['netchange'],
            'percent_change': line['pctchange'],
            'volume': line['share_volume'],
            'value': line['Nasdaq100_points']
        })
    return results