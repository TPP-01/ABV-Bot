import json
import requests


RKI_URL = "https://api.corona-zahlen.org/germany"

def get_daily_data():
    '''Returns the daily Corona data for Germany
    '''
    r = requests.get(RKI_URL)
    data = json.loads(r.text)
    delta = data.get('delta', {})
    delta['weekIncidence'] = data.get('weekIncidence', None)
    return(delta)

# import rki
# data = rki.get_daily_data()

if __name__ == '__main__':
    data = get_daily_data()
    print(f'Neue Fälle DE: {data.get("cases")}')
    print(f'Neue Todesfälle DE: {data.get("deaths")}')
    print(f'7-Tages-Inzidenz DE: {data.get("weekIncidence"):.2f}')

