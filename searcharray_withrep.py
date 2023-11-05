import random
from datetime import datetime
import sys

# function is used to perform a merge sort on a list, either in ascending or descending order.
def merge_sort(array, ascending=True):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left, ascending)
    right = merge_sort(right, ascending)

    return merge(left, right, ascending)

# This is the helper function that performs the actual merging of two sorted sublists into a single list.
def merge(left, right, ascending=True):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):

        # If ascending is True, it appends the smaller of the two elements to the result list.
        if ascending:
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        #  If ascending is False, it appends the larger element.
        else:
            if left[left_index] > right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

# function generates a random list of integers, counts values greater than 50, and performs the necessary sorting and modification based on the count.
def searcharray(n,m):
    loopcounter=0
    result = []
    count=0
    # Generates a random list of integers with n elements in the range from 1 to m
    for i in range(n):
        result.append(random.randint(1, m))
    #print (result)

    # Counts the number of values in the list that are greater than 50 and checks if there are more than 5 such values.
    for j in result:
        if j > 50:
            count=count+1
            if count>5:
                break
        else:
            continue
    if count > 5:
        #print("There are more than 5 values Greater than 50")
        result = merge_sort(result)
        #print("Sorting in Ascending order")
        #print(result)
        #print("Deleting the 5th Element")

        #  Deletes the 5th element from the sorted list.
        del(result[4])
        #print(result)

        # Inserting 10 in its correct place
        for k in result:
            if k >= 10:
                result.insert(loopcounter,10)
                break
            else:
                loopcounter=loopcounter+1

    elif count < 5:
        #print("There are less than 5 values Greater than 50")
        result= merge_sort(result,ascending=False)
        #print("Sorting in Descending order")
        #print(result)
        #print("Deleting the 2nd Element")

        #  Deletes the 2nd element from the sorted list.
        del(result[1])
        #print(result)

        # Inserting 10 in its correct place
        for k in result:
            if k <= 10:
                result.insert(loopcounter,10)
                break
            else:
                loopcounter=loopcounter+1
    return result

# function takes user input for the number of integers (n) and the ending range (m), and measures the execution time.
def main(n,m,r):
    looprun=0
    averagetimelist=[]
    while(looprun<r):
        starttime = datetime.now()
        spacetaken=0
        result = searcharray(n,m)
        #print("The final array is")
        #print(arrlist)
        endtime=datetime.now()
        elaspedtime=(endtime-starttime)
        #print("Total Time taken ",elaspedtime, "seconds")
        averagetimelist.append(elaspedtime.microseconds)
        looprun= looprun+1
    averagetime= sum(averagetimelist)//r
    spacetaken=sys.getsizeof(result)
    print("Times for ",r," repetitions is ",averagetimelist)
    print("Average time ", averagetime, " microseconds")
    print("Space taken is ",spacetaken," bytes")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of integers n: "))
            if n <= 5:
                raise ValueError("Please enter 'n' value greater than 5 ")

            m = int(input("Enter the ending range of integers m: "))
            r = int(input("Enter the value of repetitions r: "))
            main(n, m, r)
            break
        except ValueError as error:
            print(f"Error: {error}")