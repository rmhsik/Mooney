import numpy as np

def coefficients(n1, n2, theta_i):
    theta_t = np.arcsin(n1 * np.sin(theta_i) / n2)
    if np.isnan(theta_t):
        theta_t = np.pi/2

    r_p = (n2 * np.cos(theta_i) - n1 * np.cos(theta_t)) / \
        (n1 * np.cos(theta_i) + n2 * np.cos(theta_t))
    t_p = 2 * n1 * np.cos(theta_i) / \
        (n2 * np.cos(theta_i) + n1 * np.cos(theta_t))
    r_s = (n1 * np.cos(theta_i) - n2 * np.cos(theta_t)) / \
        (n1 * np.cos(theta_i) + n2 * np.cos(theta_t))
    t_s = 2 * n1 * np.cos(theta_i) / \
        (n1 * np.cos(theta_i) + n2 * np.cos(theta_t))

    cos_t = np.cos(theta_t)
    cos_i = np.cos(theta_i)

    R_s = np.absolute(r_s)**2
    R_p = np.absolute(r_p)**2
    T_s = np.absolute(t_s)**2 * (n2 * cos_t) / (n1 * cos_i)
    T_p = np.absolute(t_p)**2 * (n2 * cos_t) / (n1 * cos_i)

    return {'r_p': r_p, 't_p': t_p, 'r_s': r_s, 't_s': t_s, 'R_p': R_p, 'T_p': T_p, 'R_s': R_s, 'T_s': T_s, 'theta_t': theta_t}