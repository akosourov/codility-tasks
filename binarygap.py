def solution(N):
	gap = 0
	n_bin = bin(N)[2:]
	gap_temp = 0
	prev_el = next_el = None
	j = None

	for i in range(len(n_bin)):
		elem = n_bin[i]
		if i > 0:
			prev_el = n_bin[i-1]
		else:
			prev_el = None
		if i < len(n_bin) - 1:
			next_el = n_bin[i+1]
		else:
			next_el = None

		if elem == '1':
			if prev_el == '0' or next_el == '0':
				if j is None:
					j = i
				else:
					gap_temp = i - j - 1
					if gap_temp > gap:
						gap = gap_temp
					j = i

	return gap


if __name__ == '__main__':
	import sys

	if len(sys.argv) > 1:
		N = int(sys.argv[1])
		print(bin(N), solution(N))
	else:
		# tests
		print('solution(9)', bin(9)[2:], solution(9), 2)
		print('solution(17)', bin(17)[2:], solution(17), 3)
		print('solution(145)', bin(145)[2:], solution(145), 3)
		print('solution(529)', bin(529)[2:], solution(529), 4)
		print('solution(1041)', bin(1041)[2:], solution(1041), 5)
