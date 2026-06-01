#Exercise_5_2.py
#Author: Karoline Trindade Dutra
#Date: 2026-06-01

## Goal: Verify if coordinates are inside Münster districts
#Geoguesser – Münster Style

#Guarantee the same coordinate system
#save the layer in a object
city_districts = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]

#check the crs
#city_districts.crs()
# result = <QgsCoordinateReferenceSystem: EPSG:25832>

#build the transformation object
#crs WGS84 that will be used by the users
crs_from = QgsCoordinateReferenceSystem(4326)

#Target = crs from the current layer
crs_to = city_districts.crs()

#create the transformation object
transform = QgsCoordinateTransform(crs_from, crs_to, QgsProject.instance())

#create the pop-up dialog
parent = iface.mainWindow()

sCoords, bOk = QInputDialog.getText(
    parent,
    "Coordinates",
    "Enter coordinates as latitude, longitude",
    text = "51.96066,7.62476"
)

#parse and convert the input string
if bOk:
    parts = sCoords.split(",")
    lat = float(parts[0]) #north-south
    lon = float(parts[1]) #east-west
    
# transform the input string in a point geometry
    point_wgs84 = QgsPointXY(lon, lat) #QgsPointXY uses longitude first

# transform the CRS of the point from WGS84 to the CRS used in the layer
    point_projected = transform.transform(point_wgs84)

#Wrap in QgsGeometry to be used with .within()
    point_geom = QgsGeometry.fromPointXY(point_projected)

# Loop through districts and check containment

found = False

for district in city_districts.getFeatures():
    district_geom = district.geometry()
    
    if point_geom.within(district_geom):
        district_name = district["Name"]
        QMessageBox.information(
            parent,
            "It's a match!", #title of the dialog box
            f"The point lies within: {district_name}" #content information
        )
        found = True
        break #stop when the point is found within a district
        #one point is inside in only one district

#handle points outside Münster
if not found:
    QMessageBox.information(
        parent,
        "No match!",
        "The point does not lie within any district in Münster."
    )