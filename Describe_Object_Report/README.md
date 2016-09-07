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

    The files you wish to report on are all listed in config_files/file_list.py.
    This is simply a python list with all the data paths to your file. If a file
    cannot be found, you will see this in the report. If a file does not have an
    attribute from a certain Describe Property, you will see an "N/A" associated
    with that attibute (in verbose mode) or it will be empty (in terse mode).
    
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

    > python describe_reporter.py -t
    > python describe_reporter.py -t -p "Layer Properties" "Table Properties"

**Caveats**

    * The output will be overwritten unless you change the output's path in the source code
    * The output is written to the directory your Windows Command Prompt is pointing to when you run the .py file.
      [e.g. "C:\Users\drew\Desktop> python describe_reporter.py" will write the output to the Desktop.]
