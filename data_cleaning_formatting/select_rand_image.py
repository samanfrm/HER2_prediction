

## Saman Farahmand
## This python script seelct random tiles from each slide


# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import cv2
import numpy as np
import random
import shutil

# %%
mydir="/project/umb_kourosh_zarringhalam/saman/HER2/images/TCGA_raw_output_filtered"
target_dir="/project/umb_kourosh_zarringhalam/saman/HER2/scripts/"
os.chdir(mydir)
# get a number of tiles you want to randomly select for each slide
rand_num=100
# number of slides based on subdirectories
tile_size=512

# %%
subdirs = [x[0] for x in os.walk(mydir)]
target_dirs=[]
for subdir in subdirs:
    if('20.0' in subdir):
        target_dirs.append(subdir)

# %%
#print(target_dirs)
vert=[]
for subdir in target_dirs:
       print(subdir)
       if not os.path.exists(str(subdir.strip('20.0') + '22.0')):
           os.mkdir(str(subdir.strip('20.0') + '22.0'))
       files = os.listdir(subdir)
       print("lenght is: " + str(len(files)))
       if(len(files)!=0):
          for j in range(rand_num):
             index = random.randrange(0, len(files))
             src=str(subdir +'/' +files[index])
             trg=str(subdir.strip('20.0') + '22.0')
             shutil.copy(src, trg)            
