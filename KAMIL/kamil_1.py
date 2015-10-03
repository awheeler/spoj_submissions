import sys
for w in sys.stdin:
	t=1
	for c in list(w):
		if c in {'T','D','L','F'}:
			t*=2
	print t
