#Exercise_arcpy_1.py
#Author: Karoline Trindade Dutra
#Date: 2026-07-03

#import arcpy library
import arcpy

#set the overwrite permission - avoid the "already exists" erros
arcpy.env.overwriteOutput = True

#set the workspace
arcpy.env.workspace = r"C:\Users\karol\Documents\ArcGIS\Projects\munster_project\exercise_arcpy_1.gdb"

#define the point feature classes
point_fcs = arcpy.ListFeatureClasses(feature_type="Point")

print(point_fcs)

#define the Spatial Reference
sr = arcpy.Describe(point_fcs[0]).spatialReference

#create the feature class (layer) active_assets 
arcpy.management.CreateFeatureclass(arcpy.env.workspace, "active_assets", "POINT", spatial_reference=sr)

#add the fields status and type
arcpy.management.AddField("active_assets", "status", "TEXT")
arcpy.management.AddField("active_assets", "type", "TEXT")

# Define the relevant fields for the whole procedure
fields = ["SHAPE@", "status", "type"]

#Use the insertcursor and searchcursor for: 1. "open" the data to write and 2. read and filter the relevant rows
# the content of searchcursor is used to write in the active_assets layer
with arcpy.da.InsertCursor("active_assets", fields) as i_cur:
    for fc in point_fcs:
        if fc == "active_assets":
            continue
        with arcpy.da.SearchCursor(fc, fields, where_clause = "status = 'active'") as s_cur:
            for row in s_cur:
                i_cur.insertRow(row)

#Verify the coordinate system

print("Current CRS:", sr.name)
print("Type:", sr.type)
print("Units:", sr.linearUnitName) #empty - normal for type geographic
print("Angular unit:", sr.angularUnitName)

#Define a target coordinate system to ETRS_1989_UTM_Zone_32N
target_sr = arcpy.SpatialReference(25832)

print("Current CRS:", target_sr.name)
print("Type:", target_sr.type)
print("Units:", target_sr.linearUnitName) #empty - normal for type geographic
print("Angular unit:", target_sr.angularUnitName)

#set the projection in the layer active_assets
arcpy.management.Project("active_assets", "active_assets_utm", target_sr)

#add the field buffer distance
arcpy.management.AddField("active_assets_utm", "buffer_dist", "DOUBLE")

#calculate the buffer_dist field
expr = "dist(!type!)"
codeblock = """
def dist(t):
    return {"mast": 300, "movile_antenna": 50, "building_antenna": 100}.get(t,0)
"""
arcpy.management.CalculateField("active_assets", "buffer_dist", expr, "PYTHON3", codeblock)

#execute the buffer
arcpy.analysis.Buffer("active_assets", "coverage", "buffer_dist")


