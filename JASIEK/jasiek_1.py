from sys import stdin, exit

def key_to_direction(key) :
	switcher = {
		'N': [ 0, 1 ],
		'S': [ 0, -1],
		'E': [ 1, 0],
		'W': [ -1, 0]
	}
	return switcher.get(key)
		
def parse_list():
	# Initialize a hashmap
	locations = {}

	# Initialize coordinates
	x = 0
	y = 0
	locations [ x,y ] = 1


	# Read the lines, updating the hashmap with the calculated locations
	found_k = 0
	lc = 0
	minx=0
	miny=0
	maxx=0
	maxy=0
	while not found_k:
		lc += 1
		direction = stdin.readline().strip()
		if direction == 'K':
			found_k = 1
		else:
			(xdir, ydir) = key_to_direction(direction)
			x = x+xdir
			y = y+ydir
			locations[ x,y ] = 1
		
			if x > maxx:
				maxx=x
			elif x< minx:
				minx=x
			elif y > maxy:
				maxy=y
			elif y < miny:
				miny=y
	
	# Walk the map looking for holes and fill them
	for x in range(minx+1,maxx-1):
		for y in range(miny+1,maxy-1):
			if (x,y) not in locations:
				if (x-1,y) in locations and (x+1,y) in locations:
					locations[ x,y ] = 1
				elif (x,y-1) in locations and (x,y+1) in locations:
					locations[ x,y ] = 1

	return len(locations)

count = 0
for count in range(2):
	# Read the first character, which should be P
	P = stdin.readline().strip()
	print parse_list()
