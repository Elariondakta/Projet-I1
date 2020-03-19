import json
import uuid

#Génère les salles de base de l'ISEP

with open("./data/choice.json", "r") as f:
    data = json.load(f)
    
for i in range(1, 4):
    for j in range(1, 20):
        data["rooms"][str(uuid.uuid1())] = {
            "building_name": "NDL",
            "room_name": "L" + str(i) + str(j).zfill(2) #Pour avoir le format suivant : 01, 02, 03
        }

for i in range(1, 5):
    for j in range(1, 9):
        data["rooms"][str(uuid.uuid1())] = {
            "building_name": "NDC",
            "room_name": "N" + str(i) + str(j)
        }
    
with open("./data/choice.json", "w") as f:
    print(json.dump(data, f))
