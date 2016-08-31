# Describe-Object-Report

**Demonstrates**

    * Use of a decorator function
    * Command-line argument processing with optional flags/parameters
    * Use of arcpy's extensive collection of Describe objects
    * Web-scraping to populate a python dict

**Description:**

    Create a report of all arcpy describe-object properties for an object. Each
    property has an number of attributes associated with it. See documentation:
    https://pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm

**Usage:**

    All arguments are optional, and must be separated by whitespace. The first
    argument must be a verbose or terse flag, followed by the properties flag,
    otherwise you'll get a parsing error.

        * VERBOSE VS TERSE MODE: -v or -t
        The difference between the two is that verbose will show you all of the
        attributes that have no value, whereas terse will not. These are
        optional, and verbose mode will be reported if these arguments are not
        provided. Verbose is useful for seeing each attribute of a property.

        * PROPERTIES: -p
        Follow the -p flag with the Describe Object properties needed in the
        report. Useful for shrinking the size of the report down to just those
        properties (and their corresponding attributes) which are relevant to
        the user.

**Input**

    > python describe_reporter.py -t -p "Layer Properties" "Table Properties"

**Caveats**

    * The output will be overwritten unless you change the output's path in the source code
