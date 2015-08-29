#!/bin/sh
#PBS -q batch
#PBS -N test_rotationoutflowonlyrotation
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=6
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 6 ./mine.x /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA_RotationOutflows/script/tests/test_rotationoutflowonlyrotation.input

