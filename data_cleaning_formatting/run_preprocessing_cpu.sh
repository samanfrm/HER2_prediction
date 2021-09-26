#!/bin/bash

module load singularity/3.6.4

#BSUB -J lung

# CPU queue
#BSUB -q long

# 1GB RAM, 1 GPU device
#BSUB -R "rusage[mem=8000] span[hosts=1]"

#BSUB -n 2

# Wall time of 60 minutes
#BSUB -W 20:00

#BSUB -o "/project/umb_kourosh_zarringhalam/saman/HER2/scripts/logs/TCGA_preprocessing_001.out"
#BSUB -e "/project/umb_kourosh_zarringhalam/saman/HER2/scripts/logs/TCGA_preprocessing_001.err"

singularity exec Final_OS_IO.sif  python3 /project/umb_kourosh_zarringhalam/saman/HER2/scripts/DeepPATH/DeepPATH_code/00_preprocessing/0b_tileLoop_deepzoom4.py -s 512 -e 0 -B 70 -M 20.0 -N '73,16,20,9,-4,4' -o /project/umb_kourosh_zarringhalam/saman/HER2/images/TCGA_raw_output_filtered_meansd/ "../../HER2/TCGA-BRCA_SVS_filtered/dir_010/*svs"