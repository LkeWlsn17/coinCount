import json

coinweights = {
    2: 12,
    1: 8.75,
    0.50: 8,
    0.20: 5,
    0.10: 6.50,
    0.05: 2.35,
    0.02: 7.12,
    0.01: 3.56,
    # the dictionary that cointains the weight of each single coin
}
bagweights = {
    2: 120,
    1: 175,
    0.50: 160,
    0.20: 100,
    0.10: 130,
    0.05: 47,
    0.02: 142.4,
    0.01: 71.2,
}
f = open("values.txt")

e = f.readlines()
errors = e[0].split("=")[1].strip()
amntbags = e[1].split("=")[1].strip()
totalvalue = e[2].split("=")[1].strip()
totalweight = e[3].split("=")[1].strip()
f.close()

Serrors = 0
Perrors = 0

print(
    """
░█████╗░░█████╗░██╗███╗░░██╗  ░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗
██╔══██╗██╔══██╗██║████╗░██║  ██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝
██║░░╚═╝██║░░██║██║██╔██╗██║  ██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░
██║░░██╗██║░░██║██║██║╚████║  ██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░
╚█████╔╝╚█████╔╝██║██║░╚███║  ╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░
░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░"""
)

name = input("enter your name\n")  # gets the name value
isValidName = True  # validates the name by checking if characters in the name are not numbers but letters. It does this by searching the input letter by letter using a for loop
for character in name:
    if character.isnumeric():
        isValidName = False

if not isValidName:
    # has them re-enter the name if it flags as numeric
    name = input("enter a valid name\n")

bagweight = float(input("enter the weight of the bag"))
# gets the weight of the bag and casts it into a float
bagvalues = {2: 20, 1: 20, 0.50: 10, 0.20: 10, 0.10: 5, 0.05: 5, 0.02: 1, 0.01: 1}

# the list of acceptable coin types
cointypes = 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01

# gets the type of coin from the user and casts to a float
cointype = float(input("enter the value of your coin\n"))
totalvalue = float(totalvalue) + float(bagvalues[cointype])

while cointype in cointypes == True:
    print("")
else:
    # validates the coin type by comparing the input to the list of acceptable values (cointypes)
    cointype = float(input("please enter a valid coin value"))


# remainder is needed for a future calculation that determines how many more coins would be needed if the bag weight is correct and not misweighed
bagvalue = bagvalues[cointype]
gramsToBeChanged = bagweight - bagweights[cointype]
CoinsToBeChanged = gramsToBeChanged / coinweights[cointype]

while bagweight != coinweights[cointype]:
    print("Misweighed")
    # tells the user how many more coins they would need for a valid bag weight
    print(
        "you would need",
        gramsToBeChanged,
        "more or less grams to have a valid bagweight or",
        CoinsToBeChanged,
        "more or less coins",
    )
    bagweight = float(input("please enter the bag weight after corrections"))
    if bagweight == coinweights[cointype]:
        exit()
    errors = float(errors) + 1  # adds one to errors and casts to float
    # adds one to Single errors and casts to float
    Serrors = float(Serrors) + 1

# mathbagvlue is a variable that is used to hold the maths behind finding the value of the bag
mathbagvalue = float(bagvalue / cointype)
# totalbagvalue is the variable that stores the value of the bag
totalbagweight = coinweights[cointype] * mathbagvalue

# total value and the bag value are then added together
totalweight = float(totalweight) + totalbagweight
totalweight = str(totalweight)
totalbagweight = str(totalbagweight)
# casts both these to strings so they can be written onto the file later

volunteers = []
with open("values.txt") as f:
    e = f.readlines()
    volunteers.append(e[3].split("=")[1].strip()[1:1])
    volunteers.append((name))

# adds the variable 'name' to a list of volunteers that are working for the charity

# Perrors and Serrors mean Personal Errors and Single Run Errors
# Perrors = [0 + Serrors]
# names = [volunteers]
volunteerstats = dict()

volunteerstats = {name: Perrors}

filevalue = f"errors = {errors}\namntbags = {amntbags}\ntotalvalue = {totalvalue}\ntotalbagvalue = {totalvalue}\nvolunteers={volunteers}\nvolunteerstats={volunteerstats}"

with open("values.txt", "w+") as f:
    f.write(filevalue)

bagstatquestion = input("would you like to see bag info , answer Yes or No\n")
if bagstatquestion == "Yes":
    print(
        "Volunteer name is",
        name,
        "\n",
        "total bag weight =",
        totalbagweight,
        "\n",
        "Bags value is",
        bagvalue,
    )
else:
    print()

statsquestion = input("would you like to see the overall stats , answer Yes or No\n")
if statsquestion == "Yes":
    print(
        "total value is",
        totalvalue,
        "\n" "current volunteers are",
        volunteers,
        "\n" "volunteer name and accuracy",
        # volunteerstats[Perrors[accuracy]],
        "\n",
        "amount of bags counted are",
        amntbags,
        "\n",
    )
else:
    print()
