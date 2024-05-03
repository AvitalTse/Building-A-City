#Welcome to my project in Python
"""
Creates a city that returns a dictionary object that stores the city data .
in a city there are 3 Quarters , in each Quarter there are 5 Streets , in each Street there are 4 Buildings, and in each Building 
there are 5 apartments in each apartment located a family in this order : All the apartments on the first floor ("Appartment1") live
families under the last name "A", on the second floor - "B" and so on up to the fifth floor.
"""
def CreateCity():
    city = {}

    for quarter_num in range(1, 4):
        quarter_name = f"Quarter{quarter_num}"
        city[quarter_name] = {}

        for street_num in range(1, 6):
            street_name = f"Street{street_num}"
            city[quarter_name][street_name] = {}

            for building_num in range(1, 5):
                building_name = f"Building{building_num}"
                city[quarter_name][street_name][building_name] = []

                for apartment_num in range(1,6):
                    num=6-apartment_num
                    apartment_name = f"Apartment{num}"
                    family_name = chr(64+num)  # A, B, C...
                    city[quarter_name][street_name][building_name].append({
                        "Apartment": apartment_name,
                        "Family": f"{family_name}"
                    })

    return city
     
#Accepts city , quarter and street names and prints a demonstration of the street's buildings.
def PrintStreet(city,quarter_name,street_name):
    character = "*"
    count = 5
    cols= []
    roof=[]
    buildings_names=[city[quarter_name][street_name]]
    buildings=city[quarter_name][street_name]
    
    for i in range(1, count + 1):
      roof.append( " " * (count - i) + character * (2 * i - 1) + " " * (count - i))
    
    for building_name,apartment in buildings.items():
        apt_rows=[]
        result=[]
        empty_lines=[]
        apartment_num=len(buildings[building_name])

        if(apartment_num<5):
            for apt in range (0,(5-apartment_num)*6):
                empty_lines.append(" "*9)
        for l in range (1,apartment_num+1):
            family_name=apartment[l-1]['Family']
            for i in range(1,3):
                apt_rows.append("="*9)
            apt_rows.append("=" + " "*7 + "=")
            apt_rows.append("="+" "*(int((7-len(family_name))/2))+family_name+" "*(int((7-len(family_name))/2))+"=")
            apt_rows.append("=" + " "*7 + "=")
            apt_rows.append("="*9)
            
            result=empty_lines+roof+apt_rows
        cols.append(result)
    

    for building in buildings_names:
            print(('{: >10} '*len(buildings_names[0])).format(*building))             

    rows = list(zip(*cols))

    for row in rows:
        print(('{: >10} ' * len(row)).format(*row))

#Accepts city data and a quarter name and adds the new quarter to the city only if it doesn't already exist.
def AddQuarter(city, quarter_name):
    if quarter_name in city:
        print(f"Quarter '{quarter_name}' already exists.")
    else:
        city[quarter_name] = {}
        print(f"Quarter '{quarter_name}' added to the city.")

#Accepts city data , quarter and street names, and adds the street to the quarter only if it dosen't already exists.
def AddStreet(city, quarter_name, street_name):
    if quarter_name not in city:
        print(f"Quarter '{quarter_name}' does not exist in the city.")
    elif street_name in city[quarter_name]:
        print(f"Street '{street_name}' already exists in '{quarter_name}'.")
    else:
        city[quarter_name][street_name] = {}
        print(f"Street '{street_name}' added to '{quarter_name}'.")

"""
Accepts city data , quarter and street names , and number of apartments to add , then adds a new buildind with the number of apartments,
notice that there is a max number of 5 apartments in a building.
"""
def AddBuilding(city, quarter_name, street_name, apt_num):
    if quarter_name not in city:
        print(f"Quarter '{quarter_name}' does not exist in the city.")
    elif street_name not in city[quarter_name]:
        print(f"Street '{street_name}' does not exist in the city.")
    elif apt_num>5 or apt_num<0:
        print(f"Invalid number of appartments.")
    else:
        building_name=f'Building{len(city[quarter_name][street_name])+1}'
        city[quarter_name][street_name][building_name]=[]
        for apt in range(1,apt_num+1):
             city[quarter_name][street_name][building_name].append({
                        "Apartment": f"Apartment{apt_num-(apt-1)}",
                        "Family":"Empty"
                    })
        print(f"{apt_num} apartments added to a new building named {building_name} that have been added to {street_name}.")

#Accepts city data, quarter , street and building names , and adds an empty apartment to the building . (mac apartments in a building is 5).
def AddAppartment(city,quarter_name,street_name,building_name):
    if quarter_name not in city:
        print(f"Quarter '{quarter_name}' does not exist in the city.")
    elif street_name not in city[quarter_name]:
        print(f"Street '{street_name}' does not exist in the city.")
    elif building_name not in city[quarter_name][street_name]:
        print(f"Building '{building_name}' does not exist in the city.")
    elif len(city[quarter_name][street_name][building_name]) == 5:
        print(f"Can not add any appartments ,'{building_name}' has a maximum number of appartments.")
    else:
        print(f"An empty appartment numbered {len(city[quarter_name][street_name][building_name])+1} has been added to the city in {quarter_name} , {street_name} , {building_name}.")
        city[quarter_name][street_name][building_name].append({
                        "Apartment": f"Apartment1",
                        "Family":"Empty"
                    })

#Accepts city data , quarter , street , building and a family name , and adds the family to the first empty apartment in the building.
def AddFamily(city,quarter_name,street_name,building_name,family_name):
    if quarter_name not in city:
        print(f"Quarter '{quarter_name}' does not exist in the city.")
    elif street_name not in city[quarter_name]:
        print(f"Street '{street_name}' does not exist in the city.")
    elif building_name not in city[quarter_name][street_name]:
        print(f"Building '{building_name}' does not exist in the city.")
    else:
        for apartment in reversed(city[quarter_name][street_name][building_name]):
        # Check if the family name matches the one you're searching for
            if apartment["Family"] == "Empty":
                print(f"The family {family_name} is in {apartment['Apartment']}.")
                apartment["Family"]=family_name
                return
        print("There are no available appartments")

#Accepts city data , quarter , street and building name and removes the building from the city data. 
def RemoveBuilding(city, quarter_name, street_name,building_name):
    if quarter_name not in city:
        print(f"Quarter '{quarter_name}' does not exist in the city.")
    elif street_name not in city[quarter_name]:
        print(f"Street '{street_name}' does not exist in the city.")
    elif building_name not in city[quarter_name][street_name]:
        print(f"Building '{building_name}' does not exist in the city.")
    else:
        print(f"Building '{building_name}' have been destroyed.")
        del city[quarter_name][street_name][building_name]

#This examples how the project works , in the console you will see various demonstration of the functions.      
city_data=CreateCity()
PrintStreet(city_data,"Quarter1","Street1")  
AddBuilding(city_data,"Quarter1","Street1",4)
PrintStreet(city_data,"Quarter1","Street1") 
RemoveBuilding(city_data,"Quarter1","Street1","Building3")
AddFamily(city_data,"Quarter1","Street1","Building5","Cohen")
PrintStreet(city_data,"Quarter1","Street1") 
        
        
        