"""Ücretsiz API İle Dolar Kuru Kontrol"""
import requests
import json


def currency_check(base, to):  # base = hangi birimden çevirmek istiyorsunuz  to = hangi birime çevirmek istiyorsunuz
    try:
        url = "https://api.exchangeratesapi.io/latest?base={0}&symbols={1}".format(base, to)
        curr_response = requests.get(url)
        json_data = json.loads(curr_response.text)
        kurpure = json_data['rates'][to]
        return kurpure
    except False:
        print("fail")
        pass


usd_to_try = currency_check("USD", "TRY")
print("1 USD equals " + str(usd_to_try) + " TRY ")

try_to_usd = currency_check("TRY", "USD")
print("1 TRY equals " + str(try_to_usd) + " USD ")

eur_to_try = currency_check("EUR", "TRY")
print("1 EUR equals " + str(eur_to_try) + " TRY ")