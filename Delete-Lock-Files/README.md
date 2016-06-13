#Delete-Lock-Files

**Demonstrates**
* Use of a Python Add-In and how to utilize the provided event functions.
* Use of the glob module

**Purpose:**

    Use this script as a Python Add-In. This Add-In will delete all lock
    files in each workspace contained within an MXD's Table of Contents.
    This can be useful when user-permissions do not allow for the normal
    deletion of lock files after closing ArcMap.
    
**Work Flow:**

    Using the closeDocument event, the Add-In will execute once the user
    closes ArcMap. Then, it scans each layer in the Table of Contents for
    it's corresponding workspace, and deletes any .lock files found in that
    workspace.
    
**Input:**

    Set this script up as a Python Add-In, as seen here:
    www.arcgis.com/home/item.html?id=5f3aefe77f6b4f61ad3e4c62f30bff3b
    
**Output:**

    Deletes any files with the .loc or .lock extensions.
