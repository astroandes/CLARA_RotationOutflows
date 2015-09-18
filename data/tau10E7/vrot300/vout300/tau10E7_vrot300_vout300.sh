#!/bin/sh
#PBS -q batch
#PBS -N tau10E7_vrot300_vout300
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=24
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 24 ./mine.x /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E7/vrot300/vout300/tau10E7_vrot300_vout300.input