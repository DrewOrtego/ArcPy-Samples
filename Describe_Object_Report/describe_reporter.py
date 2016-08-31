""" describe_reporter.py
    Andrew Ortego
    8/30/2016

    TODO
    * Alter output with pprint so that it's all aligned (see output formatting)
    * utilize .ini file to accept user params

    DESCRIPTION
    Create a report of all arcpy describe-object properties for an object.

    INPUT
    All arguments are optional, and must be separated by whitespace.
    Command line arguments can include a verbose or terse flag (-v or -t) as
    an optional argument, and url's as the source of Describe documentation. If
    you only want to generate a report which contains specific Describe Object
    properties (and all of their attributes) you can enter each property
    individually (use quotes for multiple-word properties). See SAMPLE USAGE
    below.

        * VERBOSE VS TERSE MODE: -v or -t
        The difference between the two is that verbose will show you all of the
        attributes that have no value, whereas terse will not. Subsequent
        arguments are each of the describe properties being asked for in the
        report. These are optional, and verbose mode will be reported if these
        arguments are not provided.

        * URL INPUT: -u <url>
        It is optional to provide a url as an argument after the '-u' flag. The
        url should be the Describe documentation from Esri's help pages. The
        html content of that url will be parsed to collect all Properties and
        their Attributes, so verify that you are providing the url of the page
        with all the Properties listed. There is a default dict provided which
        was generated from the Pro 1.3 documentation. That default dict will be
        utilized if the provided url cannot be reached.

    CAVEATS
    * The output will be overwritten unless you change the path in the code.
    * The url param will not error-check your input, so if you are seeing
      incorrect (or no) results in your report, verify that the url has the list
      of Describe properties.
      Example: pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm

    SAMPLE USAGE
    > python describe_reporter.py
    > python describe_reporter.py -t
    > python describe_reporter.py "General Describe" Layer "Raster Catalog" -v
    > python describe_reporter.py -u esri.com\path-to-documentation
    > python describe_reporter.py -t -u esri.com\path-to-documentation Toolbox

    REPORT FORMAT
    {
        Filename 1: {
            Describe Object Class 1: {
                Property 1: output,
                Propetry 2: {},
            }
        }
        Filename 2: 'FILE NOT FOUND'
    }
"""

import arcpy
import pickle
import time
import sys
import os
from default_props import default_properties
from pprint import pprint
from functools import wraps
from collections import OrderedDict as od
try:
    from file_list import user_files
except ImportError as e:
    print("ERROR: Could not find list of files to be scanned. Please verify")
    print("that file_list.py is in the same directory as this script, and")
    print("that it contains a list called user_files which holds each path")
    print("to your files.")
    print("EXAMPLE: user_files = [u'C:\\Users\\andr7495\\Desktop\\KML.kml']")
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


def get_properties(user_input):
    """ Creates the properties dict by scraping the online Describe Object
        documentation, or use the default list of attributes.
    """
    if "-u" not in user_input:
        return default_properties
    else:
        try:
            url_index = user_input.index('-u') + 1
            url = user_input[url_index]
        except:  # probably going to be an IndexError, if anything
            print("ERROR: Verify that you have entered the -u flag followed by")
            print("a valid url, or do not use the -u flag to rely on the")
            print("default Property list. Exiting program.")
            raise SystemExit
        else:
            r = requests.get(url)
    if r.status_code != 200:
        print("Unable to connection to URL, loading default attribute dict.")
        return default_properties
    else:
        soup = bs(r.text, 'html.parser')
        xrefs = soup.find_all('a', class_='xref xref', href=True)
        header = u'https://pro.arcgis.com'
        properties = [(i.text, header + i['href']) for
                      i in xrefs if 'Properties' in i.text]
        all_attributes = dict()
        for element in properties:
            describe_property, url = element
            r = requests.get(url)
            soup = bs(r.text, 'html.parser')
            td_tags = soup.find_all('td')
            attributes = {t.text[:t.text.index("(Read Only)")] for
                          t in td_tags if "(Read Only)" in t.text}
            # Properties without attibutes are added as an unhashable set-object
            if attributes.__class__ == set:
                attributes = dict()
            all_attributes[describe_property] = attributes
        return all_attributes


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


def check_prop_list(user_types):
    """ Verify that the user has entered valid Describe Object types/classes and
        print a warning message for any invalid choices. If no arguments are
        provided, the report will print all Describe properties.Returns a list
        of Describe properties whose attributes will be included in the report.
    """
    if not user_types:
        queried_types = [p for p in default_properties]
    else:
        invalid_types = list()
        queried_types = list()
        [queried_types.append(k)
         if k in properties
         else invalid_types.append(k)
         for k in user_types]
        if invalid_types:
            print("WARNING! Describe Types will not be included in report:")
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
            desc_dict = od()
            for d_class in sorted(property_list):
                desc_dict[d_class] = dict()
                for p in default_properties[d_class]:
                    try:
                        desc_dict[d_class][p] = eval("arcpy.Describe(f).{0}".format(p))
                    except AttributeError:
                        if verbose_mode:
                            desc_dict[d_class][p] = 'ATTRIBUTE ERROR: Method not found'
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
    all_attributes = get_properties(user_input)
    verbose_mode = set_mode(user_input)
    cleaned_user_types = check_prop_list(user_input[2:])
    generate_report(verbose_mode, cleaned_user_types, user_files)
    print('\nfin.')
