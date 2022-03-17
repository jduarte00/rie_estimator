import numpy as np
import pandas as pd
from numpy import linalg as LA

__author__ = 'José Antonio Duarte'
__credit__ = 'José Antonio Duarte'
__status__ = 'beta'
__version__ = '0.1.0'
__all__ = ['get_rie', 'returnsStandardization']


def returnsStandardization(returns):
    returns_wth_mean = returns - np.mean(returns, axis=0)
    hat_sigma = np.sqrt((returns_wth_mean**2).sum(axis=1))
    r_tilde = returns_wth_mean.divide(hat_sigma, axis=0)
    X = r_tilde / np.std(r_tilde)
    return X

# The returns should be a Dataframe of size T X N without NULL values


def get_rie(returns, normalize=False):
    def get_s_k(index_lambda, N):
        return 1/N * (sum(1/(z_k[index_lambda] - lambdas)) - 1/(z_k[index_lambda] - lambdas[index_lambda]))

    # T is the number of observations, N is the number of assets
    T, N = returns.shape
    RIE_estimator = np.zeros((N, N), dtype=float)
    if normalize:
        returns = returnsStandardization(returns)
    # Calculation of the sample correlation matrix
    E = np.corrcoef(returns.T)
    # The eigenvalues and eigenvectors of the returns are obtained
    lambdas, u_ks = LA.eigh(E)
    u_ks = u_ks.T
    n_lambda = lambdas[0]
    q = float(N/T)
    sigma_sq = (n_lambda)/(1 - np.sqrt(q))**2
    lambda_plus = n_lambda*((1+np.sqrt(q))/(1 - np.sqrt(q)))**2
    # Get z_k
    z_k = lambdas - (1j / np.sqrt(N))
    # Get s_k(z_k)
    s_k = list(map(lambda index_lambda: get_s_k(
        index_lambda, N), np.argsort(lambdas)))
    # Get \xi_k^{RIE}
    xi_k = lambdas / np.abs(1 - q + q * z_k * s_k)**2
    # Get stieltjes g_{mp}(z)
    g_mp = (z_k + sigma_sq*(q-1) - (np.sqrt(z_k - n_lambda)
            * np.sqrt(z_k - lambda_plus)))/(2*q*z_k*sigma_sq)
    # Get gamma_k(z_k)
    gamma_k = sigma_sq * ((np.abs(1 - q + q*z_k*g_mp)**2)/(lambdas))
    # Get \hat{xh}_k
    xi_hat = list(map(lambda xi, gamma: xi *
                  gamma if gamma > 1 else xi, xi_k, gamma_k))
    # Get RIE
    for xi, u_i in zip(xi_hat, u_ks):
        RIE_estimator += xi*(u_i.reshape(-1, 1) @ u_i.reshape(-1, 1).T)

    return RIE_estimator
