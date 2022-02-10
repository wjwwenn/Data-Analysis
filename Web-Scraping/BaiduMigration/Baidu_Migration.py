import requests
import time
import pandas as pd
import datetime

# Baidu migration direction 0 Move in, 1 Move out
MOVE = ('move_in', 'move_out')
"""
structure 10 A city name and code
The code can be found in the Ministry of Civil Affairs , Connection address http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html
The above connection is 2019 year 11 Code of administrative division above county level of the people's Republic of China in May
"""
CITY = {' Beijing ': '110000',
' Shanghai ': '310000',
' Guangzhou ': '440100',
' Shenzhen ': '440300',
' Chengdu ': '510100',
' tianjin ': '120000',
' nanjing ': '320100',
' Hangzhou ': '330100',
' Chongqing ': '500000',
' wuhan ': '420100'}

def get_data_from_url(url):
    print(' request http data ', url)
    resp = requests.get(url, timeout=5)
    j = resp.json()

    if j['errmsg'] == 'SUCCESS':
        data_list = j['data']['list']
        return data_list
    else:
        print(' Request for server data failed !')
    return None

def get_data(city_code, direction, date):
    if city_code is None:
    # Get the current national popular immigration information according to the date / Move out of the city
        url_nation = f'http://huiyan.baidu.com/migration/cityrank.json?dt=country&id=0&type={direction}&date={date}'
        return get_data_from_url(url_nation)
    else:
                # Get the immigration information of the current city according to the city code and date / Move out data
        url_city = f'http://huiyan.baidu.com/migration/cityrank.json?dt=city&id={city_code}&type={direction}&date={date}'
    return get_data_from_url(url_city)

def get_date(year, month, day):
    d = datetime.date(year, month, day)
    return d.__format__('%Y%m%d')

def main():
    # Splice a specific date , Specific date
    date = get_date(2022, 1, 17)
    # Get the given date 、 The city of a given city code moves into / Move out data
    data = get_data(city_code=CITY[' Beijing '], direction=MOVE[0], date=date)
    df = pd.DataFrame(data=data, columns=['city_name', 'province_name', 'value'])
    df.to_excel('1.xls', encoding='utf-8') # Data writing excel file
    print(df)
    time.sleep(3)
    # Get the national popular cities moving in on a given date / Move out data
    data = get_data(city_code=None, direction=MOVE[0], date=date)
    df = pd.DataFrame(data=data, columns=['city_name', 'province_name', 'value'])
    df.to_excel('2.xls', encoding='utf-8') # Data writing excel file

if __name__ == '__main__':
    main()
