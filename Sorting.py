import time
class Sorting:

    #Bubble Sort
    def bubblesort(arr):
        startTime = time.time()
        for x in range(0, len(arr)):
          for y in range(0, len(arr)-x-1):
            if arr[y] > arr[y+1] :
              arr[y], arr[y+1] = arr[y+1], arr[y]
        endTime = time.time()
        print(arr)
        print("Time taken for Bubble Sort {}".format(endTime-startTime))

    #Selection Sort
    def selectionSort(arr):
        startTime = time.time()

        for i in range(len(arr)):
          # Find the minimum element in remaining
           minPosition = i
           for j in range(i+1, len(arr)):
               if arr[minPosition] > arr[j]:
                   minPosition = j
           # Swap the found minimum element with minPosition
           temp = arr[i]
           arr[i] = arr[minPosition]
           arr[minPosition] = temp
        endTime = time.time()
        print(arr)
        print("time taken for selection sort: {}".format(endTime-startTime))
