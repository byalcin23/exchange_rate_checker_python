"""Ücretsiz API İle Dolar Kuru Kontrol"""
import requests
import json

api_key="YOUR_API_KEY_HERE"

payload = {}
headers= {
  "apikey": api_key
}


def currency_check(base ,to , amount):  # base = hangi birimden çevirmek istiyorsunuz  to = hangi birime çevirmek istiyorsunuz
    try:
        #url = "https://api.exchangeratesapi.io/latest?base={0}&symbols={1}".format(base, to)
        url = "https://api.apilayer.com/exchangerates_data/convert?to={0}&from={1}&amount={2}".format(to, base, amount)
        curr_response = requests.request("GET", url, headers=headers, data = payload)
        json_data = json.loads(curr_response.text)
        #kurpure = json_data['rates'][to]
        kurpure = json_data['info']['rate']
        return kurpure
    except False:
        print("fail")
        pass


usd_to_try = currency_check("USD", "TRY", 1)
print("1 USD equals " + str(usd_to_try) + " TRY ")

try_to_usd = currency_check("TRY", "USD", 1)
print("1 TRY equals " + str(try_to_usd) + " USD ")

eur_to_try = currency_check("EUR", "TRY", 1)
print("1 EUR equals " + str(eur_to_try) + " TRY ")