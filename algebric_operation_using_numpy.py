import numpy as np
c=0
n=input("enter the length of the array:")
m= np.array(input("enter the array :"))
print "the det of the matrix:",np.linalg.det(m)
print "the inv of the matrix:",np.linalg.inv(m)
print "the eigen values of the matrix:",np.linalg.eig(m)
print "the singular values of the matrix:",np.linalg.svd(m)
print "the rank of the matrix:",np.rank(m)
print "the meof dian value the matrix:",np.median(m)
print "the maximum of the matrix:",np.max(m)
print "the minimum of the matrix:",np.min(m)
print "the transpose of the matrix:",np.transpose(m)
