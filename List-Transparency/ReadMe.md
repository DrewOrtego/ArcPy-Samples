# List-Transparency
Python Script Tool to be used within a toolbox (.tbx) in ArcMap/Catalog

**Demonstrates**
* Use of Script Tool paradigms
* Try/Except block used for creating meaningful output
* Use of list comprehension for faster processing

**Usage:**

    Open the included Toolbox (.tbx) file in ArcMap and add a new tool or
    set the source of the provided Script Tool to be the included python
    script.
   
**Purpose:**

    Lists all layers in a Map Document and their corresponding transparency value.
    This is written to be ran as a Script Tool in ArcMap or ArcCatalog.
    
**Work Flow:**

    Straight forward implementation of scanning each layer in a map document's
    table of contents, and determining if it has a transparency attribute.
    
**Input:**

    A the file path to a Map Document.
    
**Output:**

    Prints messages to the ArcMap results window.
