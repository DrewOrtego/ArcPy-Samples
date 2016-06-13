''' Create_Grid_Index.py
    Andrew Ortego
    3/11/2015

    Creates a grid index polygon layer on top of any feature class or shapefile.
    This acts similar to the Create Index Layer geoprocessing tool available from
    ArcGIS for Desktop. This script demos how to use an array to create a feature
    class.

    Input Parameters
        (15) source_layer - the layer used to set the extent of the grid
        (16) output_layer - the full path of the grid feature-class
'''
source_layer = r'C:\Fake_geodatabase.gdb\Layer_name'
output_layer = r'C:\Fake_geodatabase.gdb\Output_layer'

import arcpy

arcpy.env.overwriteOutput = True

class Grid:
    ''' The grid object which will consist of multiple polygons. By default,
        The object creates a 10x10 grid.'''
    def __init__(self, source, output, rows=10, columns=10):
        self.source = source
        self.output = output
        self.rows = rows
        self.columns = columns
        self.cell_width, self.cell_height = self.create_cell()

    def create_cell(self):
        ''' Creates the polygons that encompass the overlay grid.
            Returns a tuple containing the width and height of a single cell.'''
        source_extent = arcpy.Describe(self.source).extent
        cell_width = (source_extent.XMax - source_extent.XMin) / self.rows
        cell_height = (source_extent.YMax - source_extent.YMin) / self.columns
        return (cell_width, cell_height)

    def create_grid(self):
        ''' Creates the grid to be overlaid on the source feature class.'''
        origin = arcpy.Describe(self.source).extent.upperLeft
        all_cells = []
        for col in range(0, self.columns):
            for row in range(0, self.rows):
                ''' Creates the points for each corner of a cell, stores this in
                    a polygon object, then appends the single polygon to the
                    array of all polygons. The final results are merged into a
                    single shapefile/feature class.'''
                upper_left = arcpy.Point(
                    origin.X + (row * self.cell_width),
                    origin.Y - (col * self.cell_height))

                upper_right = arcpy.Point(
                    origin.X + ((row + 1) * self.cell_width),
                    origin.Y - (col * self.cell_height))

                lower_right = arcpy.Point(
                    origin.X + ((row + 1) * self.cell_width),
                    origin.Y - ((col + 1) * self.cell_height))

                lower_left = arcpy.Point(
                    origin.X + (row * self.cell_width),
                    origin.Y - ((col + 1) * self.cell_height))

                cell = arcpy.Polygon(
                    arcpy.Array(
                        (upper_left, upper_right, lower_right, lower_left)))

                all_cells.append(cell)
        arcpy.CopyFeatures_management(all_cells, self.output)


if __name__ == "__main__":
    new_grid = Grid(arcpy.mapping.Layer(source_layer), output_layer)
    new_grid.create_grid()

