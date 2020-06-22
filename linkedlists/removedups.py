class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


def main():
    linkedlist = SLinkedList()
    linkedlist.headval = Node("i")
    e2 = Node("s")
    e3 = Node("s")
    e4 = Node("o")
    e5 = Node("u")
    linkedlist.headval.nextval = e2
    e2.nextval = e3
    e3.nextval = e4
    e4.nextval = e5



if __name__ == '__main__':
        main()