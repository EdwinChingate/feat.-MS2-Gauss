import numpy as np
def RandomVecGen(NPeaks):
    rng = np.random.default_rng()
    RandomVec=rng.random(size=NPeaks)
    return RandomVec
