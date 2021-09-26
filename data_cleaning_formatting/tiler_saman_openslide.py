import numpy as np
import os
import openslide as opsl
import cv2


########################################################
mpln=512  ######tile size given to the CNN
dT=500000  ##maximum number of allowable tiles
mpl=512 ###tile size to read
step=512 ###step size, step=mpl means no overlap, step=mpl/2 means 50% overlap , and so on
T=0.2  ##min tissue threhsold

#########################################################
masirc='/project/umb_kourosh_zarringhalam/saman/HER2/scripts/'    ##the directory in which the code is running
masirw='/project/umb_kourosh_zarringhalam/saman/HER2/images/BCM_raw_output_op/'  ##the directory to write the results
masiri='/project/umb_kourosh_zarringhalam/saman/HER2/BCM_samples'  ##the directory of images
######################################################
slides=os.listdir(masiri)

########################################################
#############now tile

for fname in slides:
    
    if not os.path.isdir(masirw+fname):
        os.mkdir(masirw+fname)
    
    
    fpath=masiri+fname
    imd=opsl.OpenSlide(fpath)
        
    nr, nc = imd.dimensions
    ######read the tiles
    for i in range(0,nr-mpl-2,step):
        for j in range(0,nc-mpl-2,step):
        
            imdi=imd.read_region([i, j],0,[mpl, mpl])
            imdi=imdi.convert(mode='RGB')
            cimd=imdin=np.array(imdi,dtype=np.uint8)
            
            ##checkn if the tile passes QC
            imco=( np.sum(cimd>np.round(0.9*255),axis=2)==3)                
            imcb=( np.sum(cimd<3,axis=2)==3)
            
            imco=imco+imcb
            
            #####flip channels! using open cv to write images
            cimdf=np.zeros((mpl,mpl,3),dtype=np.uint8)
            cimdf[:,:,0]=cimd[:,:,2]
            cimdf[:,:,1]=cimd[:,:,1]
            cimdf[:,:,2]=cimd[:,:,0]
        
            if (np.sum(imco)/(mpl**2) < 1-T):
                
                ftw=masirw+fname+'/tile_'+str(i)+'_'+str(j)+'.jpg'  ###file to write!
                
                if not os.path.isfile(ftw):
                    cv2.imwrite(ftw,cimdf,  [cv2.IMWRITE_JPEG_QUALITY, 100])
