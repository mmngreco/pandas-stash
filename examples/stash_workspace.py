import pandas as pd
import numpy as np

arr1 = np.array([1,2,3])
a = 1
b = "a"
d = dict(a=1, b=b, c=arr1)

import pandas_stash as pds
pds.stash(frame=globals(), overwrite=True)

import pandas_stash as pds
pds.unstash(overwrite=True)
d
arr1
