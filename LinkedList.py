class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return '(' + str(self.data) + ') '


class LinkedList:
    def __init__(self,root = None):
        self.root = root
        self.size = 0

    def add(self,data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prv_node = None
        while this_node is not None:
            if this_node.data == d:
                if prv_node is None:
                    self.root = this_node.next
                    self.size -= 1
                    return this_node.data
                else:
                    prv_node.next = this_node.next
                    self.size -= 1
                    return this_node.data

            prv_node = this_node
            this_node = this_node.next        
        return None
        
    def find(self, d):
        this_node = self.root
        pos =1
        while this_node is not None:
            if this_node.data == d:
                print("{} found at {}".format(d, pos))
                return True
            pos += 1
            this_node = this_node.next
        print('{} is not in list'.format(d))    
        return False
    
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end = '->')
            this_node = this_node.next
        print('None')


def main():
    ll = LinkedList()
    for i in range(5):
        x = int(input())
        ll.add(x)
        ll.print_list()
    result = ll.find(int(input('Find data in list\n')))
    while(ll.size!=0):
        ll.remove(int(input('enter item to delete from list\n')))
        ll.print_list()

if __name__ == '__main__':
    main()

