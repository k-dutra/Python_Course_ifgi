#Exercise_4_3.py
#Author: Karoline Trindade Dutra
#Date: 2026-05-14

#Creating a first Qgis project from visual studio

# Import modules
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject
from qgis.core import *
import os

# Supply path to qgis install location
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.44.9", True)

#Start the Qgis App (headless - no GUI)
qgs = QgsApplication([], False)
qgs.initQgis

#List only the shapefiles in the folder Muenster
folder = "C:/Users/karol/Documents/Python_Course_ifgi/exercise_4/Muenster"
shp_files = [f for f in os.listdir(folder) if f.lower().endswith(".shp")]

print(shp_files)

# # Path to data and QGIS-project
layers_path = r"C:\Users\karol\Documents\Python_Course_ifgi\exercise_4\Muenster"
project_path = r"C:\Users\karol\Documents\Python_Course_ifgi\exercise_4\Muenster\myFirstProject.qgz"  # for QGIS version 3+

#Loop to read all .shp in the folder and create the layers in the project
for filename in os.listdir(layers_path):
    if filename.lower().endswith(".shp"):
        full_path = os.path.join(layers_path, filename)
        name = os.path.splitext(filename)[0]   # remove ".shp"
        layer = QgsVectorLayer(full_path, name, "ogr")
        # Check if layer is valid
        if not layer.isValid():
            print("Error loading the layer!")
        else:
            # Create QGIS instance, add layers and "open" the project
            project = QgsProject.instance()
            project.addMapLayer(layer) # Add layer to project
            project.read(project_path) #"open" the project
            print(f"Layer: {name} added successfully!")

# Save project
project.write()

print("Project saved successfully!")





# # Create layer
# layer = QgsVectorLayer(layer_path, "WKA eingeladen", "ogr")

# # Check if layer is valid
# if not layer.isValid():
#     print("Error loading the layer!")
# else:
#     # Create QGIS instance and "open" the project
#     project = QgsProject.instance()
#     project.read(project_path)

#     # Add layer to project
#     project.addMapLayer(layer)

#     # Save project
#     project.write()

#     print("Layers added to project\nProject saved successfully!")
