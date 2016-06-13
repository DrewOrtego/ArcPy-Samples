
#ArcPy-Samples/Cursor-Demo

**Demonstrates**
* Use of the Search, Insert, and Update Cursor's provided by the ArcPy site package.
* Use of nested cursor's to iterate through a table and make logical decisions/changes.
* SQL statements to filter results of each demo.

**Usage:**

    The documentation in the script's themselves explain each script's purpose. For the Search, Insert, and Update Cursors, be sure to
    run the scripts in the same directory as the "Cursor Demo.gdb" file geodatabase. For using the Embedded_Cursor_Demo.py script,
    include the "Embedded_Cursor_Demo.gdb" geodatabase in the directory you execute the script from.
    
**Purpose:**

    I typically send these scripts to customers who are getting started with ArcPy for the first time, and want to know how to iterate
    through a table used in ArcMap or ArcCatalog. They have been well-recieved!
    
**Work Flow:**

    Each script makes simple changes to a table in a file geodatabase.
    
**Input:**

    N/A. Running each script as-is will be sufficient. Ensure that the scripts and File Geodatabase files are all in the same directory to effectively run the scripts.
    
**Output:**

    The Insert Cursor demo will insert a new row into the table, while the Update Cursor demo will delete that row. The Embedded Cursor demo will replace specific characters in a table. All changes are reported in the Python console.
