""" describe_reporter.py
    Andrew Ortego
    8/31/2016

    DESCRIPTION
    Create a report of all arcpy describe-object properties for an object. Each
    property has an number of attributes associated with it. See documentation:
    https://pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm

    INPUT
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

    SAMPLE USAGE
    > python describe_reporter.py -t -p "Layer Properties" "Table Properties"

    CAVEATS
    * The output will be overwritten unless you change the path in the code.
    * The output is written to the directory your Windows Command Prompt is pointing to when you run the .py file.
      [e.g. "C:\Users\drew\Desktop> python describe_reporter.py" will write the output to the Desktop.]
"""

import arcpy
import time
import sys
import os
from config_files.default_props import default_properties
from pprint import pprint
from functools import wraps
from collections import OrderedDict as od
try:
    from config_files.file_list import user_files
except ImportError as e:
    message = """
    ERROR: Could not find list of files to be scanned. Please verify
    that file_list.py is in the same directory as this script, and
    that it contains a list called user_files which holds each path
    to your files.
    EXAMPLE: user_files = [u'C:\\Users\\andr7495\\Desktop\\KML.kml']
    Exiting program...
    """
    print(message)
    raise SystemExit


def timethis(func):
    """ Decorator that reports execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Created {0} in {1}s".format(
            os.path.join(os.getcwd(), u'Describe Report.txt'),
            round(end-start)))
        return result
    return wrapper


def set_mode(user_input):
    """ Check whether the user has select verbose or terse mode. This is set
        with the -v or -t flags, respectively. Return True to use verbose mode
        (default) or False to use terse mode.
    """
    mode = {"terse": False, "verbose": True}
    if "-t" in user_input:
        return mode["terse"]
    elif "-v" in user_input:
        return mode["verbose"]
    else:
        return mode["verbose"]


def check_prop_list(user_input):
    """ Verify that the user has entered valid Describe Object types/classes
        and print a warning message for any invalid choices. If no arguments
        are provided, the report will print all Describe properties. Returns a
        list of Describe properties whose attributes will be included in the
        report.
    """
    if '-p' not in user_input:
        queried_types = [p for p in default_properties]
    else:
        invalid_types = list()
        queried_types = list()
        [queried_types.append(k)
            if k in default_properties
            else invalid_types.append(k)
            for k in user_input[user_input.index('-p')+1:]]
        if invalid_types:
            message = """
            The following properties are not available. Verify that you can see
            these properties in the online documentation for the version of
            ArcMap or Pro you are using, and that they are spelled
            correctly."""
            print(message)
            for t in invalid_types:
                print(t)
    return queried_types


@timethis
def generate_report(verbose_mode, property_list, user_files):
    """ Generates the report containing each file and its associated
        Describe-object attributes. Report is a dictionary and can be useful
        for other scripts.
    """
    report_results = {}
    report_path = open(os.path.join(os.getcwd(), u'Describe Report.txt'), 'wt')
    for f in user_files:
        if arcpy.Exists(f):
            desc_dict = dict()
            for d_class in sorted(property_list):
                desc_dict[d_class] = dict()
                for p in default_properties[d_class]:
                    try:
                        desc_dict[d_class][p] = eval(
                            "arcpy.Describe(f).{0}".format(p))
                    except AttributeError:
                        if verbose_mode:
                            desc_dict[d_class][p] = 'N/A'
                        else:
                            pass
            report_results[f] = desc_dict
        else:
            report_results[f] = 'FILE NOT FOUND'
    pprint(report_results, report_path, width=400)


if __name__ == "__main__":
    """ Collect user input, check report mode, clean list of properties to be
        reported, and generate the report.
    """
    user_input = [arg for arg in sys.argv]
    verbose_mode = set_mode(user_input)
    cleaned_user_types = check_prop_list(user_input)
    generate_report(verbose_mode, cleaned_user_types, user_files)
    print('\nfin.')
