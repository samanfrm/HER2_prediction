#!/bin/bash

module load singularity/3.6.4

#module load python/2.7.9_packages/numpy/1.14.2
#module load python/2.7.9_packages/tensorflow/0.6.0 

#BSUB -J sort_Mfilter 
#BSUB -q short
#BSUB -R "rusage[mem=8000] span[hosts=1]"
#BSUB -n 2
#BSUB -W 4:00

#BSUB -o "/project/umb_kourosh_zarringhalam/saman/HER2/log_files/TCGA/SortTiles_2classes_test_norm_DCGMM.out"
#BSUB -e "/project/umb_kourosh_zarringhalam/saman/HER2/log_files/TCGA/SortTiles_2classes_test_norm_DCGMM.err" 


singularity exec Final_OP_spam.sif python3 /project/umb_kourosh_zarringhalam/saman/HER2/scripts/DeepPATH/DeepPATH_code/00_preprocessing/0d_SortTiles.py --SourceFolder=/project/umb_kourosh_zarringhalam/saman/HER2/images/TCGA_raw_output_filtered --JsonFile=/project/umb_kourosh_zarringhalam/saman/HER2/images/label_directory/TCGA_BRCA_Filtered.txt --Magnification=23 --MagDiffAllowed=0 --SortingOption=14 --PercentTest=100 --PercentValid=0 --PatientID=15 --nSplit=0