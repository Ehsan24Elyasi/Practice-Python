import requests
from cachetools import cached, TTLCache
import time

ttl_cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(ttl_cache)
def get_exchange_rate(base_currency, target_currnecy):
    url = f"https://v6.exchangerate-api.com/v6/793a93b356cf3aab90c1366b/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        None
    return response.json()['conversion_rates'][target_currnecy]

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate