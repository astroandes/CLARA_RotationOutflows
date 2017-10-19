import os

logtau = 6
vrots = [50, 100]
vouts = [5]

for vrot in vrots:
    for vout in vouts:

        path = './vrot'+str(vrot)+'/vout'+str(vout)+'/'
        filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)

        #os.system('rm '+path+filename+'_out.ascii')
        os.system('cat '+path+filename+'_out* >> temp.txt')
        os.system('echo "x y z x_u y_u z_u x_frec escaped n_scatterings" > '+path+filename+'_out.ascii')
        os.system('grep -v "#" temp.txt >> '+path+filename+'_out.ascii')
        os.system('rm temp.txt')

        #os.system('rm '+path+filename+'_in.ascii')
        os.system('cat '+path+filename+'_in* >> temp.txt')
        os.system('echo "x y z x_u y_u z_u x_frec escaped n_scatterings" > '+path+filename+'_in.ascii')
        os.system('grep -v "#" temp.txt >> '+path+filename+'_in.ascii')
        os.system('rm temp.txt')
