# Describe_Object_Projection_Bug

**Name:**

    Spatial_Describe.py

**Author:**

    Andrew Ortego - 08/22/2014

**Purpose:**

    Demonstrates an equivilency bug between ArcGIS 10.0.0 and 
    10.1 through 10.2.2. The Describe object for a feature class does not 
    catch the expected spatial reference name. Instead, WGS1984 is found.
    The issue is not present for the dataset which contains the
    feature class.

**Input:**

    Line 16: The name of the geodatabase to be scanned.
    **Ensure that the script it run from the same directory as
    the geodatabase.**

**Output:**

    Prints the spatial info for each dataset and the feature
    class(es) contained within it.
