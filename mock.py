

data = int(input("Enter your time: "))
rank = ""

if data >= 35:
    rank = "Bronze Strider"
elif data >= 30:
    rank = "Silver Sprinter"
elif data >= 27:
    rank = "Gold Pacer"
elif data >= 24:
    rank = "Platinum Racer"
elif data >= 21:
    rank = "Diamond Dasher"
elif data >= 19:
    rank = "Elite Striker"
elif data >= 17:
    rank = "Champion Runner"
else:
    rank = "Legendary Phantom"
    
print (rank)