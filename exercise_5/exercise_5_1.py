#Exercise_5_1.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-31

## Goal: Find schools within a district

#creating the dialog window
parent = iface.mainWindow()

#save the layer in a object
districts = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]

#check if the layer were loaded correctly
if not districts.isValid():
    print("Layer failed to load!")

#build the sorted district names list

# create an empty list
districts_names = []

# create a request that returns features sorted alphabetically by NAME
request = QgsFeatureRequest()
clause = QgsFeatureRequest.OrderByClause("Name")
request.setOrderBy(QgsFeatureRequest.OrderBy([clause]))

#Loop to fill the empty list districts_names
for district in districts.getFeatures(request):
    districts_names.append(district["Name"])
    
#check the list result
#print(districts_names[:5])


#Show the dorpdown dialog
sDistrict, bOk = QInputDialog.getItem(
    parent, "District Names", "Select District: ", districts_names
)

# Handle cancel option
if not bOk:
    QMessageBox.warning(parent, "Schools", "User cancelled")
    
if bOk:
    geom_district = None
    
    for district in districts.getFeatures():
        if district["Name"] == sDistrict:
            geom_district = district.geometry()
            break #stop the loop as soon the district is found
            
#find schools within a district

schools = QgsProject.instance().mapLayersByName("Schools")[0]

school_request = QgsFeatureRequest()
school_clause = QgsFeatureRequest.OrderByClause("NAME")
school_request.setOrderBy(QgsFeatureRequest.OrderBy([school_clause]))

output = ""
school_ids = []

for school in schools.getFeatures(school_request):
    if school.geometry().within(geom_district):
        output += f"{school['NAME']}, {school['SchoolType']}\n"
        school_ids.append(school.id())

#handle districts without schools
if not school_ids:
    output = "There aren't schools in the selected district"

# Show the result, select schools and zoom

#show the pop-up
QMessageBox.information(parent, f"Schools in {sDistrict}", output)

#Select the matching schools on the map
schools.selectByIds(school_ids)

iface.mapCanvas().zoomToSelected(schools)

#zoom adjustment
if iface.mapCanvas().scale()<50000:
    iface.mapCanvas().zoomScale(50000)
