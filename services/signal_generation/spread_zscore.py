import numpy as np

def zscore(values):
    mean = np.mean(values)
    std = np.std(values)
    if std == 0:
        return 0.0
    return (values[-1] - mean) / std