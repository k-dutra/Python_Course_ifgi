#Exercise_4_4.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-14

#count the number of schools by city district 
#code to be used in Qgis Python Editor.

#Import the relevant packages
from qgis.core import QgsVectorLayer #used to verify if the processing function returned an QgsVectorLayer object

# 1) Dissolve polygons by P_district
#change your INPUT path
dissolved = processing.run("native:dissolve", {
    'INPUT': 'C:/Users/karol/Downloads/Muenster/Muenster/Muenster_City_Districts.shp',
    'FIELD': ['P_district'], #Variable used to aggregate the areas
    'OUTPUT': 'TEMPORARY_OUTPUT'
})['OUTPUT']

# 2) Count points inside each dissolved polygon (Districts)
#change your POINT path
result = processing.run("native:countpointsinpolygon", {
    'POLYGONS': dissolved,
    'POINTS':   'C:/Users/karol/Downloads/Muenster/Muenster/Schools.shp',
    'WEIGHT':   '',
    'CLASSFIELD':'',
    'FIELD':    'NUMPOINTS',
    'OUTPUT':   'TEMPORARY_OUTPUT'
})['OUTPUT']

#check if the result is a QgsVectorLayer object, otherwise, treat it as a file path and build a QgsVectorLayer from it."
layer = result if isinstance(result, QgsVectorLayer) else QgsVectorLayer(result, "result", "ogr")

# Optional: add the map result
QgsProject.instance().addMapLayer(layer)

# 3) Print results in the console
for feat in layer.getFeatures():
    print(f"{feat['P_district']}: {feat['NUMPOINTS']} schools")
