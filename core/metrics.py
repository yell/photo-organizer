import numpy as np
import sklearn
import sklearn.metrics
import scipy


def distance(u, v, metric_index=0):
    assert len(u) == len(v)
    u = np.array(u)
    v = np.array(v)
    # if metric_index == 12:
        # return scipy.spatial.distance.minkowski(u, v, p=2.),
    return {
        0: sklearn.metrics.mean_squared_error, # <-
        # 1: sklearn.metrics.median_absolute_error,
        # 2: sklearn.metrics.mean_absolute_error, # <-
        # 3: sklearn.metrics.r2_score,
        # 4: sklearn.metrics.explained_variance_score,
        5: scipy.spatial.distance.braycurtis, # <-
        # 6: scipy.spatial.distance.canberra, # <-
        # 7: scipy.spatial.distance.chebyshev,
        # 8: scipy.spatial.distance.cityblock,
        9: scipy.spatial.distance.cosine, # <-
        # 10: scipy.spatial.distance.hamming,
        # 11: scipy.spatial.distance.sqeuclidean
    }[metric_index](u, v)

def mahalanobis(u, v, VI):
    u, v = np.array(u), np.array(v)
    w = u - v
    return np.sqrt(np.absolute(w.dot(VI.dot(w))))