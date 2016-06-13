""" Demonstrate usage of the DA module's UpdateCursor with a SQL statement.
    Deletes the Groundhog field. """

import arcpy, os

# Cursor parameters
feature_class = os.getcwd() + r"\Cursor Demo.gdb\Animals"
field_names   = ["OID@", "AnimalType", "AnimalName", "ScarinessRank"]
sql_statement = "ScarinessRank = 0"

# Cursor which deletes any animals with a scariness rank of 0
with arcpy.da.UpdateCursor(feature_class, field_names, sql_statement) as uc:
    for row in uc:
        uc.deleteRow()
        print "I deleted {0} the {1} from the table".format(row[2], row[1])

print "Complete"

