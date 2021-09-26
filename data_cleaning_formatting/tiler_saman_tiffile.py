import numpy as np
import os
import tifffile as TFF
import cv2


########################################################
mpln=512
dT=500000
mpl=512
step=512
T=0.2  ##min tissue threhsold

#########################################################
masirc='/project/umb_kourosh_zarringhalam/saman/HER2/scripts/'    ##the directory in which the code is running
masirw='/project/umb_kourosh_zarringhalam/saman/HER2/images/BCM_raw_output/'  ##the directory to write the results
masiri='/project/umb_kourosh_zarringhalam/saman/HER2/BCM_rest/'  ##the directory of images
######################################################
slides=os.listdir(masiri)


########################################################
#############now tile

for fname in slides:
    
    if not os.path.isdir(masirw+fname):
        os.mkdir(masirw+fname)
    
    
    fpath=masiri+fname
    imd=TFF.imread(fpath)

    nr, nc, dummy = np.shape(imd)
    ######read the tiles
    for i in range(0,nr-mpl-2,step):
        for j in range(0,nc-mpl-2,step):
        
            cimd=imd[i:i+mpl,j:j+mpl,:]
            
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
