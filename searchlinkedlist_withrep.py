import random
from datetime import datetime
import sys
# This class defines the individual nodes of the doubly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# This class defines the doubly linked list data structure.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Inserts a new node with the given data at the end of the list.
    def insertdata(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Deletes the first occurrence of a node with the specified data value from the list.
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    #  Converts the DLL to a regular Python list and returns it.
    def converttolist(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Inserts a new node with the given data in a sorted manner, either in ascending or descending order based on the ascending parameter.
    def insert_sorted(self, data, ascending=True):
        new_node = Node(data)
        current = self.head
        while current:
            if (ascending and data < current.data) or (not ascending and data > current.data):
                if current.prev is None:
                    new_node.next = current
                    current.prev = new_node
                    self.head = new_node
                else:
                    new_node.next = current
                    new_node.prev = current.prev
                    current.prev.next = new_node
                    current.prev = new_node
                return
            current = current.next
            
        if current is None:
            if self.head is None:
                self.head = new_node
            else:
                last_node = self.head
                while last_node.next:
                    last_node = last_node.next
                last_node.next = new_node
                new_node.prev = last_node

    # method for quick sorting the linked list in either ascending or descending order.
    def quick_sort(self, start, end, ascending=True):
        if start == end or end is None or start == end.next:
            return start

        pivot = self.partition(start, end, ascending)

        if ascending:
            if pivot.prev:
                self.quick_sort(start, pivot.prev, ascending)
            if pivot.next:
                self.quick_sort(pivot.next, end, ascending)
        else:
            if pivot.next:
                self.quick_sort(pivot.next, end, ascending)
            if pivot.prev:
                self.quick_sort(start, pivot.prev, ascending)

    # method for partitioning the linked list during quick sort.
    def partition(self, start, end, ascending):
        pivot = end.data
        current = start
        while current != end:
            if ascending:
                if current.data <= pivot:
                    current.data, start.data = start.data, current.data
                    start = start.next
            else:
                if current.data >= pivot:
                    current.data, start.data = start.data, current.data
                    start = start.next
            current = current.next
        end.data, start.data = start.data, end.data
        return start

    # Initiates the sorting of the entire linked list using quick sort.
    def sort(self,ascending=True):
        self.quick_sort(self.head, self.tail,ascending)

    def printdll(self):
        if self.head is None:
            return
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
    def get_size(self):
        dllsize = sys.getsizeof(self.head)
        current = self.head
        while current.next:
            dllsize += sys.getsizeof(current.next)
            current = current.next
        return dllsize

def main(n, m, r):
    looprun=0
    averagetimelist=[]
    while(looprun<r):
        starttime = datetime.now()
        
        # Creates a DoublyLinkedList instance and populates it with n random integers in the range from 1 to m.
        linked_list = DoublyLinkedList()
        for i in range(n):
            linked_list.insertdata(random.randint(1, m))
        #print(linked_list.printdll())
        count = 0

        # Counts the number of values greater than 50 in the linked list.
        for x in linked_list.converttolist():
            if x > 50:
                count += 1
                if count > 5:
                    break
        if count > 5:
            #print("There are more than 5 values Greater than 50")
            #print("Sorting in Ascending order")
            linked_list.sort(ascending=True)
            #print(linked_list.printdll())
            #print("Deleting the 5th Element")
            linked_list.delete(linked_list.converttolist()[4])
            #print(linked_list.printdll())
            linked_list.insert_sorted(10)
        else:
            #print("There are lesser than 5 values Greater than 50")
            #print("Sorting in Descending order")
            linked_list.sort(ascending=False)
            #print(linked_list.printdll())
            #print("Deleting the 2nd Element")
            linked_list.delete(linked_list.converttolist()[1])
            #print(linked_list.printdll())
            linked_list.insert_sorted(10,ascending=False)

        #print("Inserted 10 in its correct place")
        #print(linked_list.printdll)
        endtime=datetime.now()
        elaspedtime=(endtime-starttime)
        averagetimelist.append(elaspedtime.microseconds)
        looprun= looprun+1
    averagetime= sum(averagetimelist)//len(averagetimelist)
    print("Times for ",r," repetitions is ",averagetimelist)
    print("Average time ", averagetime," microseconds")
    spacetaken=linked_list.get_size()
    print("Space taken is ",spacetaken," bytes")



# takes user input for the number of integers (n) and the ending range (m).
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