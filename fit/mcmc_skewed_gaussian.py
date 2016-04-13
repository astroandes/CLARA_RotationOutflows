from numpy import *
from scipy.special import erf

#FUNCTIONS

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

def likelihood(y_obs, y_mod):
    chi_squared_y = (1.0/2.0)*sum((y_obs - y_mod)**2)
    return -chi_squared_y


#MCMC
def mcmc_skewed_gaussian(x_d, y_d):

    #Initial guess
    amplitude_neg0 = 65
    center_neg0 = -4
    sigma_neg0 = 9
    gamma_neg0 = -4
    amplitude_pos0 = 38
    center_pos0 = 2
    sigma_pos0 = 8
    gamma_pos0 = 4

    x_fit0 = x_d
    y_fit0 = sum_2_skewed_gaussian(x_fit0, amplitude_neg0, center_neg0, sigma_neg0, gamma_neg0, amplitude_pos0, center_pos0, sigma_pos0, gamma_pos0)


    #Empty arrays to save steps

    amplitude_neg_walk = empty((0))
    center_neg_walk = empty((0))
    sigma_neg_walk = empty((0))
    gamma_neg_walk = empty((0))
    amplitude_pos_walk = empty((0))
    center_pos_walk = empty((0))
    sigma_pos_walk = empty((0))
    gamma_pos_walk = empty((0))

    l_walk = empty((0))


    #Initial values

    amplitude_neg_walk = append(amplitude_neg_walk, amplitude_neg0)
    center_neg_walk = append(center_neg_walk, center_neg0)
    sigma_neg_walk = append(sigma_neg_walk, sigma_neg0)
    gamma_neg_walk = append(gamma_neg_walk, gamma_neg0)
    amplitude_pos_walk = append(amplitude_pos_walk, amplitude_pos0)
    center_pos_walk = append(center_pos_walk, center_pos0)
    sigma_pos_walk = append(sigma_pos_walk, sigma_pos0)
    gamma_pos_walk = append(gamma_pos_walk, gamma_pos0)

    l_walk = append(l_walk, likelihood(y_d, y_fit0))


    #MCMC Loop

    n_steps = 30000

    for i in range(n_steps):

        amplitude_neg_prime = random.normal(amplitude_neg_walk[i], 0.1)
        center_neg_prime = random.normal(center_neg_walk[i], 0.1)
        sigma_neg_prime = random.normal(sigma_neg_walk[i], 0.1)
        gamma_neg_prime = random.normal(gamma_neg_walk[i], 0.1)

        amplitude_pos_prime = random.normal(amplitude_pos_walk[i], 0.1)
        center_pos_prime = random.normal(center_pos_walk[i], 0.1)
        sigma_pos_prime = random.normal(sigma_pos_walk[i], 0.1)
        gamma_pos_prime = random.normal(gamma_pos_walk[i], 0.1)

        y_previous = sum_2_skewed_gaussian(x_d, amplitude_neg_walk[i], center_neg_walk[i], sigma_neg_walk[i], gamma_neg_walk[i], amplitude_pos_walk[i], center_pos_walk[i], sigma_pos_walk[i], gamma_pos_walk[i])
        y_prime = sum_2_skewed_gaussian(x_d, amplitude_neg_prime, center_neg_prime, sigma_neg_prime, gamma_neg_prime, amplitude_pos_prime, center_pos_prime, sigma_pos_prime, gamma_pos_prime)

        l_previous = likelihood(y_d, y_previous)
        l_prime = likelihood(y_d, y_prime)

        a = l_prime / l_previous

        if(a <= 1.0):
            amplitude_neg_walk = append(amplitude_neg_walk, amplitude_neg_prime)
            center_neg_walk = append(center_neg_walk, center_neg_prime)
            sigma_neg_walk = append(sigma_neg_walk, sigma_neg_prime)
            gamma_neg_walk = append(gamma_neg_walk, gamma_neg_prime)
            amplitude_pos_walk = append(amplitude_pos_walk, amplitude_pos_prime)
            center_pos_walk = append(center_pos_walk, center_pos_prime)
            sigma_pos_walk = append(sigma_pos_walk, sigma_pos_prime)
            gamma_pos_walk = append(gamma_pos_walk, gamma_pos_prime)

            l_walk = append(l_walk, l_prime)

        else:

            b = random.random()

            if( log(b) <= -a):
                amplitude_neg_walk = append(amplitude_neg_walk, amplitude_neg_prime)
                center_neg_walk = append(center_neg_walk, center_neg_prime)
                sigma_neg_walk = append(sigma_neg_walk, sigma_neg_prime)
                gamma_neg_walk = append(gamma_neg_walk, gamma_neg_prime)
                amplitude_pos_walk = append(amplitude_pos_walk, amplitude_pos_prime)
                center_pos_walk = append(center_pos_walk, center_pos_prime)
                sigma_pos_walk = append(sigma_pos_walk, sigma_pos_prime)
                gamma_pos_walk = append(gamma_pos_walk, gamma_pos_prime)

                l_walk = append(l_walk, l_prime)

            else:
                amplitude_neg_walk = append(amplitude_neg_walk, amplitude_neg_walk[i])
                center_neg_walk = append(center_neg_walk, center_neg_walk[i])
                sigma_neg_walk = append(sigma_neg_walk, sigma_neg_walk[i])
                gamma_neg_walk = append(gamma_neg_walk, gamma_neg_walk[i])
                amplitude_pos_walk = append(amplitude_pos_walk, amplitude_pos_walk[i])
                center_pos_walk = append(center_pos_walk, center_pos_walk[i])
                sigma_pos_walk = append(sigma_pos_walk, sigma_pos_walk[i])
                gamma_pos_walk = append(gamma_pos_walk, gamma_pos_walk[i])

                l_walk = append(l_walk, l_previous)


    #Best values

    amplitude_neg = amplitude_neg_walk[-1]
    center_neg = center_neg_walk[-1]
    sigma_neg = sigma_neg_walk[-1]
    gamma_neg = gamma_neg_walk[-1]
    amplitude_pos = amplitude_pos_walk[-1]
    center_pos = center_pos_walk[-1]
    sigma_pos = sigma_pos_walk[-1]
    gamma_pos = gamma_pos_walk[-1]

    print 'amplitude_neg = ', amplitude_neg
    print 'center_neg = ', center_neg
    print 'sigma_neg = ', sigma_neg
    print 'gamma_neg = ', gamma_neg
    print 'amplitude_pos = ', amplitude_pos
    print 'center_pos = ', center_pos
    print 'sigma_pos = ', sigma_pos
    print 'gamma_pos = ', gamma_pos

    return amplitude_neg, center_neg, sigma_neg, gamma_neg, amplitude_pos, center_pos, sigma_pos, gamma_pos
