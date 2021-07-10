import time
from math import floor
class Searching:
    def linearSearch(arr):

        #Time Start
        time_start = time.time()

        #search algorithm
        search = int(input("enter a number: "))
        position = 0
        isFound = False
        for i in range(0,len(arr)):
            position = i + position
            if (arr[i] == search) and not isFound:
                print("Yes, element {} present in list".format(search))
                print("Element position: {}".format(position))
            else:
                print("NOPE!!!!!!!")

        #Time End
        time_end = time.time()
        time_taken = time_end - time_start
        print("Time Taken to run: {}".format(time_taken))


    def binary_search(Array):

        Search_Term = int(input("Enter search term: "))
        length = len(Array)
        start = 0
        current_position = length-1
        while start <= current_position:
            midpoint = floor((start+current_position)/2)
            if Array[midpoint] < Search_Term:
                start = midpoint + 1
            elif Array[midpoint] > Search_Term:
                current_position = midpoint - 1
            else:
                return midpoint
        return -1
