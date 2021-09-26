import os
import cv2

mydir='/project/umb_kourosh_zarringhalam/saman/HER2/images/label_directory/2classes_unannotated_extra/Tiles_random_selected'
files = os.listdir(mydir)
for mfile in files:
    img=cv2.imread(mydir+ '/'+ mfile)
    if(img.shape[0]<512 or img.shape[1]<512):
        os.remove(str(mydir + '/' + mfile))


