# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:25:13 2019

@author: jaykumar.d.padariya
"""

import rasterio

from rasterio.merge import merge

from rasterio.plot import show

import glob

import os

# File and folder paths
dirpath = r"D:\test"

out_fp = r"D:\test\anand.tif"

# Make a search criteria to select the DEM files
search_criteria = "planet_Anand_24_09_2019*.tif"

q = os.path.join(dirpath, search_criteria)

print(q)


dem_fps = glob.glob(q)

dem_fps
src_files_to_mosaic = []
for fp in dem_fps:
       src = rasterio.open(fp)
       src_files_to_mosaic.append(src)
    
       
src_files_to_mosaic
mosaic, out_trans = merge(src_files_to_mosaic)
show(mosaic, cmap='terrain')
out_meta = src.meta.copy()
out_meta.update({"driver": "GTiff",
                   "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                  "transform": out_trans,
                   "crs": "+proj=utm +zone=43 +ellps=GRS80 +units=m +no_defs "
                   }
                  )
  
       
       # Write the mosaic raster to disk
with rasterio.open(out_fp, "w", **out_meta) as dest:
      dest.write(mosaic)
   