#!/usr/bin/python
import sys, math, time, os
import multiprocessing as mp
from multiprocessing import Process, Queue

class primeObject:
	def __init__(self, evalNumber, isPrime):
		self.evalNumber = evalNumber
		self.isPrime = isPrime

def calcPrimeErastos(numProcs, calcRange, endTime):
	print ("Calcing primes with ancient method.  Yeay Greeks!")
	# This is a place holder initializer until I setup the multiple threads.
	# At this time each individual thread will have a number which I will 
	# multiply by the calc range to 

	# This index is to help me keep track of which index I am adding which prime to
	# Essentially all it is is a glorified counter for my lists. 
	evalNumber = (0 * calcRange) + 1	#Used to put the numbers into the lists for record keeping. Will be replaced.
	evalIndex = 0	#Will be used in the loops to ensure I have not gone beyond the list extents.
	startIndex = 0		#0 * calcRange
	listLength = int(calcRange / 2)
	endIndex = startIndex + calcRange
	primeList = []
	divisor = 3
	highestCurNum = 0
	curPossiblePrime = 0

	# outermost while loop of evaluation will start here
	# Append to the list as needed.  Move the initialization loops into this outer while loop.

	print ("Start number: " + str(startIndex))
	print ("End number: " + str(endIndex))

	if evalNumber == 1:
		for i in range(startIndex, endIndex):
			if evalNumber == 1:
				primeList.append(primeObject(evalNumber, True))
				primeList.append(primeObject(2, True))
				evalNumber += 2			
			primeList.append(primeObject(evalNumber, True))	
			evalNumber += 2
	else:
		for i in range(startIndex, endIndex):			
			primeList.append(primeObject(evalNumber, True))	
			evalNumber += 2
	
	if primeList[0].evalNumber < 3:
		print ("Prime found: " + str(1))
		print ("Prime found: " + str(2))
	
	highestCurNum = primeList[listLength - 1].evalNumber
	print ("highestCurNum: " + str(highestCurNum))
	print ("listLength: " + str(listLength))

	while divisor < highestCurNum:
		while evalIndex < listLength:
			curPossiblePrime = int(primeList[evalIndex].evalNumber)
			if (curPossiblePrime / divisor) > 1 and (curPossiblePrime % divisor) == 0 \
			and (curPossiblePrime != divisor):
				primeList[evalIndex].isPrime = False
			evalIndex += 1
		evalIndex = 0
		divisor += 2

	print ("highestCurNum: " + str(highestCurNum))
	
	# highestCurNum += (numProcs * calcRange) - 96 Not sure if this is needed.
	print ("highestCurNum: " + str(highestCurNum))
	# End outermost while loop.

	for i in range(startIndex, listLength):
		print ("Index: " + str(i) + " evalNumber: " + str(primeList[i].evalNumber) \
			+ " isPrime: " + str(primeList[i].isPrime))

def main(args):
	print("The first line in my program.")
	runTime = float(args[2])
	calcRange = int(args[1])

	numProcs = mp.cpu_count()
	timeLeft = runTime
	endTime = time.time() + runTime

	calcPrimeErastos(numProcs, calcRange, endTime)

if __name__ == '__main__':
	main(sys.argv)