#!/bin/sh
#PBS -q batch
#PBS -N tau10E7_vrot100_vout200
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=24
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 24 ./mine.x /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E7/vrot100/vout200/tau10E7_vrot100_vout200.input