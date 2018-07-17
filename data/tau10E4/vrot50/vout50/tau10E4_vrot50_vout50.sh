#!/bin/sh
#PBS -q batch
#PBS -N tau10E4_vrot50_vout50
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=6
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /hpcfs/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 6 ./mine.x /hpcfs/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E4/vrot50/vout50/tau10E4_vrot50_vout50.input