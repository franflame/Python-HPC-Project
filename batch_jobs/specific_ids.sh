#!/bin/bash
#BSUB -J specific_ids
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=5GB]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -n 1
#BSUB -o required_logs/T1/specific_ids_%J.out
#BSUB -e required_logs/T1/specific_ids_%J.err
python3 src/specific_ids.py 156 1573
