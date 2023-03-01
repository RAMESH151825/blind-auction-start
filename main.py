from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
bid_list = []
bid = 0
bidder_name = ""
n = 0
def add_bid(name, value, toContinue):
  bid_dict = {}
  bid_dict["name"] = name
  bid_dict["value"] = int(value)
  bid_dict["toContinue"] = toContinue
  bid_list.append(bid_dict)

while True:
  name = input("enter your name\n")
  value = input("input value\n")
  toContinue = input("do you want to continue, yes or no\n").lower()
  add_bid(name, value, toContinue)
  if bid_list[n]["value"] > bid:
    bid = bid_list[n]["value"]
    bidder_name = bid_list[n]["name"]
  n += 1
  clear()
  if toContinue == "no":
    print(f"biggest bid is from {bidder_name} with bid value of {bid}")
    break
