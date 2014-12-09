#!/usr/bin/env python

#!/usr/bin/env python2

import cups
import labels
from reportlab import graphics

# Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 8 rows of
# labels. Each label is 90mm x 25mm with a 2mm rounded corner. The margins are
# automatically calculated.
specs = labels.Specification(90, 29, 1, 1, 83, 25, left_margin=3, top_margin=2, corner_radius=2)

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label(label, width, height, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    label.add(graphics.shapes.String(2, 2, str(obj), fontName="Helvetica", fontSize=40))

# Create the sheet.
sheet = labels.Sheet(specs, draw_label, border=True)

# Add a couple of labels.
sheet.add_label("Hello")

# Save the file and we are done.
sheet.save('basic.pdf')

conn = cups.Connection()
#print (conn.printFile(conn.getDefault(), 'basic.pdf', "Python_Status_print", {
#    'BrCutLabel': '1'
#    'BrCutAtEnd': 'ON'
#    'BrMirror': 'OFF'
#    'BrPriority': 'BrSpeed'
#    'Resolution': 'Normal'
#    'BrHalftonePattern': 'BrErrorDiffusion'
#    'BrBrightness': '0'
#    'BrContrast': '0'
#    'PageSize': '29x90'
#    'PageRegion': '29x90'
#    'BrMargin': '3'
#}))


print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))
