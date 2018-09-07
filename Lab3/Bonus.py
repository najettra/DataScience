import requests
import json
import sys

class Weather():
    def __init__(self):
        self.key = "02d8b3dee3fe9b20e3828ab1892e98a8"
        
    def Get_City_Weather(self, city_name):
        req = requests.get("http://api.openweathermap.org/data/2.5/forecast/?q="+city_name+"&appid="+self.key)     
        return req.json()
                        
    def Show_Data(self,city_name):
        data = self.Get_City_Weather(city_name)
        return json.dumps(data['city']['name']), json.dumps(data['list'][0]['main']['temp'])


weath = Weather()
if sys.argv[1]:
    city_name = sys.argv[1]
    print(city_name)
    print(weath.Show_Data(city_name))

else:
    print("Please enter city name")
