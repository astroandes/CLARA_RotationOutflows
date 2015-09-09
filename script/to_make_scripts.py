import os

#Example of directory: /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E5/vrot0/vout100

ppns = [6, 12, 24]
logtaus = [5,6,7]
vrots = [0,100,200,300]
vouts = [100,200,300]

for i in range(3):

    logtau = logtaus[i]
    ppn = ppns[i]

    for vrot in vrots:
        for vout in vouts:

            filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)
            path = '/lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E'+str(logtau)+'/vrot'+str(vrot)+'/vout'+str(vout)+'/'
            script = open(path+filename+'.sh', 'w')

            script.write('#!/bin/sh\n')
            script.write('#PBS -q batch\n')
            script.write('#PBS -N '+filename+'\n')
            script.write('#PBS -l mem=128mb\n')
            script.write('#PBS -l nodes=1:ppn='+str(ppn)+'\n')
            script.write('#PBS -M mc.remolina197@uniandes.edu.co\n')
            script.write('#PBS -m abe\n')
            script.write('\n')
            script.write('module load openmpi/1.8.5\n')
            script.write('cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/\n')
            script.write('mpiexec -n '+str(ppn)+' ./mine.x '+path+filename+'.input')

            script.close()
