#!/bin/bash

module load singularity/3.6.4

bsub -q long -J 'preprocessing_BCM' -n 4 -R "span[hosts=1]" -W 100:00 -R "rusage[mem=16000]" -o "preprocessing_BCM-ali_rest.out" -e "preprocessing_BCM-ali_rest.err" singularity exec --nv ./tfgpu_1.15.4_opencv.sif /opt/intel/intelpython3/bin/python ./tiler_saman_tiffile.py 