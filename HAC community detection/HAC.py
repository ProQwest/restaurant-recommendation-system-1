import json
import numpy as np
from collections import Counter
from scipy.sparse import coo_matrix
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix

#merge two clusters have the best improvement
def merge(i,j,cluster):
	cluster[j] = cluster[i] + cluster[j]
	del cluster[i]
	return cluster

#update the matrix
def update(i,j,Q,a):
	for k in range(0,len(a)):
		if (Q[i,k]!= 0 and Q[j,k]!=0):
			Q[j,k] = Q[i,k] + Q[j,k]
			Q[k,j] = Q[j,k]
			Q[i,k] = 0
			Q[k,i] = 0
		elif(Q[i,k]!=0 and Q[j,k] == 0):
			Q[j,k] = Q[i,k] - 2*a[j]*a[k]
			Q[k,j] = Q[j,k]
			Q[i,k] = 0
			Q[k,i] = 0
		elif(Q[i,k]==0 and Q[j,k]!=0):
			Q[j,k] = Q[j,k] - 2*a[i]*a[k]
			Q[k,j] = Q[j,k]	
		Q[i,j] = 0
		Q[j,i] = 0
		Q[i,i] = 0 
		Q[j,j] = 0
	return Q

def newa(i,j,a):
    a[j] = a[i] + a[j]
    a[i] = 0
    return a	

#find the best in Q's index,thus the next to imerge
def find_max(Q,n):
	T = Q.todense()
	I = np.argmax(T)
	p = I/n
	q = I%n
	T = []
	return (p,q)


def run():
	pair = []
	review = []
	for line in open("pair.txt"):
		temp = eval(line) 
		pair.append(temp)
		review.append(temp[0])

	review_count = Counter(review)
	pair_count   = Counter(pair)
	n = len(review_count)

	row = []
	col = []
	#the jaccard similarity
	jac = []
	for key in pair_count.keys():
		r = key[0]
		c = key[1]
		j = float(pair_count[key])/(review_count[r]+review_count[c]-pair_count[key])
		row.append(r)
		col.append(c)
		jac.append(j)

	with open('rcj.txt','w') as f:
		for i in range(0,len(row)):
			f.write(str(row[i]))
			f.write(',')
			f.write(str(col[i]))
			f.write(',')
			f.write(str(jac[i]))
			f.write('\n')
	#filt out those pair with certian threshold,just built lines for those great on the threshold
	new_row = []
	new_col = []
	new_jac = []
	for i in range(0,len(jac)):
		if jac[i]>0.003:
			new_jac.append(jac[i])
			new_row.append(row[i])
			new_col.append(col[i])

	A = coo_matrix((new_jac,(new_row,new_col)),shape = (n,n))
	A = A.tocsr()
	T = A.todense()
	k = []
	x = T.sum(axis = 1)
	for i in range(0,n):
		k.append(x[i].max())
	m = sum(k)/2

	cluster = {}
	for i in range(0,n):
		cluster[i] = [i]

	a = []
	for i in range(0,n):
		a.append(k[i]/(2*m))

	delta = []
	for i in range(0,len(new_jac)):
		t = 1/(2*m)-k[new_row[i]]*k[new_col[i]]/(4*m*m)
		delta.append(t)

	Q = coo_matrix((delta,(new_row,new_col)),shape = (n,n))
	Q = Q.tocsr()
	Q = lil_matrix(Q)

	stop = n - 1000
	count = 0
	# the criteria is based on your choice.
	while count < stop:
		t = find_max(Q,n)
		i = t[0]
		j = t[1]
		cluster = merge(i,j,cluster)
		Q = update(i,j,Q,a)
		a = newa(i,j,a)
		count = count + 1
		print count

	with open('final_community.json','w') as f:
		json.dump(cluster,f,indent = 2)


if __name__ == '__main__':
	run()