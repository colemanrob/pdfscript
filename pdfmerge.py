
# coding: utf-8

# In[30]:

import os
from PyPDF2 import PdfFileReader, PdfFileMerger
import re


# In[31]:

maps_dir = 'C:\\Users\\ColemaRo\\Desktop\\2016 OEAS\\v5\\maps'
fsheets_dir = 'C:\\Users\\ColemaRo\\Desktop\\2016 OEAS\\v5\\fsheets'


# In[32]:

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


# In[39]:

map_files = [f for f in os.listdir(maps_dir)]
fsheet_files = [f for f in os.listdir(fsheets_dir)]
map_files.sort()
fsheet_files = natural_sort(fsheet_files)
merger = PdfFileMerger()


# In[40]:

for fsheets, maps in zip(fsheet_files, map_files):
    merger.append(PdfFileReader(os.path.join(fsheets_dir, fsheets), "rb"))
    merger.append(PdfFileReader(os.path.join(maps_dir, maps), "rb"))


# In[41]:

merger.write(os.path.join(maps_dir, "merged_full.pdf"))

