# Import libraries
import json
import requests

# holds all available currencies
choice = {
  '1': 'BTC',
  '2': 'ETH'
}


print("Choose currency")
print("1 = BitCoin")
print("2 = Etheruem")
coin = input("Choose: ")


# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol="+choice[coin]+"USDT"

# requesting data from url
data = requests.get(key)
data = data.json()
price = float(data['price'])
# print(f"{data['symbol']} price is {data['price']}")




def calculate_percentage(a, b):
  c = b - a
  p = c / a * 100
  return p


def change_price(percent, price):
  return (percent*price) + price



print("")

initial = int(input("How much is your initial investment? "))
profit = int(input("How much profit would you like? "))
new = initial + profit

percentage_change = (calculate_percentage(initial, new)/100)
# print(percentage_change)
final_crypto_price = change_price(percentage_change, price)

print("")
print(f"At the current {choice[coin]} price of {price}, 
      your in order for your investment to go from {initial} to {new}, 
      the price will have to increase by {percentage_change*100}% to be {final_crypto_price}")
