# Describe-Object-Report

**Demonstrates**

    * Use of decorator
    * Command-line argument processing
    * Use of arcpy's extensive collection of Describe objects

**Description:**

    Creates a report of all arcpy describe-object properties for an object.

**Usage:**

    All arguments are optional, and must be separated by whitespace.
    Command line arguments can include a verbose or terse flag (-v or -t) as
    an optional argument, and url's as the source of Describe documentation. If
    you only want to generate a report which contains specific Describe Object
    properties (and all of their attributes) you can enter each property
    individually (use quotes for multiple-word properties). See SAMPLE USAGE
    below.

        **VERBOSE VS TERSE MODE**
        -v or -t
        The difference between the two is that verbose will show you all of the
        attributes that have no value, whereas terse will not. Subsequent
        arguments are each of the describe properties being asked for in the
        report. These are optional, and verbose mode will be reported if these
        arguments are not provided.

        **URL INPUT** 
        -u <url>
        It is optional to provide a url as an argument after the '-u' flag. The
        url should be the Describe documentation from Esri's help pages. The
        html content of that url will be parsed to collect all Properties and
        their Attributes, so verify that you are providing the url of the page
        with all the Properties listed. There is a default dict provided which
        was generated from the Pro 1.3 documentation. That default dict will be
        utilized if the provided url cannot be reached.

**Input:**

    NOTE: Be sure to update file_list.py before running!
    > python describe_reporter.py -v
    > python describe_reporter.py -t
    > python describe_reporter.py -v "General Describe" "Layer" "Table"
    > python describe_reporter.py -t "General Describe" "Workspace"

**Caveats**

    * The output will be overwritten unless you change the output's path in the source code
    * Some Describe properties do not have any attributes (e.g. dbase) and are commented out in the 'properties' dict

**Output Format (in terse mode)**

    {
        Filename 1: {
            Describe Object Class 1: {
                Property 1: output,
                Propetry 2: {},
            }
        }
        Filename 2: 'FILE NOT FOUND'
    }
