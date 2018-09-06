'''
Kristina Kolibab
Blockchain Lab 1
Sept. 6, 2018

Results:
	Searching for '000000' gives me
		name:  Kristina
		nounce:  32981133
		sol:  000000aba5ff2160311f20cf85f5c5b49f3f785e4da4399375c58273029161db
	This obviously goes past the 5 mins I had originally set as a timer, 
	but when that functinality is removed my program is able to find an answer

	Searching for '00000' gives me
		name:  Kristina
		nounce:  184109
		sol:  00000d412591eda0322c9bc157d9d929496a5b3bf2d0ed9b2884f581154ee69e
	This will complete in under 5 mins, subsequently anything less than 6 0's
	will run just fine in the time alloted. Feel free to comment out lines 39-42
	if you plan to test my program against 6 0's 
'''

import hashlib, time

def main():

	# set variables
	s = "Kristina"
	target = "000000246565"
	i = 0
	timeout = time.time() + 60*5
	str_hash = hashlib.sha256((s+str(i)).encode()).hexdigest()
	sol = True

	# loop
	while(target[:5] != str_hash[:5]):
		str_hash = hashlib.sha256((s+str(i)).encode()).hexdigest()
		print(i, ": ", str_hash)
		i += 1
		# time limit of 5 mins
		if(time.time() > timeout):
			print("time out, no solution found")
			sol = False
			break
		
	if(sol != False):
		# print solution	
		print("name: ", s)
		print("nounce: ", i)
		print("sol: ", str_hash)

if __name__ == "__main__":
	main()

