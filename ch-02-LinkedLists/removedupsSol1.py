class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def countNodes(self):
        val = self.headval
        dic = {}
        while val is not None:
            if val.dataval in dic:
                dic[val.dataval] += 1
            else:
                dic[val.dataval] = 1
            val = val.nextval
        return dic

    def Nodestoremove(self):
        dic = self.countNodes()
        dic = {key: value for key,value in dic.items() if value>1}
        res = []
        for k,v in dic.items():
            while v>1:
                res.append(k)
                v -= 1
        return res


    def removeNode(self,key):
        #https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
        val = self.headval
        if val is not None:
            if (val.dataval == key):
                self.headval = val.nextval
                val = None
                return
        while val is not None:
            if val.dataval == key:
                break
            prev = val
            val = val.nextval
        #if we arrive at the end of the linked list
        # we do nothing -> break
        if val == None:
            return
        # we skip the val.dataval (the value of the key)
        prev.nextval = val.nextval

        #val = None
    
    def displayLList(self):
        printval = self.headval
        res = ''
        while printval:
            res += printval.dataval
            printval = printval.nextval
        print(res)

               
def main():
    linkedlist = SLinkedList()
    linkedlist.headval = Node("i")
    e1 = Node("i")
    e2 = Node("s")
    e3 = Node("s")
    e4 = Node("o")
    e5 = Node("u")
    e6 = Node("u")
    e7 = Node("u")
    linkedlist.headval.nextval = e1
    e1.nextval = e2
    e2.nextval = e3
    e3.nextval = e4
    e4.nextval = e5
    e5.nextval = e6
    e6.nextval = e7
    linkedlist.displayLList()
    for i in linkedlist.Nodestoremove():
        linkedlist.removeNode(i)
    linkedlist.displayLList()
    print(linkedlist.headval.dataval)


if __name__ == '__main__':
        main()