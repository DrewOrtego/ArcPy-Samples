#Describe_Object_Projection_Bug

**Demonstrates**
* Use of ArcPy Describe objects to report metadata about dataset's and feature classes
* Use of the os module

**Usage:**

    Runs as a standalone script with Python 2.7
    
    
**Purpose:**

    Demonstrates an equivilency bug between 10.0 (SP0) and 10.1 -
    10.2.2. The Describe object for a feature class does not catch
    the expected spatial reference name. Instead, WGS1984 is found.
    The issue is not present for the dataset which contains the
    feature class.
    
    
**Work Flow:**

    Collects information about a dataset and prints formatted output
    to the console. Useful if modified to report on specific metadata,
    such as spatial information or anything else available through
    the ArcPy Describe objects.
    
**Input:**

    Line 16: The directory to the file geodatabase.
    
**Output:**

    Prints the spatial info for each dataset and the feature
    class(es) contained within it.
