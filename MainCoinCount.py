f = open("values.txt")

e = f.readlines()
totalvalue = e[2].split('=')[1].strip()
errors = e[0].split('=')[1].strip()
amntbags = e[1].split('=')[1].strip()

name = input("enter your name")
isValidName = True
for character in name:
    if character.isnumeric():
        isValidName = False

if not isValidName:
    input("enter a valid name")

bagweight = float(input("Enter a bag weight"))

cointypes = 2, 1, 0.50 , 0.20, 0.10, 0.05, 0.02, 0.01

cointype = float(input("enter the value of your coin"))

remainder = bagweight%cointype
if bagweight%cointype == 0:
    print("Valid")
else:
    print("Misweighed")
    print("you would need",remainder/cointype,"more coins to have a valid bagweight")

coinweights = {
    2 : 12,
    1 : 8.75,
    0.50 : 8,
    0.20 : 5,
    0.10 : 6.50,
    0.05 : 2.35,
    0.02 : 7.12,
    0.01 : 3.56,

}

totalbagvalue = coinweights[cointype]*bagweight
totalbagvalue = float(totalbagvalue)
print("the total value of this bag is",totalbagvalue,)

totalvalue = float(totalvalue) + totalbagvalue
totalvalue = str(totalvalue)

f.write(totalvalue)[2]
