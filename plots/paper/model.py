import os
import numpy as np
import matplotlib.pyplot as plt

def get_unit_r_sphere(data):
    '''Re-scale positions on the sphere at which the photons escaped.'''
    r_norm = np.sqrt(data['x']**2 + data['y']**2 + data['z']**2)
    x_sphere = data['x'] / r_norm
    y_sphere = data['y'] / r_norm
    z_sphere = data['z'] / r_norm
    return x_sphere, y_sphere, z_sphere

def get_atom_velocities(x_unitary, y_unitary, z_unitary, vrot):
    '''Defines new atom velocities based on vrot (vr).'''
    v_x = - y_unitary * vrot
    v_y = x_unitary * vrot
    v_z = np.zeros(len(z_unitary))
    return {'x':v_x, 'y':v_y, 'z':v_z}

def doppler_shift(data, vrot=0.0, v_th=12.86):
    '''Updates old_data adding doppler shifts. the result is stored in new_data.'''
    new_data = data.copy()
    new_data['x'], new_data['y'], new_data['z'] = get_unit_r_sphere(data)

    atom_velocities = get_atom_velocities(new_data['x'], new_data['y'], new_data['z'], vrot=vrot)

    new_data['x_frec'] = data['x_frec']
    new_data['x_frec'] += atom_velocities['x']*data['k_x']/v_th
    new_data['x_frec'] += atom_velocities['y']*data['k_y']/v_th
    new_data['x_frec'] += atom_velocities['z']*data['k_z']/v_th

    return new_data

def read_data(vrot=0, vout=5, logtau=6, input_dir="../../data/"):
    '''Reads the data.'''
    tau_name = 'tau10E' + str(logtau)
    vrot_name = 'vrot' + str(vrot)
    vout_name = 'vout' + str(vout)
    filename = tau_name + '_' + vrot_name + '_' + vout_name + '_out.ascii'
    fname = os.path.join(input_dir, tau_name, vrot_name, vout_name, filename)

    dtype = [('x', 'f8'), ('y', 'f8'), ('z', 'f8'),
             ('k_x', 'f8'), ('k_y', 'f8'), ('k_z', 'f8'),
             ('x_frec', 'f8'), ('escaped', 'i8'), ('n_scattering', 'i8')]

    df = np.loadtxt(fname, skiprows=1, dtype=dtype)
    df = df[df['escaped']==0]
    return df

def filter_by_theta(data, min_theta, max_theta):
    '''Returns data that escaped within the min and max angles.'''
    cos_theta_k_out = np.abs(data['k_z'])
    ii = (cos_theta_k_out < np.abs(np.cos(min_theta)))
    ii = ii & (cos_theta_k_out > np.abs(np.cos(max_theta)))
    return data[ii]

def filter_by_direction(data):
    '''Returns only the x_frec_escaped between those upper and lower angles (red and blue).'''
    r_mag = (data['x']**2 + data['y']**2)**0.5
    r_x = data['x']/r_mag
    r_y = data['y']/r_mag
    
    dot = r_x*data['k_x'] + r_y*data['k_y']
    proj_x = data['k_x'] - r_x*dot
    proj_y = data['k_y'] - r_y*dot
    
    perp_x = -r_y
    perp_y = r_x
    
    para = proj_x*perp_x + proj_y*perp_y
    
    inds = np.where(para >= 0) #parallel (red)
    inds_c = np.where(para < 0) #antiparallel (blue)
    
    return data[inds], data[inds_c]

def bins_to_x(bins):
    '''Convert histogram bins to n-1 dim array of x coordinates.'''
    xs = []
    for i in range(len(bins)-1):
        xs.append( (bins[i]+bins[i+1])/2.0 )
    xs = np.array(xs)
    return xs

def get_spectra(data, v_th=12.86, as_hist=True):
    '''Returns the spectrum in velocity units.'''
    velocity = -data['x_frec']*v_th
    n, b = np.histogram(velocity, bins=50)
    n = n / n.sum()
    if (as_hist):
        return b, n
    else:
        return bins_to_x(b), n

def plot_spectra(x, y, ax, alpha=1.0, lw=2, ls='-', c='k', label='label'):
    '''Basic plot of spectra.'''
    ax.hist(x, weights=y, histtype='step', fill=False, 
            normed=True, color=c, linewidth=lw, bins=50, 
            alpha=alpha, linestyle=ls, label=label)
    
def main(vrot, vout, logtau, min_theta, max_theta):
    '''Main. Shows an example of its use.'''
    # Input
    vrot0 = 0

    data = read_data(vrot0, vout, logtau)
    doppler = doppler_shift(data, vrot=vrot)
    doppler_theta = filter_by_theta(doppler, min_theta, max_theta)
    x, y = get_spectra(doppler_theta, as_hist=False)
    
    return x, y


# MAIN
if __name__ == "__main__":
    main(vrot=150, vout=5, logtau=6, min_theta=np.pi/2.0-0.15, 
         max_theta=np.pi/2.0)
