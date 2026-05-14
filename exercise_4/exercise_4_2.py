#Exercise_4_2.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-14

#load and show a shapefile in Qgis Python Editor
path = "C:/Users/karol/Downloads/Muenster/Muenster/Schools.shp" #use your own path
schools_layer = iface.addVectorLayer(path, "Schools", "ogr")

#show the attributes of a layer
for field in schools_layer.fields():
    print(field.name())

#extract the school names and coordinates
#export to a csv file
import csv

#change to save in your own path
with open("C:/Users/karol/Downloads/SchoolReport.csv", "w", 
newline = "", encoding = "utf-8") as new_file:
    writer = csv.writer(new_file, delimiter = ";")
    writer.writerow(["Name", "x", "y"]) #provide the header
    for point in schools_layer.getFeatures(): #loop to get and to write each row
        coord = point.geometry().asPoint()
        writer.writerow([point["NAME"], coord.x(), coord.y()])

print("File exported successfully!")