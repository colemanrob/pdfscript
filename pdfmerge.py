
# coding: utf-8

# importing packages

import os
from PyPDF2 import PdfFileReader, PdfFileMerger


# identify two seperate locations of files

maps_dir = '/home/rob/projects/pdfscript/maps'
fsheets_dir = '/home/rob/projects/pdfscript/fsheets'


# convert dir to lists and define merger

map_files = [f for f in os.listdir(maps_dir)]
fsheet_files = [f for f in os.listdir(fsheets_dir)]
merger = PdfFileMerger()


# loop through list and map and factsheet together

for maps, fsheets in zip(map_files, fsheet_files):
    merger.append(PdfFileReader(os.path.join(maps_dir, maps), "rb"))
    merger.append(PdfFileReader(os.path.join(fsheets_dir, fsheets), "rb"))


# write output into one document

merger.write(os.path.join(maps_dir, "merged_full.pdf"))

