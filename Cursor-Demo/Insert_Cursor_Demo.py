""" Demonstrate usage of the DA module's InsertCursor. """

import arcpy, os

# Parameters for the cursor's
feature_class = os.getcwd() + r"\Cursor Demo.gdb\Animals"
field_names   = ("OID@", "AnimalType", "AnimalName", "ScarinessRank")
Groundhog = (8, "Groundhog", "Phil", 0)

# Insert the new animal
with arcpy.da.InsertCursor(feature_class, field_names) as ic:
    ic.insertRow(Groundhog)
print "Inserted the Phil the Groundhog into the table."

