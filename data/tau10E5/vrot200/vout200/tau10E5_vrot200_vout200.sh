#!/bin/sh
#PBS -q batch
#PBS -N tau10E5_vrot200_vout200
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=6
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 6 ./mine.x /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E5/vrot200/vout200/tau10E5_vrot200_vout200.input