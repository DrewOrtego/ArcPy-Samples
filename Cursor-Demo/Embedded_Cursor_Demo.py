""" Demonstrate usage of the DA module's InsertCursor and SearchCursor. """

import arcpy, os

# 1 Parameters for Search Cursor:
feature_class_Search = os.getcwd() + r"\Embedded Cursor Demo.gdb\Animals"
field_names_Search   = "AnimalType"
sql_statement_Search = "ScarinessRank = 5"

# 2 Parameters for Insert Cursor:
feature_class_Insert = os.getcwd() + r"\Embedded Cursor Demo.gdb\New_Table"
field_names_Insert   = "Insert_Field"

# 3 A list of the character's we want to replace:
replace_characters = ["#", "!", "$"]

# 4 Delete the fields in "New_Table" so that we start with a blank table:
arcpy.DeleteRows_management(feature_class_Insert)

# 5 Iterate over the original table, and erase the unwanted characters:
#     Note that the contents of search_row[0] in a variable called 'temp',
#     then updated the contents of 'temp' for inserting into the second table.
with arcpy.da.SearchCursor(feature_class_Search, field_names_Search, sql_statement_Search) as search_cursor:
    with arcpy.da.InsertCursor(feature_class_Insert, field_names_Insert) as insert_cursor:
        for search_row in search_cursor:
            temp = search_row[0]
            print "Original row contents: {0}".format(temp)
            for char in replace_characters:
                temp = temp.replace(char, "")
            print " Updated row contents: {0}\n".format(temp)
            insert_cursor.insertRow([temp])

# 6 Print a message to indicate we're done:
print "Complete"

