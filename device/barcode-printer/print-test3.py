#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39
import cups


COMPANY = "Company"


class Printer(object):
    def __init__(self):
        self.conn = cups.Connection()

    def PrintPdf(self, pdf_file, printer_name=None):
        if printer_name is None:
            printer_name = self.conn.getDefault()

        options = {
            #'BrCutLabel': '1'
            #'BrCutAtEnd': 'ON'
            #'BrMirror': 'OFF'
            #'BrPriority': 'BrSpeed'
            #'Resolution': 'Normal'
            #'BrHalftonePattern': 'BrErrorDiffusion'
            #'BrBrightness': '0'
            #'BrContrast': '0'
            #'PageSize': '29x90'
            #'PageRegion': '29x90'
            #'BrMargin': '3'
        }
        job_id = self.conn.printFile(printer_name, pdf_file, "Test print from Python", options)

        print("Job ID: %d" % job_id)


class PdfGenerator(object):
    page_width = 90*mm
    page_height = 29*mm

    margin_left = 3*mm
    margin_top = 2*mm
    margin_right = 4*mm
    margin_bottom = 2*mm

    inner_left = margin_left
    inner_top = page_height - margin_top
    inner_right = page_width - margin_right
    inner_bottom = margin_bottom
    inner_width = inner_right - margin_left
    inner_height = inner_top - margin_bottom

    def generate_label(self, pdf_file, data, title):
        canv = self._create_new_canvas(pdf_file)

        canv.setAuthor(COMPANY)
        canv.setTitle(title)
        canv.setSubject(data)

        #self._draw_border(canv)
        self._draw_logo(canv, self.inner_left + 1*mm, self.inner_top - 8*mm, "logo.gif")
        self._draw_title(canv, self.inner_left + 30*mm, self.inner_top - 7*mm, title)
        self._draw_barcode(canv, self.inner_bottom + 5*mm, data, bar_height=10*mm)

        canv.showPage()
        canv.save()

    def _create_new_canvas(self, pdf_file):
        return canvas.Canvas(pdf_file, pagesize=(self.page_width, self.page_height))

    def _draw_border(self, canv):
        canv.roundRect(self.margin_left, self.margin_bottom, self.inner_width, self.inner_height, radius=5, stroke=1, fill=0)

    @staticmethod
    def _draw_title(canv, x, y, title):
        canv.setFont('Helvetica', 12)
        canv.drawString(x, y, title)

    @staticmethod
    def _draw_logo(canv, x, y, image_file):
        canv.drawImage(image_file, x, y, 28*mm, 7*mm)

    def _draw_barcode(self, canv, y, data, bar_height=20*mm):
        # http://en.wikipedia.org/wiki/Code_39

        #barcode = code39.Standard39(data, barWidth=0.5*mm, barHeight=bar_height, stop=True, checksum=True)
        barcode = code39.Standard39(data, barWidth=0.55*mm, barHeight=bar_height, stop=True, checksum=False)
        barcode.drawOn(canv, self.inner_left + (self.inner_width - barcode.width) / 2, y)

        split_data = self._split_barcode_data(data, 3)
        canv.setFont('Helvetica', 10)
        canv.drawCentredString(self.inner_left + self.inner_width / 2, y - 4*mm, split_data)

    @staticmethod
    def _split_barcode_data(data, nth_characters):
        (company, article) = data.split("-", 1)
        article = ' '.join([article[i:i+nth_characters] for i in range(0, len(article), nth_characters)])
        return "%s - %s" % (company, article)


def main():
    pdf = PdfGenerator()
    printer = Printer()
    with tempfile.NamedTemporaryFile() as temp:
        temp.close()
        #pdf_file = temp.name
        pdf_file = "label_example.pdf"

        pdf.generate_label(pdf_file, "PS-SYHEKH", "Festo pisztoly mosó")
        #printer.PrintPdf(pdf_file)

if __name__ == '__main__':
    main()