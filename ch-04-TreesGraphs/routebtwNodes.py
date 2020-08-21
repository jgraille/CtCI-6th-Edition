class Node:
  def __init__(self,n,adjacent=None):
    self.n = n
    self.adjacent = adjacent
    self._marked = False
  
  @property
  def marked(self):
    return self._marked

  @marked.setter
  def marked(self,value):
    if isinstance(value,bool):
      self._marked = value
    else:
      raise TypeError("Value is not a boolean")

class Queue:
  def __init__(self,listQueue=None):
    self.listQueue = listQueue
  def addElement(self,val):
    self.listQueue.append(val)
    return self.listQueue
  def removeElement(self):
    if self.listQueue:
      return self.listQueue.pop(0)

def routebtwNodes(Nodestart,end):
  thequeue = Queue([])
  Nodestart.marked = True
  thequeue.addElement(Nodestart)
  if thequeue.listQueue:
    print(thequeue.listQueue)
  else:
    print('empty')
    print(thequeue.listQueue)
  while thequeue.listQueue:
    node_r = thequeue.removeElement()
    for n in node_r.adjacent:
      if n.marked == False:
        n.marked = True
        thequeue.addElement(n)

def main():
  G = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
      }
  g = { "F" : ["I"],
        "B" : ["J"],
        "G" : ["D","H"],
        "C" : ["G"],
        "A" : ["B","C","D"],
        "E" : ["F","A"],
        "D" : ["A"]
        }
  node_f = Node("F",[Node("I")])
  node_e = Node("E",[Node("F"),Node("A")])
  routebtwNodes(node_e,"I")

if __name__ == '__main__':
  main()