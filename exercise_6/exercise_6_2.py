#Exercise_6_2.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-06


#Goal: modify and create new fields

#save the layers in a python object
pools = QgsProject.instance().mapLayersByName("public_swimming_pools")[0]
districts = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]

#check the capabilities
provider = pools.dataProvider()
capabilities = provider.capabilitiesString()
print(capabilities) #the capabilities are in portuguese

if "Adicionar atributos" in capabilities:
    print("We can add fields.")
else:
    print("This layer does not support adding fields")

#create a new empty field for the district of each pool
#QgsField(name, type,lenght)
if "Adicionar atributos" in capabilities:
    new_field = QgsField("district", QVariant.String, "string", 50)
    
    #add it via the provider
    provider.addAttributes([new_field])
    
    #update field list ("commit")
    pools.updateFields()
    
#Build a loop to update the Type and District columns

#check the values in "Type" variable
types = {pool["Type"] for pool in pools.getFeatures()}
print(types)

#get the field list
fields = pools.fields()

if "Mudar valores de atributos" in capabilities:
    
    for pool in pools.getFeatures():
        
        pool_id = pool.id()
        pool_geom = pool.geometry()
        
        #detail the type letter
        if pool["Type"] == "H":
            new_type = "Hallenbad"
        else:
            new_type = "Freibad"
            
        attributes = {
            fields.indexOf("Type"): new_type
        }
        
    #find the district which each pool is in
        for district in districts.getFeatures():
            if pool_geom.within(district.geometry()):
                attributes[fields.indexOf("district")] = district["Name"]
                break #a pool can only be in one district, thus the break stops the processing when it is found
                
    #write both changes (use of "...Values" in plural for multiple changes)
        provider.changeAttributeValues({pool_id: attributes})


#count how many pools by district - one way to verify the results
import pandas as pd
df_districts = pd.DataFrame([feature["district"] for feature in pools.getFeatures()])
print(df_districts.value_counts())