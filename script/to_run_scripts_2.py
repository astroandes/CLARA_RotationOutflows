import os

logtaus = [5,6]
vrots = [50,100]
vouts = [25,50,75]

for i in range(2):

    logtau = logtaus[i]
    vrot = vrots[i]

    for vout in vouts:

	filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)
	path = '/lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E'+str(logtau)+'/vrot'+str(vrot)+'/vout'+str(vout)+'/'
	os.system('qsub '+path+filename+'.sh')
