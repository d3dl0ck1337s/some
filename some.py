#!/usr/bin/env python3
import sys
from PIL import Image
import numpy as np
flag = '<redacted>'
chars = np.asarray(list('~^r%K9#'))
SC, GCF, WCF = 1/10, 1, 7/4
img = Image.open('image.png')
S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
img = np.sum( np.asarray( img.resize(S) ), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)
arr = chars[img.astype(int)]
arr = '\n'.join(''.join(row) for row in arr)
print(arr)
try:
    eval(arr)
except SyntaxError:
	pass