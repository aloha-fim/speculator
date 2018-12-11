import numpy as np
from numpy.linalg import norm
from ast import literal_eval
from operator import itemgetter

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# convert each dict of values back into an ndarray
def fromZeroes(data):
    features = literal_eval(data)
    narray = np.zeros((1,7,7,512))

    for i, first in features.items():
        for j, second in first.items():
            for k, third in second.items():
                for l, fourth in third.items():
                    narray[i][j][k][l] = fourth

    return narray

def findClosest(photo, iarray):
    closest = []
    for image in iarray:
        comparison = {
            'mlsnum': image.mlsnum,
            'closeness': norm(photo - fromZeroes(image.features))
        }
        closest.append(comparison)

    closest.sort(key=itemgetter('closeness'))
    # only return the top five
    return [c['mlsnum'] for c in closest[:5]]
