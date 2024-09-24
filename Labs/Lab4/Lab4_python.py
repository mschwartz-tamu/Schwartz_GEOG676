
# creat a gdb and garage
import arcpy

arcpy.env.workspace = r'C:\Users\mschwartz95\DevSource\Schwartz_GEOG676\Labs\Lab4'
folder_path = r'C:\Users\mschwartz95\DevSource\Schwartz_GEOG676\Labs\Lab4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'C:\Users\mschwartz95\DevSource\2024-TAMU-GEOG-676-GIS-Programming-MGsc\data\homework\04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# open campus gdb, copy feature to our gdb
campus = r'C:\Users\mschwartz95\DevSource\2024-TAMU-GEOG-676-GIS-Programming-MGsc\data\homework\04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# buffer the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_Buffered', 150)

# Intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', r'C:\Users\mschwartz95\DevSource\Schwartz_GEOG676\Labs\Lab4', '\nearbybuildings.csv')