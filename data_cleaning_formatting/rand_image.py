# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import cv2
import numpy as np
import random

# %%

def concat_tile(im_list_2d):
    hor=[]
    for im_list_h in im_list_2d:
        try:
            hor.append(cv2.hconcat(im_list_h))
        except:
            continue 
    return cv2.vconcat(hor)

# %%
mydir="/project/umb_kourosh_zarringhalam/saman/HER2/images/TCGA_raw_output_filtered"
target_dir="/project/umb_kourosh_zarringhalam/saman/HER2/scripts/"
os.chdir(mydir)
# get a number of tiles you want to randomly select for each slide
rand_num=50
# number of slides based on subdirectories
tile_size=512

# %%
subdirs = [x[0] for x in os.walk(mydir)]
target_dirs=[]
for subdir in subdirs:
    if('23.0' in subdir):
        target_dirs.append(subdir)

# %%
#print(target_dirs)
vert=[]
for subdir in target_dirs[:50]:
    try:
       hor=[]
       print(subdir)
       files = os.listdir(subdir)
       print("lenght is: " + str(len(files)))
       if(len(files)!=0):
          for j in range(rand_num):
             #index = random.randrange(0, len(files))
             hor.append(cv2.imread(subdir+ '/'+ files[j]))    
          vert.append(hor)
    except:
       continue
print("concating all tiles into 2D matrice image...")
im_tile = concat_tile(vert)
print("Writing the result...")
cv2.imwrite(str(target_dir+'TCGA_concat_image_normalized_0-50_DCGMM.jpg'), im_tile)
