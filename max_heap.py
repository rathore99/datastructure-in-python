'''1. implement maxheap using list
2. operations to implement 
   i) push()
  ii) pop()
 iii) peek()
''' 
class MaxHeap:
    def __init__(self, items = [] ):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatup(len(self.heap)-1)
        print(self.__str())
    # Function to insert element in heap
    def push(self, item):
        self.heap.append(item)
        self.__floatup(len(self.heap)-1)
        self.printHeap()
    
    def pop(self):
        if len(self.heap) < 2:
            print("heap is empty ...no item available to pop ")
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            self.__swap(len(self.heap)-1, 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
            return max
    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return False

    def __floatup(self, index):
        parent = index // 2
        child = index
        if self.heap[child] > self.heap[parent] and parent > 0:
            self.__swap(child,parent) 
            self.__floatup(parent)
        else:
            return 
    def __bubbleDown(self, parent):
        right = 2 * parent + 1 
        left  = 2 * parent
        if left <= len(self.heap)-1 and self.heap[parent] < self.heap[left] :
            self.__swap(left, parent)
            self.__bubbleDown(left)
        if right <= len(self.heap)-1 and self.heap[parent] < self.heap[right] :
            self.__swap(right, parent)
            self.__bubbleDown(right)
        else:
            print("heap after deletion ")
            self.printHeap()
            return
        return    
    def __str(self):
        return str(self.heap)

    def __swap(self, child, parent):
        self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
        return 
    def printHeap(self):
        print(self.__str())
    


def main():
    
    while(True):
        print('''play with max heap 
        1. create heap(for once) 
        2. push element
        3. pop element
        4. find max
        5. print heap
        6. exit()''')
        option = int(input())
        if option == 6:
            break
        else:
            if option == 1:
               list = [int(x) for x in input().split()]
               obj = MaxHeap(list)
            elif option == 2:
                print('enter element to push in heap ')
                element = int(input())
                obj.push(element)   
            elif option == 3:
                print("element popped is ", obj.pop())
            elif option == 4:
                print('''Max element in heap is: ''', obj.peek() )
            elif option == 5:
                obj.printHeap()
        
if __name__ == '__main__':
    main()