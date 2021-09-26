# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import cv2
import os


# %%
img_list=pd.read_csv('img_list.txt',sep='\t',header=None)


# %%
# 2nd column: 'positive/test_TCGA-EW-A1OZ-01Z-00-DX1_113_9.jpeg'
# 1st column: '/project/umb_kourosh_zarringhalam/saman/HER2/images/TCGA_raw_output_filtered/TCGA-EW-A1OZ-01Z-00-DX1_files/20.0/113_9.jpeg'
magnification='20.0'
for i in range(len(img_list)):
    src_file=str(img_list.iloc[i,1])
    #print(src_file)
    src_img=cv2.imread(src_file)
    
    trg_file=str(img_list.iloc[i,0])
    trg_fname=trg_file.split('/')[-1]
    trg_dir='/'.join(trg_file.split('/')[:-1])
    trg_dir=str(trg_dir.replace('/20.0','/21.0/'))
    #print(str(trg_dir + trg_fname))
    if not os.path.exists(trg_dir):
        os.mkdir(trg_dir)
    try:
        cv2.imwrite(str(trg_dir + trg_fname),src_img)
    except:
        continue


