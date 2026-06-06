#Exercise_6_1.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-05

#Goal - create a map from a CSV file

#open the csv file (r = reading mode)
csv_file = open(r"C:\Users\karol\Downloads\Data for Session 6\Data for Session 6\standard_land_value_muenster.csv", "r")
lines = csv_file.readlines()
csv_file.close()


#print some rows
print(lines[0])
print(lines[1])

#create the memory layer through URI

#build the uri
uri = ("polygon?"
        "crs=EPSG:25832&"
        "field=standard_land_value:double&"
        "field=type:string&"
        "field=district:string")

layer = QgsVectorLayer(uri, "temp_standard_land_value_muenster", "memory")
provider = layer.dataProvider()

#loop through each row
for line in lines[1:]:
    parts = line.split(";")
    
    #in land variable, replace comma as a decimal separator for dot
    land_value = float(parts[0].replace(",","."))
    land_type = parts[1]
    district = parts[2]
    
    #in the Geometry (WKT) remove \n at the end
    wkt = parts[3].strip() #removes any empty space before or after
    
    #convert the wkt to QgsGeometry object
    geom = QgsGeometry.fromWkt(wkt)
    
    #build the feature
    feat = QgsFeature(layer.fields())
    feat.setAttribute("standard_land_value", land_value)
    feat.setAttribute("type", land_type)
    feat.setAttribute("district", district)
    feat.setGeometry(geom)
    
    provider.addFeatures([feat])

#add the layer to the TOC
QgsProject.instance().addMapLayer(layer)
