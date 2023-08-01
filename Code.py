import requests
from datetime import datetime

def get_weather_data():
    API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return None



def convert_date(timestamp_str):
    date = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

    # Format the datetime object to "dd/mm/yyyy" format
    formatted_date = date.strftime('%d/%m/%Y')
    
    return formatted_date

def process_dates(data):
    list_data = data
    date_dict = {}
    start_idx = -9999
    for idx,record in enumerate(list_data):
        if start_idx == -9999:
            start_idx = idx
            
        date_in_seconds = convert_date(record.get('dt_txt'))
        date_dict[date_in_seconds] = (start_idx,idx)
    return date_dict
     
def get_data_func(data):
    list_data = data
    key = input("Press any key 1,2,3 to continue or 0 to terminate ")
    date_dict = process_dates(list_data)
    while True:
        
        if key == '1':
            date = input("Enter input in DD/MM/YYYY format ")
            idx = date_dict.get(date,-1)
            
            while idx == -1:
                print("Enter another date ")
                key = input()
            else:
                for i in range(idx[0],idx[1]):
                    summ = list_data[i].get('main').get('temp')
                print(f'Average temperature for the day : {summ/(idx[1]+1)}')
         elif key == '2':
            date = input("Enter input in DD/MM/YYYY format ")
            idx = date_dict.get(date,-1)
            while idx == -1:
                print("Enter another date ")
                key = input()
            else:
                for i in range(idx[0],idx[1]):
                    summ = list_data[i].get('wind').get('speed')
                print(f'Average wind speed for the day : {summ/(idx[1]+1)}')
        elif key == '3':
            date = input("Enter input in DD/MM/YYYY format ")
            idx = date_dict.get(date,-1)
            while idx == -1:
                print("Enter another date ")
                key = input()
            else:
                for i in range(idx[0],idx[1]):
                    summ = list_data[i].get('main').get('pressure')
                print(f'Average wind pressure for the day : {summ/(idx[1]+1)}')
                
        elif key == '0':
            break
        else:
            print("Press key 1 for average temperature for the day") 
            print("Press key 2 for average wind speed for the day ")
            print("Press key 3 for average wind pressure for the day")
            print("Press 0 to terminate ")
        key = input('Press another key ')
            
            
data = get_weather_data()
get_data_func(data)  
