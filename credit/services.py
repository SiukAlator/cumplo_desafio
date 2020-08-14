import requests
import datetime

def generate_request(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return ''
    

def get_TMC(params={}):
    a_date = (str(params['date'])).split('-')
    api_key = '9c84db4d447c80c74961a72245371245cb7ac15f'
    #Solo existe data del mes anterior al presente mes
    today = datetime.datetime.today()
    # print('mes:', today.month)
    if (int(a_date[1]) >= today.month):
        a_date[1] = str(today.month -1)
    url = 'https://api.sbif.cl/api-sbifv3/recursos_api/tmc/'+a_date[0]+'/'+a_date[1]+'?apikey='+api_key+'&formato=json'
    response = generate_request(url)
    if response:
        TMCs = response.get('TMCs')
        return TMCs

    return ''