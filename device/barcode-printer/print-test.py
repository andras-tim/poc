#!/usr/bin/env python

# Print a file to the printer

import cups
from xhtml2pdf import pisa

def main():
    # Filename for temp file
    filename = "/tmp/print.pdf"

    # generate content
    xhtml = "<h1>Test print</h1>\n"
    xhtml += "<h2>This is printed from within a Python application</h2>\n"
    xhtml += "<p style=\"color:red;\">Coloured red using css</p>\n"

    pdf = pisa.CreatePDF(xhtml, file(filename, "w"))
    if not pdf.err:
        # Close PDF file - otherwise we can't read it
        pdf.dest.close()

        # print the file using cups
        conn = cups.Connection()
        # Get a list of all printers
        printers = conn.getPrinters()
        for printer in printers:
            # Print name of printers to stdout
            print printer,
        printers[printer]["device-uri"]
        # get first printer from printer list
        printer_name = printers.keys()[0]
        conn.printFile(printer_name, filename, "Python_Status_print", {})
    else:
        print "Unable to create pdf file"

if __name__=="__main__":
    main()
