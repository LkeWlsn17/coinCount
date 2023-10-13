f = open("values.txt")

e = f.readlines()
totalvalue = e[2].split('=')[1].strip()
errors = e[0].split('=')[1].strip()
amntbags = e[1].split('=')[1].strip()
f.close()

print("""
░█████╗░░█████╗░██╗███╗░░██╗  ░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗
██╔══██╗██╔══██╗██║████╗░██║  ██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝
██║░░╚═╝██║░░██║██║██╔██╗██║  ██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░
██║░░██╗██║░░██║██║██║╚████║  ██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░
╚█████╔╝╚█████╔╝██║██║░╚███║  ╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░
░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░""")

name = input("enter your name\n")
isValidName = True
for character in name:
    if character.isnumeric():
        isValidName = False

if not isValidName:
    input("enter a valid name\n")

bagweight = float(input("Enter a bag weight\n"))

cointypes = 2, 1, 0.50 , 0.20, 0.10, 0.05, 0.02, 0.01

cointype = float(input("enter the value of your coin\n"))

remainder = bagweight%cointype
if bagweight%cointype == 0:
    print("")
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

mathbagvalue = float(bagweight/cointype)
totalbagvalue = (coinweights[cointype]*mathbagvalue)

totalvalue = float(totalvalue) + totalbagvalue
totalvalue = str(totalvalue)
totalbagvalue = str(totalbagvalue)

volunteers = []
f = open("values.txt")
e = f.readlines()
volunteers.append(e[3].split('=')[1].strip())
volunteers.append(name)
                
f.close()


print("the total value of this bag is",totalbagvalue,)
filevalue = f"errors = {errors}\namntbags = {amntbags}\ntotalbagvalue = {totalvalue}\nvolunteers={volunteers}"

f = open("values.txt",'r+')
f.write(filevalue)