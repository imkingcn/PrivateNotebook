
import requests
import json
import jsonpath


class Weather:
    def __init__(self):
        self.url = "https://www.tianqiapi.com/api/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.city="信阳";
        self.params={
            "appid":"61216394",
            "appsecret":"mBMrhk62",
            "version":"v9",
            "city":self.city
        }

    def get_html(self):
        #weather={};
        response = requests.get(self.url, headers=self.headers,params=self.params).text
        data=json.loads(response)
        Date=jsonpath.jsonpath(data,'$.data..day')
        Dates=jsonpath.jsonpath(data,'$.data..date')
        Hour=iter(jsonpath.jsonpath(data,'$.data..hours..hours'))
        Weather=iter(jsonpath.jsonpath(data,'$.data..hours..wea'))
        # print(Date)
        # print(Dates)
        # print(Hour)
        # print(Weather)
        for date,dates in zip(Date,Dates):
            print(date+" "+dates)
            for hour,wea in zip(Hour,Weather):
                print(hour+":"+wea)
                if (hour=='00时'):
                    break
            


  

if __name__ == "__main__":
    weather = Weather()
    weather.get_html()
