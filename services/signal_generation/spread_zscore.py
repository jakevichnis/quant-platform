import numpy as np

def zscore(values):
    mean = np.mean(values)
    std = np.std(values)
    return (values[-1] - mean) / std