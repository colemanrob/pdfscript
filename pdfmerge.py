
# coding: utf-8

# In[9]:

import os
from PyPDF2 import PdfFileReader, PdfFileMerger


# In[38]:

maps_dir = '/home/rob/projects/pdfscript/maps'
fsheets_dir = '/home/rob/projects/pdfscript/fsheets'


# In[39]:

map_files = [f for f in os.listdir(maps_dir)]
fsheet_files = [f for f in os.listdir(fsheets_dir)]
merger = PdfFileMerger()


# In[40]:

for maps, fsheets in zip(map_files, fsheet_files):
    merger.append(PdfFileReader(os.path.join(maps_dir, maps), "rb"))
    merger.append(PdfFileReader(os.path.join(fsheets_dir, fsheets), "rb"))


# In[42]:

merger.write(os.path.join(maps_dir, "merged_full.pdf"))

