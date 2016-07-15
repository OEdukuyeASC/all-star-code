from random import *
characterList = [ "Mario", "Tidus", "Cloud Strife", "Guile"]
vehicleList = [ "Blue Falcon", "Batmobile", "Outlaw Star", "Death Star"]
wivesList = [ " Beyonce" , " Meagan Good", "Kylie Jenner", "Kehlani"]
characterList.append(" Noctis Lucis Caelum")
vehicleList.append("The Regalia")
wivesList.append("Emma Watson")
cResponse = raw_input(" Who is your favorite video gamme character?")
wResponse = raw_input("Who would you want your wife to be?")
vResponse = raw_input ( "what would you like to use as your vehicle")

print ("your fave character is...", choice(characterList))
print ("your vehicle is ...", choice(vehicleList))
print ("your Wife is ....", choice(wivesList))