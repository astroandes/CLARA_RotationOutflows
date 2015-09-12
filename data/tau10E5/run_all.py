import os

logtaus = [5]
vrots = [0,100,200,300]
vouts = [100,200,300]

for logtau in logtaus:
    for vrot in vrots:
        for vout in vouts:

            filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)
            path = '/lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E'+str(logtau)+'/vrot'+str(vrot)+'/vout'+str(vout)+'/'
            
	    os.system('qsub '+path+filename+'.sh')
