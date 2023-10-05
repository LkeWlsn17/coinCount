import config

Errors = from values import errorss

name = input("enter your name")
amntbags = from values import amntbagss

if name != str:
    name = input("re-enter the name")

bagweight = input()
if bagweight != float:
    print("enter a number for the weight")

cointypes = 2, 1, 0.50 , 0.20, 0.10, 0.05, 0.02, 0.01
cointype = input()
if cointype is not in cointypes:
    print("Invalid Coin Type")
