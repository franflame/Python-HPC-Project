#!/bin/bash
#BSUB -J jacobi_benchmark
#BSUB -q hpc
#BSUB -W 01:00
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=8000MB]"
#BSUB -o benchmark_%J.out
#BSUB -e benchmark_%J.err

# Go to submission directory
cd $LS_SUBCWD

echo "Running in directory:"
pwd

echo "Python used:"
which python

echo "Allocated cores:"
echo $LSB_DJOB_NUMPROC

echo "Job started"
date

python benchmark_parallel.py

echo "Job finished"
date
