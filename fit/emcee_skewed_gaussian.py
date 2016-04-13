from numpy import *
from scipy.interpolate import interp1d
from scipy.special import erf
import emcee
import os
import corner
import matplotlib.pyplot as plt
#FUNCTIONS

#Bifurcation index
def find_bifurcation_index(intensities):
    i_prev = 0
    bif_index = -1

    intensities_length = len(intensities)
    start_index = 0.3*intensities_length
    end_index = 0.7*intensities_length

    intensities = intensities[start_index:end_index]

    for i in range(len(intensities)-1):
        i_curr = intensities[i]
        i_next = intensities[i+1]
        if(i_prev >= i_curr and i_curr<=i_next):
            bif_index = i
        i_prev = i_curr

    if (bif_index==-1):
        return intensities_length/2
    else:
        return bif_index+start_index

#Based on the definition in: https://github.com/lmfit/lmfit-py/blob/master/lmfit/lineshapes.py
def gaussian(x, amplitude, center, sigma):
    """1 dimensional gaussian:
    gaussian(x, amplitude, center, sigma)
    """
    return (amplitude/(sqrt(2*pi)*sigma)) * exp(-(1.0*x-center)**2 /(2*sigma**2))

#Based on the definition in: https://github.com/lmfit/lmfit-py/blob/master/lmfit/lineshapes.py
def sum_2_skewed_gaussian(x, amplitude_neg, center_neg, sigma_neg, gamma_neg, amplitude_pos, center_pos, sigma_pos, gamma_pos):
    """Gaussian, skewed with error function, equal to
     gaussian(x, center, sigma)*(1+erf(beta*(x-center)))
    with beta = gamma/(sigma*sqrt(2))
    with  gamma < 0:  tail to low value of centroid
          gamma > 0:  tail to high value of centroid
    see http://en.wikipedia.org/wiki/Skew_normal_distribution
    """
    asym_neg = 1 + erf(gamma_neg*(x-center_neg)/(sqrt(2.0)*sigma_neg))
    g_neg = asym_neg * gaussian(x, amplitude_neg, center_neg, sigma_neg)

    asym_pos = 1 + erf(gamma_pos*(x-center_pos)/(sqrt(2.0)*sigma_pos))
    g_pos = asym_pos * gaussian(x, amplitude_pos, center_pos, sigma_pos)

    return g_neg+g_pos



def lnprob(param, x_d, y_d):
    amplitude_neg, center_neg, sigma_neg, gamma_neg, amplitude_pos, center_pos, sigma_pos, gamma_pos = param

    if (0.0<amplitude_neg<500.0) and (-50<center_neg<30) and (0<sigma_neg<50) and (-10<gamma_neg<10) and (0.0<amplitude_pos<500.0) and (-30<center_pos<50) and (0<sigma_pos<50) and (-10<gamma_pos<10):
        y_m = sum_2_skewed_gaussian(x_d, amplitude_neg, center_neg, sigma_neg, gamma_neg, amplitude_neg, center_neg, sigma_neg, gamma_neg)
        chi_squared = (1.0/2.0)*sum((y_d-y_m)**2)
        return -chi_squared
    return -inf


#emcee
def emcee_skewed_gaussian(x_d, y_d):

    # bifurcation_index = find_bifurcation_index(y_d)
    #
    # #First guess
    # amplitude_neg_0 = max(y_d[0:bifurcation_index+1])
    # center_neg_0 = mean(x_d[0:bifurcation_index+1])
    # sigma_neg_0 = std(x_d[0:bifurcation_index+1])
    # gamma_neg_0 = -2
    # amplitude_pos_0 = max(y_d[bifurcation_index:-1])
    # center_pos_0 = mean(x_d[bifurcation_index:-1])
    # sigma_pos_0 = std(x_d[bifurcation_index:-1])
    # gamma_pos_0 = 2

    half = len(y_d)/2

    #First guess
    amplitude_neg_0 = 12*max(y_d[0:half+1])
    center_neg_0 = mean(x_d[0:half+1])
    sigma_neg_0 = std(x_d[0:half+1])
    gamma_neg_0 = -2
    amplitude_pos_0 = 12*max(y_d[half:-1])
    center_pos_0 = mean(x_d[half:-1])
    sigma_pos_0 = std(x_d[half:-1])
    gamma_pos_0 = 2

    first_guess = [amplitude_neg_0, center_neg_0, sigma_neg_0, gamma_neg_0, amplitude_pos_0, center_pos_0, sigma_pos_0, gamma_pos_0]


    #Running emcee
    ndim = 8
    nwalkers = 240
    nsteps = 500

    pos = [first_guess+ 1e-3*random.randn(ndim) for i in range(nwalkers)]

    sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x_d, y_d), threads=8)

    sampler.run_mcmc(pos, nsteps, rstate0=random.get_state())

    # Saving results
    samples_fc = sampler.flatchain

    savetxt('sampler_flatchain.dat', samples_fc, delimiter=',')

    #This number should be between approximately 0.25 and 0.5 if everything went as planned.
    print("Mean acceptance fraction: {0:.3f}".format(mean(sampler.acceptance_fraction)))

    #Discard the initial 50 steps
    samples = sampler.chain[:, 50:, :].reshape((-1, ndim))

    samples[:, 2] = exp(samples[:, 2])
    amplitude_neg_mcmc, center_neg_mcmc, sigma_neg_mcmc, gamma_neg_mcmc, amplitude_pos_mcmc, center_pos_mcmc, sigma_pos_mcmc, gamma_pos_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]), zip(*percentile(samples, [16, 50, 84], axis=0)))

    print 'amplitude_neg = ', amplitude_neg_mcmc
    print 'center_neg = ', center_neg_mcmc
    print 'sigma_neg = ', sigma_neg_mcmc
    print 'gamma_neg = ', gamma_neg_mcmc
    print 'amplitude_pos = ', amplitude_pos_mcmc
    print 'center_pos = ', center_pos_mcmc
    print 'sigma_pos = ', sigma_pos_mcmc
    print 'gamma_pos = ', gamma_pos_mcmc

    

    #fig = corner.corner(samples, labels=["$a_n$", "$c_n$", "$s_n$, $g_n$", "$a_p$", "$c_p$", "$s_p$, $g_p$"])
    #fig = corner.corner(samples)
    #fig.savefig("triangle.png")

    return amplitude_neg_mcmc[0], center_neg_mcmc[0], sigma_neg_mcmc[0], gamma_neg_mcmc[0], amplitude_pos_mcmc[0], center_pos_mcmc[0], sigma_pos_mcmc[0], gamma_pos_mcmc[0]
