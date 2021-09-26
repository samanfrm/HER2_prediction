#!/bin/bash

module load singularity/3.6.4

bsub -q long -J 'preprocessing_rand' -n 4 -R "span[hosts=1]" -W 8:00 -R "rusage[mem=16000]" -o "run_randimage.out" -e "run_randimage.err" singularity exec --nv ./tfgpu_1.15.4_opencv.sif /opt/intel/intelpython3/bin/python ./rand_image.py