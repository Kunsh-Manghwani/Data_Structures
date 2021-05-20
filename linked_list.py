class node:
    def __init__(self, data):
        self.val = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insertbeg(self, key):
        n_new = node(key)
        n_new.next = self.head
        self.head = n_new

    def insertend(self, key):
        h = self.head
        if h is None:
            n_new = node(key)
            self.head = n_new
        else:
            while h.next is not None:
                h = h.next
            n_new = node(key)
            h.next = n_new

    def insertafter(self, n_after, key):
        h = self.head
        if h is None:
            print("The node cannot be inserted as the list doesn't exist")
            return
        else:
            while h.val != n_after:
                h = h.next
                if h is None:
                    print("The Node cannot be inserted")
                    return
            n_new = node(key)
            n_new.next = h.next
            h.next = n_new

    def deletenode(self, key):
        h = self.head
        prev = None
        if h is None:
            print("The list is Empty.Therefore, the node cannot be deleted")
            return
        if h.val == key:
            self.head = h.next
            return
        while h is not None and h.val != key:
            prev = h
            h = h.next
        if h is None:
            print("The value is not present in the list")
        else:
            prev.next = h.next

    def deletebeg(self):
        h = self.head
        if h is None:
            print("The list is Empty.Therefore, the node cannot be deleted")
            return
        self.head = h.next

    def delete_end(self):
        h = self.head
        if h is None:
            print("The list is Empty.Therefore, the node cannot be deleted")
            return
        while h.next.next is not None:
            h = h.next
        h.next = None

    def nth_nodefromlast(self, n):
        prev = self.head
        curr = self.head
        if self.head is None:
            print("The list doesn't exist")
            return
        for i in range(n):
            if curr is not None:
                curr = curr.next
            else:
                print("Enough nodes are not present in the linked list")
                return
        while curr is not None:
            curr = curr.next
            prev = prev.next
        print("Data from Nth last node is ", prev.val)

    def nth_nodefromstart(self, n):
        h = self.head
        if h is None:
            print("The list doesn't exist")
            return
        for i in range(n-1):
            h = h.next
            if h is None:
                print("Enough nodes are not present in the linked list")
                return
        print("Data from Nth first Node is", h.val)

    def middleoflist(self):
        slow = self.head
        fast = self.head
        if self.head is None:
            print("The list is empty")
            return
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Data of the middle of the Liked List is", slow.val)

    def printlist(self):
        h = self.head
        while h is not None:
            print(h.val, end=" -> ")
            h = h.next
        print("None")


if __name__ == '__main__':
    c = 0
    l = linkedlist()
    while 1:
        print("0-- Exit(Default)")
        print("1-- print list")
        print("2-- Insert at end")
        print("3-- Insert at beginning")
        print("4-- Insert after a Node")
        print("5-- Delete Node with a particular value")
        print("6-- Delete node from beginning")
        print("7-- Delete node from end")
        print("8-- Data of nth node from last")
        print("9-- Data of nth node from Beginning")
        print("10-- Data from the middle of the linked List")
        try:
            c = int(input("Enter your choice:- "))
        except ValueError:
            print("Sorry! your choice is invalid. Please try again")
            continue
        if c == 0:
            break
        elif c == 1:
            l.printlist()
        elif c == 2:
            item = int(input("Enter the value:- "))
            l.insertend(item)
        elif c == 3:
            item = int(input("Enter the value:- "))
            l.insertbeg(item)
        elif c == 4:
            node_after = int(input("Enter the after value:- "))
            item = int(input("Enter the value:- "))
            l.insertafter(node_after, item)
        elif c == 5:
            item = int(input("Enter the value to be deleted:- "))
            l.deletenode(item)
        elif c == 6:
            l.deletebeg()
        elif c == 7:
            l.delete_end()
        elif c == 8:
            item = int(input("Enter the index of node from last:- "))
            l.nth_nodefromlast(item)
        elif c == 9:
            item = int(input("Enter the index of node from Start:- "))
            l.nth_nodefromstart(item)
        elif c == 10:
            l.middleoflist()
        else:
            print("Sorry! Wrong choice. Please Enter Once again")
    print("\nYou have successfully Executed the Linked List program created by Kstar")
