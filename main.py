import numpy as np
import sys

def random_assymetric_matrix(n, draw_proba):
	win_threshold = (1+draw_proba)/2 # assumes equal chances
	# suboptimal, nxn random values instead of n(n-1)/2
	A = np.random.rand(n,n)
	A[A>win_threshold] = 1
	A[np.logical_and(A<win_threshold,A>draw_proba)] = -1
	A[np.logical_and(A>0,A<draw_proba)] = 0
	A = np.triu(A,k=1)
	A = A - A.transpose()
	return A
	

def create_random_tournament(n,p = 1, draw_proba=0.05):
	# INPUTS
	# n: number of players
	# p: number of games each player plays with another
	# draw_proba: probability of a draw, see e.g https://chess.stackexchange.com/questions/23807/what-is-the-draw-frequency-for-3-consecutive-games-same-players-amateur-level
	#
	# OUTPUTS
	# M: n x n matrix with values between -p and p
	
	M = np.zeros((n,n))
	for game in range(p):
		A = random_assymetric_matrix(n,draw_proba)
		M = M + A
	return M
	

def 2D_projection(M):
	eigval, eigvec = np.linalg.eig(M) # complex eigenvalues but conjugate ! => 2D MDS is possible
	print(np.abs(eigval))
	

if __name__ == "__main__":
	if len(sys.argv) >= 1:
		n = 10
		p = 1
	if len(sys.argv)>=2:
		n = int(sys.argv[1])
	if len(sys.argv)>=3:
		p = int(sys.argv[2])
	M = create_random_tournament(n,p)
	#print(M)
	2D_projection(M)
