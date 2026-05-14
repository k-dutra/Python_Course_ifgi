#Exercise_4_1.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-14

#python script to use inside Qgis with a project with layers already loaded

#import relevant packages
from qgis.PyQt.QtCore import QVariant, QUrl
from qgis.core import QgsField, edit
from qgis.PyQt.QtWebKitWidgets import QWebView

#List the layers in your project
for layer in QgsProject.instance().mapLayers().values():
    print(layer.name())

# put a specific layer in an object
#in this script we will work with the Muenster_City_Districts layer
layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]


#creating new attributes in the attribute table
# wikipedia url
#1st create a new empty field
layer.dataProvider().addAttributes([
QgsField("wiki_url", QVariant.String, len = 500)])

layer.updateFields()

#2nd update the field with the desired info
with edit(layer): #open the edition mode
    for feature in layer.getFeatures(): #loop through all features
        name = feature["Name"] #acess the attribute Name
        feature["wiki_url"] = "https://de.wikipedia.org/wiki/" + name.replace(" ", "_") #concatenate and replace spaces by _
        layer.updateFeature(feature)

#Creating the pop-up
# create one QWebView instance
web = QWebView()

#create a function to show the pop up for selected features
def show_wiki():
    for feature in layer.getSelectedFeatures():
        url = feature["wiki_url"]
        web.load(QUrl(url))
        web.show()
        break

# Connect the signal: every time the selection changes, show_wiki() runs
layer.selectionChanged.connect(show_wiki)