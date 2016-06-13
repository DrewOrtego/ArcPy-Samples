# ArcPy-Samples/Fix_Report_URL

**Demonstrates**
* Bug fix for an issue with Esri's Report Designer utility
* Use of functions to compartmentalize functionality
* Error checking to ensure that the script will run properly on any system, and report issues in a useful manner
* Effective reporting for describing the bug-fix to Esri's development team
* Use of the BeautifulSoup4 module

**Usage:**

         Runs as a standalone script with Python 2.7.
         
**Purpose:**

         This script repairs the erroneous ```<a>``` tag's created by the Report Designer, if hyperlinks are enabled.
                
         If you're creating a report and saving it as an HTM or HTML file, the <a> tags will look like this:
                        ```html
                        <a href="True"><nobr>http://www.esri.com/</nobr></a></span>
                        ```
         This creates a hyperlink using the URL, but that link leads to a non-existent file call "True".

        This script will repair those links, and remove the redacted <nobr> tags, making the URL's function correctly.

        Occasionally the user will want to make a Table of Contents HTM file in conjunction with the report. 
        This script will detect that TOC file as long as it has the same name as the report HTM file, and update 
        the links in that TOC file to utilize the repaired HTML file.

   [More information about Report Designer](http://resources.arcgis.com/en/help/main/10.2/index.html#//004v00000002000000)
                
**Caveats:**

        * This script requires the Beautiful Soup 4 module, found here:
        http://www.crummy.com/software/BeautifulSoup/#Download
        From that zip file, move the "bs4" folder into the following directory:
        C:\Python27\ArcGIS10.x\Lib\site-packages
        
        * This script could potentially run just fine with any HTM file, so verify that you are using it to correct HTM or 
        HTML files created with the Report Designer.
        
**Work Flow:**

         Creates a new HTML file and copies the HTM file to it, line-by-line. If
         an <a> tag is found with the href-attribute set to "True", it will be
         corrected to fix that URL.
         
         As the script runs, it reports inaccessible URLs so that
         the user can double-check that address. This is useful for replacing
         any URL's which are inaccessible.
         
         If a .toc file is detected, the hyperlinks in that .toc file will be
         repaired to link to the new HTML file created in fix_report_urls. This
         is not required, but exetremely useful to customer's who need this
         functionality.
    
**Input:**

        Before running the script, update the input_htm and output_html variables on lines 101 and 102.
        
**Output:**

        An .html file with the same appearance as the .htm file, but with working
        hyperlinks. (Assuming the URL is correct.)'''
