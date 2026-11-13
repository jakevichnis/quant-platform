import numpy as np
from statsmodels.tsa.stattools import coint


def hedge_ratio(a, b):
    slope, intercept = np.polyfit(b, a, 1)
    return slope


def spread(a, b, ratio):
    return a - ratio * b


def check_pair(a, b, threshold=0.05):
    t_stat, p_value, _ = coint(a, b)
    return p_value < threshold, p_value

