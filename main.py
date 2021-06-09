import numpy as np
import sys


def create_random_tournament(n,p = 1, draw_proba=0.05):
	# INPUTS
	# n: number of players
	# p: number of games each player plays with another
	# draw_proba: probability of a draw, see e.g https://chess.stackexchange.com/questions/23807/what-is-the-draw-frequency-for-3-consecutive-games-same-players-amateur-level
	#
	# OUTPUTS
	# M: n x n matrix with values between -p and p
	
	M = np.zeros((n,n))
	win_threshold = (1+draw_proba)/2 # assumes equal chances
	for game in range(p):
		A = np.random.rand((n,n))
		A[A>win_threshold] = 1
		A[np.logical_and(A<win_threshold,A>draw_proba)] = -1
		A[np.logical_and(A>0,A<draw_proba)] = 0
		M = M + A
	return M
	

if __name__ == "__main__":
	if len(sys.argv) == 1:
		n = 10
	else:
		n = int(sys.argv[1])
	M = create_random_tournament(n,p)
	print(M)
