from objloader import OBJ
import numpy as np
np.float128 = np.float64
np.complex256 = np.complex128
factory = {}

def get_model(path):
    if path not in factory:
        factory[path] = OBJ(path)
        factory[path].generate()

    return factory[path]




